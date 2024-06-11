import sqlite3
from fastapi import FastAPI
from model import Item

app = FastAPI()

@app.get('/')
async def root():
    return {'message': "Hellow World!"}

@app.get('/tasks/')
async def tasks():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Tasks')
    tasks = cursor.fetchall()
    print(tasks)
    connection.commit()
    connection.close()
    ret = {}
    for task in tasks:
        ret[task[0]] = task
    return ret

@app.get('/tasks/{id}')
async def tasks_id(id: int):
    
    return {'id': id}

@app.post('/tasks/')
async def item_post(item: Item):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Tasks (name, description, status) VALUES (?, ?, ?)', (item.name, item.description, item.status))
    connection.commit()
    connection.close()
    return {'item': item}

@app.put('/tasks/{id}')
async def item_put(id: int, item: Item):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (item.status, id))
    connection.commit()
    connection.close()
    return {'item': item,
            'id': id}

@app.delete('/tasks/{id}')
async def item_del(id: int):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Tasks WHERE id = ?', (id,))
    connection.commit()
    connection.close()
    return {'id': id}