import serial
import cv2
import os
import time

# Initialize the recording flag and counter
is_recording = False
video_counter = 0
recordSec = 3  # Set the recording duration in seconds

# Function to start recording
def start_recording():
    global is_recording, video_counter
    is_recording = True
    
    # Increment the video counter
    video_counter += 1

    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    # Define the codec and create a VideoWriter object for MP4
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_filename = f'output_{video_counter}.avi'
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))
    
    print("Recording started...")
    
   
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('Recording', frame)
    
    time.sleep(recordSec)
    stop_recording()
    
    # Release the camera and video writer
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Recording stopped.")

# Function to stop recording
def stop_recording():
    global is_recording
    is_recording = False
    cv2.destroyAllWindows()
    print("Recording stopped.")

# Open the serial port connection to the Arduino
ser = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate

while True:
    # Read data from Arduino
    data = ser.readline().decode().strip()
    print(f"Received: {data}")
    # Process the received data
    if data == "START_RECORDING":
        start_recording()

ser.close()
