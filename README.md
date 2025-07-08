# SQLAlchemy_tutorial
Туториал по работе с SQLAlchemy в Flask
Что такое SQLAlchemy?

SQLAlchemy – это ORM (Object Relational Mapper)

ORM позволяет работать с базами данных как с объектами Python, а не писать SQL-запросы вручную.
 
Пример: ❌ Без ORM (обычный SQL-запрос в Python):

cursor.execute("INSERT INTO tasks (title) VALUES ('Buy milk')")
✅ С ORM (SQLAlchemy):

new_task = Task(title="Buy milk")
db.session.add(new_task)
db.session.commit()
