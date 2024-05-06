# IoT Exercise 2

Before you do this one, make sure you already have done [IoT Exercise 1](exercise-1.md).

In this exercise we will add two push buttons to the breadboard for turning the LED on and off. If you don't have any buttons you can use only connection wires and short them to simulate a push button.

A graphical view of this exercise is [here](../images/exercise-2-board.webp).

![Overview of this exercise](../images/exercise-2-overview.png)

We will also use the push buttons to control a friends LED.

## Material

- All things from [IoT Exercise 1](exercise-1.md) already on the breadboard and working.
- Two tactile push buttons.
- Some more connection cables.

## Preparations

- Do [IoT Exercise 1](exercise-1.md)

### Sources for more information

- [Pull up resistor](https://en.wikipedia.org/wiki/Pull-up_resistor)

## Learning goals

- Some more electronics
- The concept of "debouncing"
- The concept of "pull up" and "pull down" resistors
- Practice IoT networking
- Difference between local processing and cloud processing.

## Some background

We could easily make a circuit with only electronics to have the buttons control the LED locally. We could still send the `topic_read` information to let the world know about the LED status.

The benefit of local processing like in the example above is that the buttons will control the LED even though the connection to the cloud server is down. In many cases this is a demand.

But, on the other hand, if we instead created a function for the buttons in IoT Open we can use Node RED or some other logic to connect the buttons dynamically to other stuff around the world. That is way more flexible and have advantages.

Both local and cloud processing have pros and cons. None of them is better than the other, there are just different characteristics.


## Steps to make this happen

Make sure you only pass one milestone once it works and you understand why it works.

### Milestone I (Electronics prototype)

Add two push buttons to the board and make the circuit as in [this image](../images/exercise-2-circuit.png). Please note that the buttons have two pairs of connected pins. If the test below doesn't work try rotate the buttons 90 degrees in any direction.

Also note that push buttons have pins that don't suite breadboards so well so make sure they are well attached.

Please be thorough when making the connections. If you visit the physical workshop we will have limited access to debugging tools. Do not move to the next milestone without checking every wire.

### Milestone II (Software POC)

This small program will just test that your electronics are correct and works.

If you get an error message when executing the buttons.py below try these commands an then try again.

```
sudo apt remove python3-rpi.gpio
sudo apt install python3-rpi-lgpio
```

1. Make sure you passed milestone I.
1. Save [this program](../code/buttons.py) as "buttons.py"
1. Run it like "python python buttons.py"
1. You will see a message on the screen every time you press a button.
1. Any key on the keyboard will exit the program.
1. Do not move to the next section until it works and you know why!


### Milestone III (MQTT from the two buttons)

No we will use MQTT to send data from the two push buttons. Here we will use the two buttons as one switch where one is ON the other is OFF. Another possibility is to use only one and make it toggle the LED. That is left as an exercise if you like a programming challenge.

1. Make sure your Raspberry Pi have access to the internet (port 443 and 8883 needs to be open from the RPi and out)
1. Make sure the Edge-client box in your installation in IoT Open is green.
1. Save the code below as button_integration.py
1. Run the code with python button_integration.py
1. Watch the MQTT in IoT Open when clicking you buttons
1. Do not move to the next section until it works and you know why!

Please note that the buttons will only send MQTT as long as the script above is running. If this was a real application we need a way to start the integration whenever the Raspberry Pi boots up. There is a description on how to do this in [exercise 1](./exercise-1.md)

### Milestone IV (Verify MQTT traffic)

Verify that everything works so far.

1. Make sure you have achieved milestone III
1. Log in to IoT Open
1. Open a console (ssh or terminal) on the Raspberry Pi and make sure the script above is running (only one instance)
1. Navigate to the MQTT-window in IoT Open on your Installation.
1. Press your buttons and see the MQTT messages flow. 1 = On and 0 = OFF
1. Test is ready, do not move on until it works and you know why!

### Milestone V (Create a function in IoT Open for your buttons)

In order to connect the buttons to the world we need to create a function for them in IoT Open.

1. Make sure you passed milestone IV
1. Log in to IoT Open and navigate to your installation
1. Navigate to functions and create a new function
1. Call it "MyButtons" or whatever you see fit
1. Give it type "switch"
1. In the meta data section add topic_write with value obj/tuc/button
1. In the log for your new function you should see your button presses
1. Do not move to the next section until it works and you know why!

### Milestone VI (Connect your buttons to the LED via Node-RED)

This is where the magic happens. Now let's create a flow in Node-RED with one `lynx - in` that uses the `topic_read` from our buttons and connect that to a `lynx - out` that uses the `topic_write` on our LED. We can also add two `Inject` nodes sending `number` `1` and `0` to control the LED from Node-RED as well.

![Node-RED](../images/exercise-2-node-red.png)

1. Make sure you have achieved Milestone V
1. Start Node-RED on your Raspberry Pi (or where you have it installed)
1. Make sure both integration_v2.py from the last exercise and button_integration.py is running on your Raspberry Pi. Use two ssh-sessions in two console windows if you are unsure.
1. Now create a flow in Node-RED that connects the function MyButtons with MyLED.
1. Verify that you now can torn your LED on and off with the Buttons.
1. Do not move to the next section until it works and you know why!


### Milestone VII (Control your friends LED from your board via Node-RED)

Now it getting IoT for real!

1. Make sure you have achieved Milestone VI
1. Log in to IoT Open and navigate to your installation
1. Create an API-key for your user give that to your team mate
1. You both create another IoT Open connection in Node-RED using that Key. Se [last exercise](./exercise-1.md) if you don't remember how. Name it "Friends IoT Open" or something so you don't confuse the two connections.
1. Add each others LED to you boards and mote the lines between your buttons and your LED and add a new one between your buttons and your friends LED
1. Now you should be able to control each others LED's

## Reflection

This is kind of fun, isn't it? What we have done is an example og cloud processing (or central processing). Controlling your LED with the buttons on your board will not work unless the Raspberry Pi is connected to IoT Open. That is a drawback and in some cases not acceptable.

The opposite to central- or cloud-processing is local processing and that's where an Edge-client like the Raspberry Pi can come in very handy. For instance your buttons could turn on the LED with just a simple local script on the Raspberry or even only through electronics. That should work all the time.

But why would we need cloud processing then? That it for the flexibility and the possibility to connect the things in the edge to other applications. Like you did when you connected to your friends board. You can also easily change the action of the buttons at any time.

In many cases a combination of cloud and local processing is best. But then we have to take into account what happens when the edge unit is offline.