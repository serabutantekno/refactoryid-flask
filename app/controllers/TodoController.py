from app import app, db, request
from app.controllers.BaseResponseController import BASE_RESPONSE
from app.models import Todo


class TodoController:


    RESPONSE = BASE_RESPONSE()


    def get_all(self):
        data = Todo.Todo.query.all()
        result = [Todo.Todo.data_to_json(todo) for todo in data]
        return self.RESPONSE.base_response(message="get all todos", data=result)
        

    def get_by_id(self, id):
        try:
            data = Todo.Todo.query.get(id)        
            result = data.data_to_json()
            return self.RESPONSE.base_response(message=f"get todo id = {id}", data=result)
        except Exception as error:
            print(error)
            return {"message": "ID not found"}


    def create(self):
        if request.form:
            try:
                form = request.form.to_dict()
                form["status"] = int(form["status"])
                post = Todo.Todo(**form)
                db.session.add(post)
                db.session.commit()
            except Exception as error:
                print(error)
                return self.RESPONSE.error()
            data = Todo.Todo.data_to_json(post)
            return self.RESPONSE.base_response(message="created", data=form, status_code=201)
