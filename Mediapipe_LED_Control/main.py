import cv2
import mediapipe as mp
import serial
import time
arduino = serial.Serial('/dev/tty.usbmodem11301', baudrate=9600)
time.sleep(2)
cap = cv2.VideoCapture(0)
hand_detect = mp.solutions.hands
draw_utils = mp.solutions.drawing_utils
with hand_detect.Hands() as hands:
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hands.process(rgb_frame)
        hand = output.multi_hand_landmarks
        if hand:
           for hand_landmarks in hand:
               draw_utils.draw_landmarks(frame, hand_landmarks, hand_detect.HAND_CONNECTIONS)

           lm = hand_landmarks.landmark
           if lm[3].x > lm[4].x :
               arduino.write("thumb_open\n".encode())
           if lm[3].x < lm[4].x:
               arduino.write("thumb_close\n".encode())
           if lm[8].y < lm[6].y :
               arduino.write("index_open\n".encode())
           if lm[8].y > lm[6].y:
               arduino.write("index_close\n".encode())
           if lm[12].y < lm[10].y :
               arduino.write("middle_open\n".encode())
           if lm[12].y > lm[10].y:
               arduino.write("middle_close\n".encode())
           if lm[16].y < lm[14].y :
               arduino.write("ring_open\n".encode())
           if lm[16].y > lm[14].y:
               arduino.write("ring_close\n".encode())
           if lm[20].y < lm[18].y :
               arduino.write("pinky_open\n".encode())
           if lm[20].y > lm[18].y:
               arduino.write("pinky_close\n".encode())

        cv2.imshow('frame',frame)
        cv2.waitKey(1)