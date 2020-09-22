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

The sensor ID should look like example 28-000006780b89
