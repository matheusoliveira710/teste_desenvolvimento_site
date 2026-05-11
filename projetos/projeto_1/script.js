function criarTarefa(){
    let nomeTarefa = prompt("Digite o nome da tarefa: ");
    let prioridade = prompt("Digite a prioridade: alta, média ou baixa ")
    let prazoTarefa = prompt("Digite o prazo da tarefa: ")
    let classePrioridade = ""
    if (prioridade === "alta") {
        classePrioridade = "alta";
    } else if (prioridade === "média") {
        classePrioridade = "media";
    }
    else {
        classePrioridade = "baixa";
    }

    if (nomeTarefa === null || nomeTarefa === "") {
        return
    }
    let card = document.createElement("div");
    card.classList.add("card", classePrioridade);
    card.innerHTML = 
    
    `<h3>${nomeTarefa}</h3>
    <p>📅 ${prazoTarefa}</p>
    <p>🔥 ${prioridade}</p>
        <button onclick="editarTarefa(this)">
            Editar
        </button>

        <button onclick="excluirTarefa(this)">
            Excluir
        </button>
        <button onclick="voltarTarefa(this)">
            ⬅ Voltar
        </button>
        <button onclick="moverTarefa(this)">
            ➡ Mover
        </button>    
    `
    
    document.getElementById("a-fazer").appendChild(card);
}

function editarTarefa(botao){
    let card = botao.parentElement;
    
    let titulo = card.querySelector("h3");

    let novoNome = prompt("Editar tarefa: ", titulo.textContent);

    if (novoNome === null || novoNome === "") {
        return
    }

    titulo.textContent = novoNome;
}

function excluirTarefa(botao){
    botao.parentElement.remove();
}

function moverTarefa(botao) {

    let card = botao.parentElement;

    let colunaAtual = card.parentElement.id;

    if (colunaAtual === "a-fazer") {

        document
            .getElementById("em-andamento")
            .appendChild(card);

    } else if (colunaAtual === "em-andamento") {

        document
            .getElementById("concluido")
            .appendChild(card);
    }
}

function voltarTarefa(botao) {
    let card = botao.parentElement;
    let colunaAtual = card.parentElement.id;
    if (colunaAtual === "em-andamento") {
        document.getElementById("a-fazer").appendChild(card);
    } else if (colunaAtual === "concluido") {
        document.getElementById("em-andamento").appendChild(card);
    }
}
