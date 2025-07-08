from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Task {self.title}>"


with app.app_context():
    db.create_all()


@app.route('/add/<title>')
def add_task(title):
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return f"Task '{title}' added!"


@app.route('/tasks')
def read_tasks():
    tasks = Task.query.all()
    return {task.id: {"title": task.title, "completed": task.completed} for task in tasks}


@app.route('/update/<int:id>/<new_title>')
def update_task(id, new_title):
    task = Task.query.get_or_404(id)
    task.title = new_title
    db.session.commit()
    return f"Task{id} updated to '{new_title}'!"


@app.route('/remove/<title>')
def remove_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return f"Task {id} removed!"


if __name__ == "__main__":
    app.run(debug=True)
