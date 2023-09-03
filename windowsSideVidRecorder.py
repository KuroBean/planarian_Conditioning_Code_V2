import cv2
import numpy as np

# Define the video capture device (0 for default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

height=720
width=1280
cap.set(3,width)
cap.set(4,height)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width,height))
# Define the recording duration in seconds
record_duration = 5  # Adjust this as needed

# Start recording
start_time = cv2.getTickCount()
while True:
    ret, frame = cap.read()
    print(ret)
    if not ret:
        break
    cv2.imshow('Camera Feed', frame)
    cv2.waitKey(1)
    # Write the frame to the output video
    out.write(frame)

    # Check if the recording duration has been reached
    current_time = cv2.getTickCount()
    elapsed_time = (current_time - start_time) / cv2.getTickFrequency()
    if elapsed_time >= record_duration:
        break

# Release video capture and writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()



# import serial
# import cv2
# import os
# import time

# # Initialize the recording flag and counter
# is_recording = False
# video_counter = 0
# recordSec = 3  # Set the recording duration in seconds

# # Function to start recording
# def start_recording():
#     global is_recording, video_counter
#     is_recording = True
    
#     # Increment the video counter
#     video_counter += 1

#     # Initialize the camera
#     cap = cv2.VideoCapture(0)
    
#     # Define the codec and create a VideoWriter object for MP4
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    
#     print("Recording started...")
    
   
#     ret, frame = cap.read()
#     out.write(frame)
#     cv2.imshow('Recording', frame)
    
#     time.sleep(recordSec)
#     stop_recording()
    
#     # Release the camera and video writer
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#     print("Recording stopped.")

# # Function to stop recording
# def stop_recording():
#     global is_recording
#     is_recording = False
#     cv2.destroyAllWindows()
#     print("Recording stopped.")

# # Open the serial port connection to the Arduino
# ser = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate

# while True:
#     # Read data from Arduino
#     data = ser.readline().decode().strip()
#     print(f"Received: {data}")
#     # Process the received data
#     if data == "START_RECORDING":
#         start_recording()

# ser.close()
