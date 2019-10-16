var todoList = {
	
	todos : [],

	// displayTodos : function() {										//for displaying in console
	// 	if (this.todos.length === 0) {
	// 		console.log('Your todo list is empty!')
	// 	}
	// 	else {
	// 		console.log('My todos :');
	// 		for (var i = 0; i < this.todos.length; i++) {
	// 			if (this.todos[i].completed === true) {
	// 				console.log('(x) ',this.todos[i].todoText);
	// 			}
	// 			else {
	// 				console.log('( ) ',this.todos[i].todoText);
	// 			}
	// 		}
	// 	}
	// },
	
	addTodos : function(todoText) {
		this.todos.push({
			todoText : todoText,
			completed : false
		});
	},
	
	changeTodos : function(position,todoText) {
		var todo = this.todos[position];
		todo.todoText = todoText;
	},
	
	deleteTodos : function (position) {
		this.todos.splice(position,1);
	},

	toggleCompleted : function (position) {
		var todo = this.todos[position];
		todo.completed = !todo.completed;
	},

	toggleAll : function () {
		var totalTodos = this.todos.length;
		var completedTodos = 0;

		//get number of completed todos
		this.todos.forEach( function (todo) {
			if (todo.completed === true) {
				completedTodos++;
			}
		});

		//if everything is true make everything false
		if (completedTodos === totalTodos) {
			this.todos.forEach( function (todo) {
				todo.completed = false;
			});
		}
		//otherwise make all true
		else {
			this.todos.forEach( function (todo) {
				todo.completed = true;
			});
		}

		//toggleAll should simply toggle the truth value for the completed flag instead of setting the same value for each todo 
		//use the following code if this is the required functionality as per your use case
		// this.todos.forEach(todo=>{
		// 	todo.completed=!todo.completed;
		// })
		
	}
};

var handler = {
	size : 0,
	addTodos : function() {
		var todoAddTextInput = document.getElementById('todoAddTextInput');
		if (todoAddTextInput.value === '') {
			this.emptyHandler("Add");
		}
		else {
			todoList.addTodos(todoAddTextInput.value);
			todoAddTextInput.value = '';
			this.size++;
			view.displayTodos();
		}
	},

	changeTodos : function() {
		var todoChangePositionInput = document.getElementById('todoChangePositionInput');
		var todoChangeNameInput = document.getElementById('todoChangeNameInput');
		var inputValue = todoChangePositionInput.valueAsNumber;
		var hasDuplicate = todoList.todos.some(todo =>
			todo.todoText === todoChangeNameInput.value
		)

		if (hasDuplicate) {
			this.duplicateHanlder(todoChangeNameInput.value)
		} else if (
			todoChangePositionInput.value === '' ||
			todoChangeNameInput.value === ''
		) {
			this.emptyHandler("Change");
		} else if (inputValue >= this.size || inputValue < 0) {
			this.indexHandler(this.size);
		} else {
			todoList.changeTodos(inputValue,todoChangeNameInput.value);
			todoChangePositionInput.value = '';
			todoChangeNameInput.value = '';
			view.displayTodos();
		}
	},

	deleteTodos : function() {
		var todoDeletePositionInput = document.getElementById('todoDeletePositionInput');
		var inputValue = todoDeletePositionInput.valueAsNumber;
		if (todoDeletePositionInput.value === '') {
			this.emptyHandler("Delete");
		}
		else if (inputValue >= this.size || inputValue < 0) {
			this.indexHandler(this.size);
		}
		else {
			todoList.deleteTodos(inputValue);
			todoDeletePositionInput.value = '';
			this.size--;
			view.displayTodos();
		}
	},

	advanceDeleteTodos : function(position) {
		todoList.deleteTodos(position);
		this.size--;
		view.displayTodos();
	},

	toggleCompleted : function() {
		var todoTogglePositionInput = document.getElementById('todoTogglePositionInput');
		var inputValue = todoTogglePositionInput.valueAsNumber;
		if (todoTogglePositionInput.value === '' ) {
			this.emptyHandler("Toggle");
		}
		else  if (inputValue >= this.size || inputValue < 0) {
			this.indexHandler(this.size);
		}
		else 
		{
			todoList.toggleCompleted(todoTogglePositionInput.valueAsNumber);
			todoTogglePositionInput.value = '';
			view.displayTodos();
		}
	},

	advanceToggleCompleted : function(position) {
		todoList.toggleCompleted(position);
		view.displayTodos();
	},
	
	toggleAll : function() {
		todoList.toggleAll();
		view.displayTodos();
	},

	emptyHandler : function(method) {
		window.alert(`Enter some value in the input field to ${method} an Item!`);
	},

	duplicateHanlder : function(value) {
		window.alert(
			'"' + value + '" already exists from the open tasks.\n' +
			'Try to use another name.'
		);
	},

	indexHandler : function (s) {
		window.alert("Index out of size!\n" + s + " is the maximum size!!");
	}
};

let enterHandler = function(keyCode, functionToCall, parameters){
	if(keyCode === 'Enter'){
		//Need to bind handler for the 'this' error
		functionToCall = functionToCall.bind(handler);
		functionToCall(...parameters);
	}
};

//Enter event handler for add input
let todoAddTextInput = document.getElementById('todoAddTextInput');

todoAddTextInput.addEventListener("keypress", function(e){
	enterHandler(e.key, handler.addTodos, []);
});

let todoChangePositionHandler = function(e){
	enterHandler(e.key, handler.changeTodos, []);
};

//Enter event handler for change inputs
let todoChangeNameInput = document.getElementById('todoChangeNameInput');

todoChangeNameInput.addEventListener("keypress", todoChangePositionHandler);

//Enter event handler for delete input
let todoDeletePositionInput = document.getElementById('todoDeletePositionInput');

todoDeletePositionInput.addEventListener("keypress", function(e){
	enterHandler(e.key, handler.deleteTodos, []);
});

//Enter event handler for toggle input
let todoTogglePositionInput = document.getElementById('todoTogglePositionInput');
todoTogglePositionInput.addEventListener("keypress", function(e){
	enterHandler(e.key, handler.toggleCompleted, []);
});



// var myButton = document.getElementById('myButton');

// myButton.addEventListener('click',function() {
// 	var todoTextInput = document.getElementById('todoTextInput');
// 	console.log(todoTextInput.value);
// });


var view = {
	displayTodos : function() {
		var todosUl = document.querySelector('ul');

		todosUl.innerHTML = '';
		todoList.todos.forEach(function (todo,position) {
			var todoLi = document.createElement('li');
			
			todoLi.id = position;
			todoLi.addEventListener('mousedown', 
				event => view.toggleTodoCompleted(event, position)
			);
			todoLi.appendChild(this.createTodoTemplate(todo));
			todoLi.appendChild(this.createDeleteButton());
			todosUl.appendChild(todoLi);
		}, this);
	},

	createDeleteButton : function() {
		var deleteButton =  document.createElement('button');
		deleteButton.textContent = 'Delete';
		deleteButton.className = 'advanceDeleteButton danger';
		deleteButton.onclick = function() {
			var position = this.parentNode.id;     //this->deleteButton
			//console.log(this.parentNode)
			handler.advanceDeleteTodos(position);
		}
		return deleteButton;
	},

	createTodoTemplate : function({completed, todoText}) {
		var todoLabel = document.createElement('label');
		var todoInput = document.createElement('input');
		var todoSpan = document.createElement('span');
		var todoContent = document.createElement('span');
		
		todoInput.setAttribute('type', 'checkbox');
		todoSpan.classList.add('todo-checkmark');
		todoContent.textContent = todoText;

		todoLabel.appendChild(todoInput);
		todoLabel.appendChild(todoContent);
		todoLabel.appendChild(todoSpan);

		if (completed) {
			todoInput.setAttribute('checked', completed);
			todoContent.classList.add('todo-completed');
		}

		return todoLabel;
	},

	toggleTodoCompleted : function(event, position) {
		if (event.target.className.indexOf('advanceDeleteButton') < 0) {
			handler.advanceToggleCompleted(position);
		}
	}
};
