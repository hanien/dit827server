from flask import Flask
from flask import request, jsonify
import pymongo

## SETUP DB CONNECTION AND FLASK ##
connection_string = "mongodb+srv://hanien:hanien123@cluster0-eidux.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = pymongo.database.Database(client, "aptiv")
collection = pymongo.collection.Collection(db, "sensorreadings")
app = Flask(__name__)
app.config["MONGODB_HOST"] = client

## ROUTES
@app.route("/", methods = ['POST'])
def post_reading():
    data = request.json
    collection.insert_one({'type': data['type'], 'value': data['value']})
    return jsonify(data)

@app.route("/<reading_type>", methods = ['GET'])
def get_reading(reading_type):
    found_reading = collection.find_one({'type': reading_type})
    return found_reading['value']

@app.route("/<reading_type>", methods = ['PATCH'])
def update_reading(reading_type):
    data = request.json
    found_reading = collection.find_one_and_update({'type': reading_type}, {'$set': {'value': data['value']}})
    return found_reading['value']

## START FLASK
if __name__ == "__main__":
    app.run()