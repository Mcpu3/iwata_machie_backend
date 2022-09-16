from typing import Optional

from fastapi import FastAPI
import MySQLdb
import uvicorn


app = FastAPI()
connect = MySQLdb.connect(host='db', user='root', password='password', db='test')

@app.get('/')
def read_root():
    return {'hello': 'world'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}

@app.get('/test')
def test():
    cursor = connect.cursor()
    cursor.execute('select * from test')
    fetched = cursor.fetchone()
    hello = fetched[0]
    world = fetched[1]
    cursor.close()
    return {hello: world}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")