from datetime import datetime
from threading import Timer
import RPi.GPIO as GPIO
import time

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

relay=12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)

secs=delta_t.seconds+1

def toggle_relay():
    GPIO.output(relay, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(relay, GPIO.LOW)

GPIO.cleanup()

t = Timer(secs, toggle_relay)
t.start()