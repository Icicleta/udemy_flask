from flask import Flask, request # importing the flask class
app = Flask(__name__) # creating an instance of the Flask class
import uuid
from db import stores, items
from flask_smorest import abort

@app.post('/store')
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201

@app.get('/store') # The primary url for our application
def gets_stores(): # This method returns 'Flask Dockerized', which is displayed in our browser.
    return {"stores": list(stores.values())}

@app.get('/store/<store_id>')
def gets_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(message="Store ID not found.")

@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")

    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id":item_id }
    items[item_id] = new_item
    return new_item, 201
        
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}       

@app.get('/item/<item_id>')
def gets_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item ID not found.")

 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # This statement starts the server on your local machine.