import cv2
import numpy as np
import serial
import time

# Initialize the recording flag and counter
is_recording = False
video_counter = 0
record_duration = 3+0.2  # Set the recording duration in seconds

startLagTime=time.time()

def start_recording():
    global is_recording, video_counter
    is_recording = True
    print("starting recording")
    # Increment the video counter
    video_counter += 1
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

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
 
    output_filename = f'output_{video_counter}.mp4' 
     

    out = cv2.VideoWriter(output_filename, fourcc, 30.0, (width,height))
    # Define the recording duration in seconds

    # Start recording

    start_time = cv2.getTickCount()

    print(time.time()-startLagTime)

    while True:
        ret, frame = cap.read()
        #print(ret)
        if not ret:
            break
        #cv2.imshow('Camera Feed', frame)
        #cv2.waitKey(1)
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
# Open the serial port connection to the Arduino
ser = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate
counter=0
while True:
    counter=counter+1
    print(f"cycle count: {counter}")
    # Read data from Arduino
    data = ser.readline().decode().strip()
    print(f"Received: {data}")
    # Process the received data
    
    if data == "START_RECORDING":
        startLagTime=time.time()
        start_recording()

