const deleteButtons = document.querySelectorAll('.delete-button');

deleteButtons.forEach(button => {
    button.addEventListener('click', event => {
        event.preventDefault();
        const taskId = button.dataset.taskId;
        deleteTask(taskId);
    });
});

document.getElementById('add-task-form').addEventListener('submit', event => {
    event.preventDefault();
    const content = document.getElementById('task-content').value;
    addTask(content);
});

function addTask(content) {
    fetch('/add_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content: content })
    })
    .then(response => {
        if (response.ok) {
             location.reload();
        } else {
            throw new Error('Failed to add task');
        }
    })
    .catch(error => console.error(error));
}

function deleteTask(id) {
    fetch(`/delete_task/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            location.reload();
        } else {
            throw new Error('Failed to delete task');
        }
    })
    .catch(error => console.error(error));
}