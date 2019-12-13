from flask import Flask, render_template
from flask import request, jsonify
import pymongo
import json
import os

## SETUP DB CONNECTION AND FLASK ##
connection_string = "mongodb+srv://hanien:hanien123@cluster0-eidux.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = pymongo.database.Database(client, "aptiv")
collection = pymongo.collection.Collection(db, "sensorreadings")
app = Flask(__name__)
app.config["MONGODB_HOST"] = client


## ROUTES
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/how-it-works", methods=["GET"])
def how_it_works():
    return render_template("how-it-works.html")

@app.route("/gallery", methods=["GET"])
def gallery():
    team_images_path = os.path.join('static', 'img', 'team-images')
    team_images = os.listdir(team_images_path)
    app.config['UPLOAD_FOLDER'] = team_images
    return render_template("gallery.html", len = len(team_images), images=team_images)

@app.route("/api/sensors", methods=['POST'])
def post_reading():
    data = request.json
    collection.insert_one(
        {'_id':data['_id'], 
        'temperature': data['temperature'],
        'humidity':data['humidity'] ,
        'pressure': data['pressure'],
        'altitude': data['altitude'],
        'gain':data['gain'],
        'lux':data['lux'],
        'luminosity':data['luminosity'], 
        'ir': data['ir'], 
        'full': data['full'] })
    return jsonify(data)

@app.route("/api/sensors/<rpi_id>", methods=['GET'])
def get_id(rpi_id):
    rpi = collection.find_one({'_id' : rpi_id})
    return jsonify(rpi)


@app.route("/api/sensors/<rpi_id>", methods=['PUT'])
def update_reading(rpi_id):
    data = json.loads(request.data)
    temperature = data['temperature']
    humidity = data['humidity']
    pressure = data['pressure']
    altitude = data['altitude']
    gain = data['gain']
    lux = data['lux']
    ir = data['ir']
    full = data['full']
    found_reading = collection.find_one_and_update(
        {'_id': rpi_id}, {'$set': {'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'altitude': altitude,
        'gain': gain,
        'lux': lux,
        'ir': ir,
        'full': full 
        }})
    return jsonify(found_reading)


## START FLASK
if __name__ == "__main__":
    app.debug = True
    app.run()
