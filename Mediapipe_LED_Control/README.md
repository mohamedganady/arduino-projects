# Mediapipe Control 5 LEDs

## Overview
This project demonstrates how to control **5 LEDs** connected to an Arduino board using **hand gestures** detected by **Mediapipe**.  
The Python script uses your webcam to track hand landmarks and sends commands over serial to the Arduino, which then turns LEDs on/off according to the detected gestures.

---

## Features
- Hand gesture detection using **Mediapipe Hands**  
- Real-time control of **5 LEDs** via Arduino  
- Simple serial communication between Python and Arduino  
- Easily extendable to more LEDs or other devices  

---

## Hardware Required
- Arduino board  
- 5 LEDs  
- 5 resistors (220Ω recommended)  
- Jumper wires  
- Breadboard (optional)  
- USB cable to connect Arduino to PC  

---

## Software Required
- Python 3.x  
- Arduino IDE  
- Python packages:  
  ```bash
  pip install mediapipe opencv-python pyserial
