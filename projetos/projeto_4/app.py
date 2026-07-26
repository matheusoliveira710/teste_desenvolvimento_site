import sys
import threading
import requests
import sqlite3
from flask import Flask, request, jsonify
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                            QLineEdit, QPushButton, QLabel, QMessageBox, QHBoxLayout, QComboBox, QListWidget)
from PyQt5.QtCore import Qt, pyqtSignal, QObject

# --- CONFIGURAÇÃO DO DISCORD ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1530201924735991950/-lJM5Hu5KMaWZFzcwcR3kabzUnbKdVZdx9w-a2BRMAb-23roIjJY2g4ELCtdfGUezrPP"

# --- PONTE DE SINAIS ENTRE THREADS ---
class WorkerSignals(QObject):
    novo_dado = pyqtSignal(str, str)

signal_bridge = WorkerSignals()

# --- MINI SERVIDOR FLASK EM SEGUNDO PLANO ---
flask_app = Flask(__name__)

@flask_app.route('/webhook-discord', methods=['POST'])
def receber_do_discord():
    data = request.json
    texto = data.get('text')
    quadrante = data.get('quadrant', 'Fazer Agora')
    
    if texto:
        signal_bridge.novo_dado.emit(texto, quadrante)
        return jsonify({"status": "Sucesso"}), 200
    return jsonify({"error": "Dados inválidos"}), 400


# --- ROTA PARA RECEBER COMANDOS DO CHAT (EX: !adicionar) ---
@flask_app.route('/comando-chat', methods=['comando_chat'])
@flask_app.route('/comando-chat', methods=['POST'])
def comando_chat():
    data = request.json
    mensagem = data.get('mensagem', '').strip()
    
    if mensagem.startswith("!adicionar"):
        try:
            conteudo = mensagem.replace("!adicionar", "").strip()
            
            if "[" in conteudo and "]" in conteudo:
                quadrante = conteudo.split("[")[1].split("]")[0].strip()
                texto = conteudo.split("]")[1].strip()
            else:
                quadrante = "Fazer Agora"
                texto = conteudo
                
            mapa_quadrantes = {
                "Fazer Agora": "Fazer Agora",
                "Agendar": "Agendar",
                "Delegar": "Delegar",
                "Eliminar": "Eliminar"
            }
            
            q_final = mapa_quadrantes.get(quadrante, "Fazer Agora")
            
            if texto:
                signal_bridge.novo_dado.emit(texto, q_final)
                return jsonify({"status": f"Sucesso! Tarefa adicionada em '{q_final}'."}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
            
    return jsonify({"error": "Comando não reconhecido. Use !adicionar [Quadrante] Texto"}), 400

def rodar_servidor():
    flask_app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)


# --- APLICAÇÃO DESKTOP PYQT5 ---
class EisenhowerDesktop(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_db()
        self.setWindowTitle("Matriz de Eisenhower - Desktop Pro")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f4f6f9; font-family: 'Segoe UI', Arial;")

        # Conecta o sinal do Flask à função de adicionar item na tela
        signal_bridge.novo_dado.connect(self.adicionar_item_externo)

        # Layout Principal
        central_widget = QWidget()
        self.layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Cabeçalho
        titulo = QLabel("Matriz de Eisenhower (Desktop)")
        titulo.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(titulo)

        # Formulário de Adição
        form_layout = QHBoxLayout()
        self.input_texto = QLineEdit()
        self.input_texto.setPlaceholderText("O que precisa ser feito?")
        
        self.combo_quadrante = QComboBox()
        self.combo_quadrante.addItems(["Fazer Agora", "Agendar", "Delegar", "Eliminar"])
        
        btn_adicionar = QPushButton("Adicionar Tarefa")
        btn_adicionar.setStyleSheet("background-color: #3498db; color: white; font-weight: bold; padding: 8px; border-radius: 4px;")
        btn_adicionar.clicked.connect(self.adicionar_tarefa_ui)

        form_layout.addWidget(self.input_texto, stretch=2)
        form_layout.addWidget(self.combo_quadrante, stretch=1)
        form_layout.addWidget(btn_adicionar, stretch=1)
        self.layout.addLayout(form_layout)

        # Grid de Listas (Os 4 Quadrantes)
        grid_layout = QHBoxLayout()
        
        self.listas = {}
        quadrantes = ["Fazer Agora", "Agendar", "Delegar", "Eliminar"]
        for q in quadrantes:
            v_box = QVBoxLayout()
            lbl = QLabel(q)
            lbl.setStyleSheet("font-weight: bold; color: #34495e; margin-top: 10px;")
            lw = QListWidget()
            v_box.addWidget(lbl)
            v_box.addWidget(lw)
            grid_layout.addLayout(v_box)
            self.listas[q] = lw

        self.layout.addLayout(grid_layout)
        self.carregar_dados()

    def init_db(self):
        self.conn = sqlite3.connect('eisenhower_desktop.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, texto TEXT, quadrante TEXT)')
        self.conn.commit()

    def carregar_dados(self):
        for lw in self.listas.values():
            lw.clear()
        self.cursor.execute('SELECT texto, quadrante FROM tarefas')
        for row in self.cursor.fetchall():
            texto, quadrante = row
            if quadrante in self.listas:
                self.listas[quadrante].addItem(texto)

    def adicionar_tarefa_ui(self):
        texto = self.input_texto.text().strip()
        quadrante = self.combo_quadrante.currentText()
        if not texto:
            QMessageBox.warning(self, "Aviso", "Digite uma tarefa válida!")
            return

        self.salvar_e_atualizar(texto, quadrante)
        self.input_texto.clear()

        # Envia para o Webhook do Discord (se configurado)
        try:
            if WEBHOOK_URL.startswith("http"):
                requests.post(WEBHOOK_URL, json={"content": f"📌 **Nova Tarefa (App Desktop):**\n> {texto}\n📍 Categoria: *{quadrante}*"}, timeout=3)
        except Exception as e:
            print(f"Erro ao enviar webhook: {e}")

    def salvar_e_atualizar(self, texto, quadrante):
        self.cursor.execute('INSERT INTO tarefas (texto, quadrante) VALUES (?, ?)', (texto, quadrante))
        self.conn.commit()
        if quadrante in self.listas:
            self.listas[quadrante].addItem(texto)

    def adicionar_item_externo(self, texto, quadrante):
        self.salvar_e_atualizar(texto, quadrante)


if __name__ == "__main__":
    # Inicia o servidor Flask em segundo plano
    t = threading.Thread(target=rodar_servidor, daemon=True)
    t.start()

    app = QApplication(sys.argv)
    window = EisenhowerDesktop()
    window.show()
    sys.exit(app.exec_())