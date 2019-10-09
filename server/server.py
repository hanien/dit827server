from flask import Flask, render_template
from flask import request, jsonify
import pymongo

## SETUP DB CONNECTION AND FLASK ##
connection_string = "mongodb+srv://hanien:hanien123@cluster0-eidux.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = pymongo.database.Database(client, "aptiv")
collection = pymongo.collection.Collection(db, "sensorreadings")
app = Flask(__name__, 
            static_folder = "../",
            template_folder = "../")

app.config["MONGODB_HOST"] = client


## ROUTES
@app.route("/", methods = ["GET"])
def index():
    return render_template("mainPage.html")

@app.route("/api/sensors", methods=["GET"])
def get_readings():
    print("GET")
    rpis = collection.find({})
    print(type(rpis))
    res = {}
    for rpi in rpis:
        if rpi["_id"] == "driver":
            res["driver"] = rpi
        elif rpi["_id"] == "passenger":
            res["passenger"] = rpi
        elif rpi["_id"] == "back":
            res["back"] = rpi
        else:
            res["middle"] = rpi
    return res

@app.route("/api/sensors", methods=['POST'])
def post_reading():
    data = request.json
    collection.insert_one(
        {'_id':data['_id'], 
        'temperature': data['temperature'],
        'sound': data['sound'] ,
        'light': data['light'],
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
    return rpi


@app.route("/api/sensors/<rpi_id>", methods=['PUT'])
def update_reading(rpi_id):
    data = request.json
    temperature = data['temperature']
    sound = data['sound']
    light = data['light']
    humidity = data['humidity']
    pressure = data['pressure']
    altitude = data['altitude']
    gain = data['gain']
    lux = data['lux']
    luminosity = data['luminosity']
    ir = data['ir']
    full = data['full']
    found_reading = collection.find_one_and_update(
        {'_id': rpi_id}, {'$set': {'temperature': temperature,
        'sound': sound,
        'light': light,
        'humidity': humidity,
        'pressure': pressure,
        'altitude': altitude,
        'gain': gain,
        'lux': lux,
        'luminosity': luminosity,
        'ir': ir,
        'full': full 
        }})
    return found_reading


## START FLASK
if __name__ == "__main__":
    app.run()
