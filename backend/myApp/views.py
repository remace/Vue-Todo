# from . import settings
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

import config

# instantiate the app and configure it
app = Flask(__name__)
app.config.from_object('config')


from .models import Todo, db
from .serializers import todos_schema, todo_schema

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/', methods=["GET"])
@app.route('/check/', methods=['GET'])
def ping_pong():
    return jsonify({'ping':'pong'})

# Todo API routes
@app.route('/api/todos/', methods=['GET'])
def get_all_todos():
    todos = Todo.query.all()
    return todos_schema.jsonify(todos)

@app.route('/api/todo/<int:id>/', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get(id)
    return todo_schema.jsonify(todo)


@app.route('/api/todo/create/', methods=['GET','POST'])
def post_todo():
    title = request.json.get("title", ' ')
    description = request.json.get("description", ' ')
    visible = request.json.get('visible', True)
    done = request.json.get('done', True)
    todo = Todo(title = title,
        description = title,
        visible = visible,
        done = done
        )
    db.session.add(todo)
    db.session.commit()
    return todo_schema.jsonify(todo)


@app.route('/api/todo/<int:id>/', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return todo_schema.jsonify(todo)

@app.route('/api/todo/<int:id>/', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get(id)
    todo.update(kwargs=request.json)
    db.session.commit()
    return todo_schema.jsonify(todo)


if __name__ == '__main__':
    app.run(debug=DEBUG)
