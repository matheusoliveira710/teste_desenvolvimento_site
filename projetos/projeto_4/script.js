// Carrega tarefas salvas ou inicia array vazio
let tasks = JSON.parse(localStorage.getItem('eisenhower_tasks')) || [];

function renderTasks() {
    // Limpa as listas visuais
    document.getElementById('list-q1').innerHTML = '';
    document.getElementById('list-q2').innerHTML = '';
    document.getElementById('list-q3').innerHTML = '';
    document.getElementById('list-q4').innerHTML = '';

    // Popula os quadrantes
    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.className = 'task-item';
        li.innerHTML = `
            <span>${task.text}</span>
            <button onclick="deleteTask(${index})">✕</button>
        `;
        document.getElementById(`list-${task.quadrant}`).appendChild(li);
    });

    // Salva no navegador
    localStorage.setItem('eisenhower_tasks', JSON.stringify(tasks));
}

function addTask() {
    const input = document.getElementById('taskInput');
    const select = document.getElementById('quadrantSelect');
    const text = input.value.trim();

    if (text === '') {
        alert('Digite uma descrição para a tarefa!');
        return;
    }

    tasks.push({
        text: text,
        quadrant: select.value
    });

    input.value = '';
    input.focus();
    renderTasks();
}

function deleteTask(index) {
    tasks.splice(index, 1);
    renderTasks();
}

// Renderiza ao carregar a página
renderTasks();