from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    todo_item_name = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


db.create_all()


@app.get("/")
def home():
    # query list of todo items on db
    todo_list = db.session.query(Todo).all()
    # return todo items
    return render_template("base.html", todo_list=todo_list)


@app.post("/add")
def add():
    todo_item = request.form.get("todo_item")
    new_todo = Todo(todo_item_name=todo_item, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.get("/update/<int:todo_id>")
def update(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
