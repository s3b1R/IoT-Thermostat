import time
import urllib
import threading
from flask import Flask, render_template, jsonify, request

minTemp = None
actTemp = None
urlOn = "http://192.168.43.103/relay?state=1"
urlOff = "http://192.168.43.103/relay?state=0"


def temp_monitor():
    while 1:
        # Open the file for the sensor and read contents
        tempfile = open("/sys/bus/w1/devices/28-00000c8aa780/w1_slave")
        thetext = tempfile.read()
        tempfile.close()
        # Get the temperature
        tempdata = thetext.split("\n")[1].split(" ")[9]
        temperature = float(tempdata[2:])
        temperature = temperature / 1000
        # set actual temperatur for use in main thread
        global actTemp
        actTemp = temperature
        # Switching my plug
        global minTemp
        if temperature < minTemp:
            urllib.urlopen(urlOn)
        else:
            urllib.urlopen(urlOff)

        time.sleep(1)

t = threading.Thread(target=temp_monitor)
t.daemon = True
t.start()


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/update")
def update():
    templateData = {'data' : actTemp}
    return jsonify(templateData), 200

@app.route("/set_temp")
def set_temp():
    wishTemp = request.args.get("temp")
    global minTemp
    minTemp = int(wishTemp)
    templateData = {"data": minTemp}
    return jsonify(templateData), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
