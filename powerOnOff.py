import RPi.GPIO as GPIO
import datetime
import time

# Set GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin you're using
gpio_pin = 2

# Set the GPIO pin as output
GPIO.setup(gpio_pin, GPIO.OUT)

def set_gpio_high():
    GPIO.output(gpio_pin, GPIO.HIGH)
    print(f"GPIO pin {gpio_pin} set to HIGH at {datetime.datetime.now()}")

def set_gpio_low():
    GPIO.output(gpio_pin, GPIO.LOW)
    print(f"GPIO pin {gpio_pin} set to LOW at {datetime.datetime.now()}")

while True:
    now = datetime.datetime.now()
    morning_time = now.replace(hour=7, minute=0, second=0, microsecond=0)
    night_time = now.replace(hour=23, minute=0, second=0, microsecond=0)

    if now >= morning_time and now < night_time:
        set_gpio_high()
    else:
        set_gpio_low()

    # Sleep for a minute to avoid excessive CPU usage
    time.sleep(60)