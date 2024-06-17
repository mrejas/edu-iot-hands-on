# IoT Hands on practice

## Background

These files was made for the practical part of an IoT Education given in Sweden for [TUC Sweden](https://www.tucsweden.se/). The course is a mostly theoretical course and this material is only for the practical part of the course.

The files here are mostly of interest to the students on the course but others might find something interesting as well. It is possible to do this all of you own but then you will of course miss out on the lecturing, anecdotes and bad delivered jokes that was given as well.

## Prerequisites

You will need some things to get started. They are specified in each exercise but to sum it up you will need:

- A Raspberry Pi (Model 3 or 4) with 64-bit Raspberry Pi OS
- A breadboard and som electronical components
  - Some connection cables
  - At least 2 330 Ohm resistors (The value is not that important above 200 and below 400 should work)
  - At least 1 LED
  - At least 2 tactile push buttons
  - A cell phone with IOS or Android (optional only for exercise 3)

  You can get all the components in any basic electronics starter kit.

## The exercises

In the exercises we will step by step build an IoT application including hardware, software and using the platform IoT Open to connect it all together.

### First exercise (orientation and getting started)

In this exercise we will control a LED on our breadboard using commands from an application connected to IoT Open. This is exactly how a switch or any on/off actuator works.

[Read the first exercise](/exercises/exercise-1.md)  
[Graphical overview](https://github.com/mrejas/edu-iot-hands-on/raw/main/images/exercise-1-board.webp)

### Second exercise (locally vs cloud)

This is a continuation of the first exercise. In this exercise we will add two buttons to the breadboard and use them to send a signal to the IoT Platform. The signal will then be used to control the LED from the first exercise. We will control the LED both Locally and via the IoT Open platform. This exercise also emphases the pros and cons with central (cloud) and edge (local) processing.

[Read the second exercise](/exercises/exercise-2.md)  
[Graphical overview](https://github.com/mrejas/edu-iot-hands-on/raw/main/images/exercise-2-board.webp)

### Third exercise (expand the boundaries)

Let's add another thing into the equation. Our phone will now be a sensor. And depending on the orientation of your phone, i.e. if the screen is phasing up or down, the LED will be lit.

[Read the third exercise](/exercises/exercise-3.md)  
[Graphical overview](https://github.com/mrejas/edu-iot-hands-on/raw/main/images/exercise-3-board.webp)

### Fourth exercise

 We will use an internal sensor of the Raspberry Pi and use different ways to trigger measurements.

[Read the fourth exercise](/exercises/exercise-4.md)

### Fifth exercise

Here we will use a photoresistor as input

[Read the fifth exercise](/exercises/exercise-5.md)

### Sixth exercise

This is the final exercise. It is probably only useful for my students in Helsingborg since it is a group effort and I assume that most reading this text works alone. But hey, I might be wrong of course :-).

[Read the sixth exercise](/exercises/exercise-6.md)