from app import app, request
from app.controllers.TodoController import TodoController


todo = TodoController()


@app.route("/todo", methods=["GET", "POST"])
def todo_route():
    if request.method == "GET":
        return todo.get_all()
    elif request.method == "POST":
        return todo.create()


@app.route("/todo/<int:id>", methods=["GET"])
def todo_route_id(id):
    if request.method == "GET":
        return todo.get_by_id(id)


@app.route("/todo/query")
def todo_user():
    return todo.get_by_user()


@app.route("/todo/<int:id>/status")
def todo_status(id):
    return todo.update_status(id)
