from flask import Flask, render_template
from flask import request, jsonify
import pymongo

## SETUP DB CONNECTION AND FLASK ##
connection_string = "mongodb+srv://hanien:hanien123@cluster0-eidux.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = pymongo.database.Database(client, "aptiv")
collection = pymongo.collection.Collection(db, "sensorreadings")
app = Flask(__name__, 
            static_folder = "../website",
            template_folder = "../website")
app.config["MONGODB_HOST"] = client

## ROUTES
@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/api/sensors", methods = ['POST'])
def post_reading():
    data = request.json
    collection.insert_one({'type': data['type'], 'value': data['value']})
    return jsonify(data)

@app.route("/api/sensors/<reading_type>", methods = ['GET'])
def get_reading(reading_type):
    found_reading = collection.find_one({'type': reading_type})
    return found_reading['value']

@app.route("/api/sensors/<reading_type>", methods = ['PATCH'])
def update_reading(reading_type):
    data = request.json
    found_reading = collection.find_one_and_update({'type': reading_type}, {'$set': {'value': data['value']}})
    return found_reading['value']

## START FLASK
if __name__ == "__main__":
    app.run()
