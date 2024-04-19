# IoT Exercise 1

In this exercise we will control a LED on our breadboard using commands from an application connected to IoT Open. This is exactly how a switch or any on/off actuator works. This will also work as a foundation for the upcoming exercises.

![Overview of the goal for this exercise](../images/exercise-1-overview.png)

## Material

- Raspberry Pi with 64bit operating system
- Breadboard and some connection cables so that you can connect the pins from the Raspberry Pi to your breadboard.
- A LED
- A 330Ω Resistor\*

In [this photo](../images/exercise-1-circuit-photo.jpg) you can see all the components needed.

_\*) 330Ω is not exact, if higher the LED will glow less intence. Newer go under 200Ω since that may damage your Raspberry Pi._

## Preparations

- Install Raspberry Pi OS 64bit on your Raspberry (if you haven't already). Make sure you can log in to it from your laptop.
- You should have an account on IoT Open that you can log into from earlier exercises.

### Sources for more information

- [Raspberry Pi Documentation, Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [IoT Open Platform](https://lynx.iotopen.se)
- [How To Use A Breadboard](https://www.build-electronic-circuits.com/breadboard/)
- [Resistor color code calculator](https://www.calculator.net/resistor-calculator.html)


## Learning goals

- Actuators (Control real things via IoT, unlike sensors that just collects data)
- Communication via MQTT
- IoT Open Edge Client
- How topic\_write and the MQTT-payload format works in IoT Open
- Starting point for following exercises

## Steps to make this happen

### Milestone I (Electronics prototype and verification)

Make the electronics work and the LED to flash.

1. Make sure you can login to your Raspberry Pi and that it is arm64.
1. Make the circuit as in [this image](../images/exercise-1-circuit.png).
1. Test the circuit with these commands
   1. `gpioset gpiochip0 16=1` # The LED should be lit
   1. `gpioset gpiochip0 16=0` # The LED should be dark
   1. Test 3 and 4 over and over.
1. Do not move to the next section until it works and you know why!

[A photo of my circuit](../images/exercise-1-circuit-photo.jpg).

### Milestone II (Software POC)

Since we will use Python in the next milestones let's make sure it works for us to control the LED.

1. Make sure you passed milestone I.
1. Install paho python lib on your RPi: `sudo apt-get install python3-paho-mqtt` 
1. Save [this program](../code/led_flash.py) as "led\_flash.py"
1. Run it like "python python led\_flash.py"
1. The LED should be lit for one half second.
1. Do not move to the next section until it works and you know why!

### Reflection

Ok, where are we?

Now we can control the LED with Python code. That's cool. We could now write local logic to make some cool stuff but only locally on the Raspberry Pi. To connect this to the world and make IoT of it we need to do some more. There are (at least) two ways to do this. We could have the code connect to the platform itself. That would be like a native sensor/actuator where the Raspberry Pi acts as a large device. An other way to do it is to let the Raspberry Pi be an Edge Client and have some capabilities of its own. Here we go the second route an connect the Raspberry Pi as an Edge Client. 

### Milestone III (Establish connection)

1. Make sure your Raspberry Pi have access to the internet (port 443 and 8883 needs to be open from the RPi and out)
1. Please make a backup of important stuff on your RPi if any.
1. Prepare the Edge-client in IoT Open (installation -> Settings -> Edge client Create new credentials) and save the Credentials somewhere.
1. Run the script at https://github.com/mrejas/rpi-edge-client.sh/blob/main/iotopen-lynx-edge-client.sh
1. Verify in IoT Open that the Edge-Client is connected.
1. Do not move to the next section until it works and you know why!

### Milestone IV (Verify MQTT traffic)

1. Make sure you have achieved milestone III
1. Log in to IoT Open
1. Open a console (ssh or terminal) on the Raspberry Pi
1. Navigate to the MQTT-window in IoT Open on your Installation
1. Type the following on the Raspberry Pi `mosquitto_pub -t obj/test -m "Hello World"`
1. In the MQTT-window in IoT Open you should now see `<clientid>/obj/test Hello World`
1. Test is ready, do not move on until it works and you know why!
