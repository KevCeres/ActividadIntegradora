const taskList = document.getElementById('taskList');

async function fetchTasks() {
    const response = await fetch('/get_tasks');
    const data = await response.json();
    const tasks = data.tasks;

    taskList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task;
        taskList.appendChild(li);
    });
}

async function addTask() {
    const taskInput = document.getElementById('taskInput');
    const task = taskInput.value.trim();

    if (task) {
        const response = await fetch('/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ task: task }),
        });
        const data = await response.json();
        if (response.ok) {
            fetchTasks();
        } else {
            alert('Error: ' + data.message);
        }
    }
    taskInput.value = '';
}

// Inicializar la lista de tareas al cargar la página
window.onload = fetchTasks;