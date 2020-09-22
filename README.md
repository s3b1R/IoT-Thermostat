# IoT-Thermostat
Turning on and off a myStrom WiFi Switch, depending on the measured Temperatur with a DS18B20 temperature sensor on a Raspberry Pi

---

## Hardware setup

Connect your Sensor onto your Raspberry Pi like in the scheme below:

![how to connect sensor](/pic4readme/RPI-GPIO.jpg)

---

## Enable 1-Wire on the Raspberry Pi

Since the DS18B20 Sensor uses 1-wire, you have to enable 1-Wire on your Raspberry Pi.  
Open the needed config.txt file with:  
`sudo nano /boot/config.txt`  
  
Add this line at the bottom of the file:  
`dtoverlay=w1-gpio`  
Save the file and reboot your Raspberry.

---

## Find the sensor ID

Find your sensors unique address in the 1-wire directory:  
`ls -l /sys/bus/w1/devices`  

The sensor ID should look like example 28-00000c8aa780  
Note this ID and insert it in thermometer.py in line 15 into the path instead of 28-00000c8aa780  

---

## Find WiFi Switch IP Adress

Pair your myStrom WiFi Switch with your WLAN. Nevertless to say, it hast to be the same network as the Raspberry Pi is in it.  
Find the IP adress of your WiFi Switch in the network. You can do it in your router interface, or use the `arp -a ` command on your Raspberry Pi.  
  
Note the IP adress and insert it in thermometer.py in line 8 and 9 into the path instead of the IP adress there.  

---

## Run the script

Now you're ready to run the script. You have to run it as sudo. Be sure, you're in the directory where the thermometer.py file is located and type  
'sudo python thermometer.py'  

## Run the script on startup

If you want to run the script automatically when your Raspberry Pi ist starting up, you can use a crontab for it.  


