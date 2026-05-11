let tarefas = [];
let tarefasSalvas = localStorage.getItem("tarefas");
if (tarefasSalvas) {
    tarefas = JSON.parse(tarefasSalvas);
    console.log(tarefas);
    tarefas.forEach(function(tarefa) {
        criarCard(tarefa);
    });
}

function criarCard(tarefa) {

    let classePrioridade = "";

    if (tarefa.prioridade === "alta") {

        classePrioridade = "alta";

    } else if (tarefa.prioridade === "média") {

        classePrioridade = "media";

    } else {

        classePrioridade = "baixa";
    }

    let card = document.createElement("div");

    card.classList.add("card", classePrioridade);

    card.innerHTML = `
    
        <h3>${tarefa.nome}</h3>

        <p>📅 ${tarefa.prazo}</p>

        <p>🔥 ${tarefa.prioridade}</p>

        <button onclick="moverTarefa(this)">
            ➡ Mover
        </button>

        <button onclick="voltarTarefa(this)">
            ⬅ Voltar
        </button>

        <button onclick="editarTarefa(this)">
            Editar
        </button>

        <button onclick="excluirTarefa(this)">
            Excluir
        </button>
    `;

    document.getElementById(tarefa.status).appendChild(card);
}

function criarTarefa(){

    let nomeTarefa = prompt("Digite o nome da tarefa: ");

    let prioridade = prompt(
        "Digite a prioridade: alta, média ou baixa"
    );

    let prazoTarefa = prompt(
        "Digite o prazo da tarefa: "
    );

    if (nomeTarefa === null || nomeTarefa === "") {

        return;
    }

    let tarefa = {

        nome: nomeTarefa,

        prioridade: prioridade,

        prazo: prazoTarefa,

        status: "a-fazer"
    };

    tarefas.push(tarefa);

    localStorage.setItem(
        "tarefas",
        JSON.stringify(tarefas)
    );

    console.log(tarefas);

    criarCard(tarefa);
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
    let card = botao.parentElement;
    let titulo = card.querySelector("h3").textContent;
    tarefas = tarefas.filter(function(tarefa) {
        return tarefa.nome !== titulo;
    });
    localStorage.setItem(
        "tarefas",
        JSON.stringify(tarefas)
    );
    card.remove();
}

function moverTarefa(botao) {
    let card = botao.parentElement;
    let colunaAtual = card.parentElement.id;
    let titulo = card.querySelector("h3").textContent;
    let tarefa = tarefas.find(function(t) {
        return t.nome === titulo;
    });
    if (colunaAtual === "a-fazer") {
        tarefa.status = "em-andamento";
        document.getElementById("em-andamento").appendChild(card);
    } else if (colunaAtual === "em-andamento") {
        tarefa.status = "concluido";
        document.getElementById("concluido").appendChild(card);
    }
    localStorage.setItem(
        "tarefas",
        JSON.stringify(tarefas)
    );
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
