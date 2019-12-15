# Server #
Flask server for Aptiv project currently serving four endpoints.

 - ```[GET]/``` Serves the website
 - ```[POST]/api/sensors/<rpi_id>``` Posts a new sensor reading type to the server
     * ```<rpi_id>``` can be one of the following ids: ``` driver``` , ``` back``` ,  ``` middle``` , or ``` passenger```.
    * The Body should be in ```JSON``` format.
    *Example body:* 
        ```sh
               {
                 "temperature":{"value":"20"},
                 "pressure":{"value":"20"},
                 "altitude":{"value":"20"},
                 "temperature":{"value":"20"},
                 "sound":{"value":"20.3"},
                 "light":{"value":"12.6"},
                 "humidity":{"value":"65"},
                 "gain":{"value":"20"},
                 "lux":{"value":"20"},
                 "ir":{"value":"20"},
                 "full":{"value":"20"}
              }
        ```
 - ```[GET]/api/sensors/<rpi_id>``` Gets the current sensor reading values for the `Raspberry Pi` specified in the parameter
 - ```[PUT]/api/sensors/<rpi_id>``` Updates the sensor reading values for the `Raspberry Pi` specified in the parameter
___

# How to start the WebServer #

# 1. Requirements

* [Git](https://git-scm.com/) 
* Code Editor (e.g. [PyCharm](https://www.jetbrains.com/pycharm/), [VSCode](https://code.visualstudio.com/),  [Atom](https://atom.io/), etc.)
* [Flask](http://flask.palletsprojects.com/en/1.1.x/) WebApp/WebServer requires [python3](https://www.python.org/download/releases/3.0/) & [pip3](https://pip.pypa.io/en/stable/) to run.
# 2. Cloning the Repository
* With SSH
    ```bash
    git clone git@github.com:hanien/dit827server.git
    ```
* With HTTPS
    ```bash
    git clone https://github.com/hanien/dit827server.git
    ```
# 3. Flask Requirement
Open your Terminal Command Line and type:

* 
    ```sh
     cd dit827server
     ```
    
*
    ```sh
     $ pip install Flask
     ```
[![Flask](https://user-images.githubusercontent.com/33482142/70390201-35cd7680-19c9-11ea-8a9b-106eee4dd195.png)](http://flask.palletsprojects.com/en/1.1.x/)

# 4. Run the ```python``` server:
Open your Terminal Command Line again and type:

*
    ```sh
     python server.py
     ```
* Open your browser and go to the link: http://127.0.0.1:5000/ OR http://localhost:5000/

