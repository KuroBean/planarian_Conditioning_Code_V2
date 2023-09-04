import serial
import pyautogui
import time
# Initialize the recording flag
is_recording = False
duration=3
pyautogui.moveTo(2510,480)
# Function to start recording
def start_recording():
    global is_recording
    is_recording = True
    
    pyautogui.click()
    startTime=time.time()
    while True:
        if time.time()-startTime>=duration+0.5:
            break
    pyautogui.click()
        


# Open the serial port connection to the Arduino
ser = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate

while True:
    # Read data from Arduino
    data = ser.readline().decode().strip()#seems to only have value for every new msg, then when no activity, is waiting for new msg
    print("running")
    # Process the received data
    if data == "START_RECORDING":
        start_recording()


ser.close()
