import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

last_pressed = {};
last_pressed[14]=0;
last_pressed[15]=0;

def button_callback(gpio):
    now=time.time()
    if now - last_pressed[gpio] < 0.1:
        return


    print("Button was pushed! " + str(gpio))
    last_pressed[gpio] = now

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=button_callback)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(15,GPIO.RISING,callback=button_callback)

print("Press the buttons on you board.")
message = input("Then press enter to quit\n")

GPIO.cleanup()
