const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");
let todos = [];

todoForm.addEventListener("submit", submitAddTodo);

function deleteTodo(event){
    const li = event.target.parentElement;
    li.remove();
    todos = todos.filter((todo) => todo.id !== parseInt(li.id));
    window.localStorage.setItem('todo', JSON.stringify(todos));
}

function paintTodo(newTodo){
    const li = document.createElement('li');
    li.id = newTodo.id;
    const span = document.createElement('span');
    const button = document.createElement('button');
    span.innerText = newTodo.text;
    button.innerText = 'X';
    button.addEventListener("click", deleteTodo);

    li.appendChild(span);
    li.appendChild(button);
    todoList.appendChild(li);
}

function submitAddTodo(event){
    event.preventDefault();
    const content = document.getElementById("content")
    const newTodo = {text: content.value, id: Date.now(), };
    todos.push(newTodo);
    window.localStorage.setItem('todo', JSON.stringify(todos));
    content.value = "";
    paintTodo(newTodo);
}

let currentTodo = JSON.parse(localStorage.getItem('todo'));

if(currentTodo !== null){
    todos = currentTodo;
    todos.forEach(todo => paintTodo(todo));
}