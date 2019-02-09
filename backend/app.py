from flask import Flask, request
import pymongo

app = Flask(__name__)
mongoclient = pymongo.MongoClient('mongodb://admin:password123@ds058508.mlab.com:58508/grocerybuddy')

@app.route('/')
def hello_world():
    return 'Hello, Grocery buddies!'

@app.route('/testdb', methods=['GET', 'POST'])
def use_db():
    names = mongoclient.grocerybuddy.test_names
    if request.method == 'GET':
        name = names.find_one(sort=[('_id', pymongo.DESCENDING)])['name']
        return 'Hello, ' + name + '!\n'
    elif request.method == 'POST':
        new_name = request.args['name']
        names.insert_one({'name': new_name})
        return 'Name saved\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
