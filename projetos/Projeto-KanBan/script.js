let tarefas = [];
let tarefasSalvas = localStorage.getItem("tarefas");
if (tarefasSalvas) {
    tarefas = JSON.parse(tarefasSalvas);
    console.log(tarefas);
    tarefas.forEach(function(tarefa) {
        criarCard(tarefa);
    });
    atualizarContadores();
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

    card.dataset.id = tarefa.id;

    card.classList.add("card", classePrioridade);

    card.innerHTML = `
    
        <h3>${tarefa.nome}</h3>

        <p>📅 ${tarefa.prazo}</p>

        <div class="data-hora">
        
            <p>🕒 ${tarefa.hora}</p>

            <p>🔥 ${tarefa.prioridade}</p>
        
        </div>

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

function atualizarContadores() {
    
    let fazer = document.querySelectorAll("#a-fazer .card").length;
    
    let andamento = document.querySelectorAll("#em-andamento .card").length;
    
    let concluido = document.querySelectorAll("#concluido .card").length;
    
    document.getElementById("titulo-a-fazer").textContent = `A Fazer (${fazer})`;
    
    document.getElementById("titulo-em-andamento").textContent = `Em andamento (${andamento})`;
    
    document.getElementById("titulo-concluido").textContent = `Concluído (${concluido})`;
}

function criarTarefa(){

    let nomeTarefa =
        document.getElementById("nome").value;

    let prioridade =
        document.getElementById("prioridade").value;

    let prazoTarefa =
        document.getElementById("prazo").value;

    let horaTarefa =
        document.getElementById("hora").value;

    if (nomeTarefa === "") {
        return;
    }

    let tarefa = {

        id: Date.now(),

        nome: nomeTarefa,

        prioridade: prioridade,

        prazo: prazoTarefa,

        hora: horaTarefa,

        status: "a-fazer"
    };

    tarefas.push(tarefa);

    localStorage.setItem(
        "tarefas",
        JSON.stringify(tarefas)
    );

    console.log(tarefas);

    criarCard(tarefa);

    atualizarContadores();

    document.getElementById("nome").value = "";

    document.getElementById("prazo").value = "";

    document.getElementById("hora").value = "";

    document.getElementById("prioridade").value = "alta";
}

function editarTarefa(botao){
    let card = botao.parentElement;
    
    let id = Number(card.dataset.id);

    let tarefa = tarefas.find(function(t) {
        return t.id === id;
    });

    let novoNome = prompt("Editar tarefa: ", tarefa.nome);

    if (novoNome === null || novoNome === "") {
        return
    }

    tarefa.nome = novoNome;
    card.querySelector("h3").textContent = novoNome;
    localStorage.setItem(
        "tarefas",
        JSON.stringify(tarefas)
    );
}

function excluirTarefa(botao){

    let confirmar = confirm(
    "Deseja excluir essa tarefa?"
    );

    if (!confirmar) {
        return;
    }

    let card = botao.parentElement;
    let id = Number(card.dataset.id);
    tarefas = tarefas.filter(function(tarefa) {
        return tarefa.id !== id;
    });
    localStorage.setItem(
        "tarefas",
        JSON.stringify(tarefas)
    );
    card.remove();
    atualizarContadores();
}

function moverTarefa(botao) {
    let card = botao.parentElement;
    let colunaAtual = card.parentElement.id;
    let id = Number(card.dataset.id);
    let tarefa = tarefas.find(function(t) {
        return t.id === id;
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
    atualizarContadores();
}

function voltarTarefa(botao) {

    let card = botao.parentElement;

    let colunaAtual = card.parentElement.id;

    let id = Number(card.dataset.id);

    let tarefa = tarefas.find(function(t) {

        return t.id === id;
    });

    if (colunaAtual === "em-andamento") {

        tarefa.status = "a-fazer";

        document
            .getElementById("a-fazer")
            .appendChild(card);

    } else if (colunaAtual === "concluido") {

        tarefa.status = "em-andamento";

        document
            .getElementById("em-andamento")
            .appendChild(card);
    }

    localStorage.setItem(
        "tarefas",
        JSON.stringify(tarefas)
    );
    atualizarContadores();
}

function pesquisarTarefa() {
    let textoPesquisa = document.getElementById("pesquisa").value.toLowerCase();
    let cards = document.querySelectorAll(".card");
    cards.forEach(function(card) {
        let nomeTarefa = card.querySelector("h3").textContent.toLowerCase();
        if (nomeTarefa.includes(textoPesquisa)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}