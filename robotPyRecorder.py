import serial
import pyautogui

# Initialize the recording flag
is_recording = False
pyautogui.moveTo(2510,480)
# Function to start recording
def start_recording():
    global is_recording
    is_recording = True
    
    pyautogui.click()
    while is_recording:
        data = ser.readline().decode().strip()
        if data == "STOP_RECORDING":
            is_recording=False
        # Break the loop on a key press (e.g., 'q') or if not recording
        if not is_recording:
            break
    

# Function to stop recording
def stop_recording():
    pyautogui.click()

# Open the serial port connection to the Arduino
ser = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate

while True:
    # Read data from Arduino
    data = ser.readline().decode().strip()
    print("running")
    # Process the received data
    if data == "START_RECORDING":
        start_recording()
    elif data == "STOP_RECORDING":
        stop_recording()

ser.close()
