import time
import urllib
import threading
from flask import Flask, render_template, jsonify, request

minimalTemperature = None
actualTemperature = None
turnSwitchOn = "http://192.168.43.103/relay?state=1"
turnSwitchOff = "http://192.168.43.103/relay?state=0"


def temperature_monitor():
    while 1:
        sensorFile = open("/sys/bus/w1/devices/28-00000c8aa780/w1_slave")
        sensorData = sensorFile.read()
        sensorFile.close()

        temperatureData = sensorData.split("\n")[1].split(" ")[9]
        measuredTemperature = float(temperatureData[2:])
        measuredTemperature = measuredTemperature / 1000

        global actualTemperature
        actualTemperature = measuredTemperature

        global minimalTemperature
        if measuredTemperature < minimalTemperature:
            urllib.urlopen(turnSwitchOn)
        else:
            urllib.urlopen(turnSwitchOff)

        time.sleep(1)


t = threading.Thread(target=temperature_monitor)
t.daemon = True
t.start()

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/update")
def update():
    templateData = {'data': actualTemperature}
    return jsonify(templateData), 200


@app.route("/set_temperature")
def set_temp():
    wishTemperature = request.args.get("temperature")
    global minimalTemperature
    minimalTemperature = int(wishTemperature)
    templateData = {"data": minimalTemperature}
    return jsonify(templateData), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
