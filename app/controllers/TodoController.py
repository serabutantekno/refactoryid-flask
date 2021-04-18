from app.controllers.BaseResponseController import BASE_RESPONSE
from app.models import Todo


class TodoController:


    RESPONSE = BASE_RESPONSE()


    def get_all(self):
        data = Todo.Todo.query.all()
        result = [Todo.Todo.data_to_json(todo) for todo in data]
        return self.RESPONSE.base_response(message="get all todos", data=result)
