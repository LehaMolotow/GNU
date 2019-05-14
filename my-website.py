from flask import Flask, render_template
import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import threading, time, os, sys
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
led1 = 20  
led2 = 26 
led3 = 12
DHT22_pin = 17

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
@app.route("/")
def main():
   return render_template('main.html')
 
@app.route("/<pin>/<action>")
def action(pin, action):
   temperature = ''
   humidity = ''
   if pin == "pin1" and action == "on":
      GPIO.output(led1, GPIO.HIGH)
   
   if pin == "pin1" and action == "off":
      GPIO.output(led1, GPIO.LOW)
   
   if pin == "pin2" and action == "on":
      GPIO.output(led2, GPIO.LOW)
   
   if pin == "pin2" and action == "off":
      GPIO.output(led2, GPIO.HIGH)
      time.sleep(10)
      GPIO.output(led2, GPIO.LOW)
      time.sleep(15)
      GPIO.output(led2, GPIO.HIGH)
      time.sleep(10)
      GPIO.output(led2, GPIO.LOW)
      time.sleep(2)
      GPIO.output(led2, GPIO.HIGH)
      time.sleep(10)
      GPIO.output(led2, GPIO.LOW)
      time.sleep(2)
      GPIO.output(led2, GPIO.HIGH)
      time.sleep(2)
      GPIO.output(led3, GPIO.LOW)
      time.sleep(30)
      GPIO.output(led3, GPIO.HIGH)
   if pin == "pin3" and action == "on":
      GPIO.output(led3, GPIO.LOW)
      time.sleep(30)
      GPIO.output(led3, GPIO.HIGH)
   if pin == "pin3" and action == "off":
      GPIO.output(led3, GPIO.HIGH)

   if pin == "dhtpin" and action == "get":
      humi, temp = dht.read_retry(dht.DHT11, DHT22_pin)  # Reading humidity and temperature
      humi = '{0:0.1f}' .format(humi)
      temp = '{0:0.1f}' .format(temp)
      temperature = 'Temperature: ' + temp 
      humidity =  'Humidity: ' + humi
   templateData = {
   'temperature' : temperature,
   'humidity' : humidity
   }
   return render_template('main.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
