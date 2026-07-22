import sys
import sqlite3
import shutil
import os
import argparse
import requests
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, QHBoxLayout)
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

# --- CONFIGURAÇÕES ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1519711446445981805/RMb3waFX8JoRFwpgmg32ga5SasqgQsNa7C6J1RcuxU6Ag9Z-fBK2TS_8kl5IxkOPoC70"
LIMITE_ORCAMENTO = 500.0

class DashboardApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_db()
        self.setWindowTitle("Dashboard Financeiro")
        self.setGeometry(100, 100, 600, 700)
        self.setStyleSheet("background-color: #f0f0f0; font-family: Arial;")

        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        # UI: Cabeçalho
        self.label_titulo = QLabel("Novo Gasto:")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_titulo)

        # Inputs
        form_layout = QHBoxLayout()
        self.cat_input = QLineEdit(); self.cat_input.setPlaceholderText("Categoria")
        self.val_input = QLineEdit(); self.val_input.setPlaceholderText("Valor")
        self.btn = QPushButton("Adicionar")
        self.btn.setStyleSheet("background-color: #007BFF; color: white;")
        self.btn.clicked.connect(self.adicionar_item)
        form_layout.addWidget(self.cat_input); form_layout.addWidget(self.val_input); form_layout.addWidget(self.btn)
        self.layout.addLayout(form_layout)

        # Gráfico
        self.series = QPieSeries()
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(self.chart_view)

        # Botão Limpar
        self.btn_limpar = QPushButton("Limpar Dados")
        self.btn_limpar.setStyleSheet("background-color: #dc3545; color: white;")
        self.btn_limpar.clicked.connect(self.limpar_banco)
        self.layout.addWidget(self.btn_limpar)

        self.carregar_dados()

    def init_db(self):
        self.conn = sqlite3.connect('financeiro.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS gastos (categoria TEXT, valor REAL)')
        self.conn.commit()

    def carregar_dados(self):
        self.series.clear()
        self.cursor.execute('SELECT categoria, SUM(valor) FROM gastos GROUP BY categoria')
        rows = self.cursor.fetchall()
        total = sum(r[1] for r in rows)
        for row in rows:
            slice = self.series.append(row[0], row[1])
            # Slice-Click (Interatividade)
            slice.clicked.connect(lambda s=slice, t=total: self.mostrar_detalhes(s, t))

    def mostrar_detalhes(self, slice, total):
        porc = (slice.value() / total) * 100 if total > 0 else 0
        QMessageBox.information(self, "Detalhes", f"Cat: {slice.label()}\nValor: R$ {slice.value():.2f}\nPart: {porc:.1f}%")

    def adicionar_item(self):
        cat, val_raw = self.cat_input.text().strip(), self.val_input.text().replace(',', '.')
        try:
            val = float(val_raw)
            self.cursor.execute('INSERT INTO gastos VALUES (?, ?)', (cat, val))
            self.conn.commit()
            
            # Alerta de Orçamento
            if val > LIMITE_ORCAMENTO:
                QMessageBox.warning(self, "Alerta", "Gasto acima do limite!")
                # Integração Webhook
                requests.post(WEBHOOK_URL, json={"content": f"🚨 Alerta de gasto: R$ {val} em {cat}"})
            
            self.carregar_dados()
        except: QMessageBox.critical(self, "Erro", "Valor inválido!")

    def limpar_banco(self):
        self.cursor.execute('DELETE FROM gastos')
        self.conn.commit()
        self.carregar_dados()

    def closeEvent(self, event):
        # Backup Automático
        if not os.path.exists('backup'): os.makedirs('backup')
        shutil.copy('financeiro.db', f'backup/financeiro_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db')
        event.accept()

# --- MODO CLI HÍBRIDO ---
def modo_cli(cat, val):
    conn = sqlite3.connect('financeiro.db')
    conn.execute('INSERT INTO gastos VALUES (?, ?)', (cat, float(val)))
    conn.commit()
    print(f"Sucesso: {cat} - R$ {val}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--add", nargs=2, metavar=('cat', 'val'), help="Adicionar gasto via terminal")
    args = parser.parse_args()

    if args.add:
        modo_cli(args.add[0], args.add[1])
    else:
        app = QApplication(sys.argv)
        window = DashboardApp()
        window.show()
        sys.exit(app.exec_())
