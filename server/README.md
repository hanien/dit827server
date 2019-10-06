# Server #
Flask server for Aptiv project currently serving four endpoints.

 - [GET] */*
    Serves the website
 - [POST] */api/sensors/*
    Posts a new sensor reading type to the server
        example body: 
       {
         "temp":{"value":"20"},
         "sound":{"value":"20.3"},
         "light":{"value":"12.6"},
         "humidity":{"value":"65"}
      }
 - [GET] */api/sensors/<reading-type>*
    Gets the current sensor reading value for the sensor type specified in the parameter
 - [PATCH] */api/sensors/<reading-type>*
    Patches the sensor reading value for the sensor type specified in the parameter