import serial

# Replace 'COM3' with the actual COM port your Arduino is connected to
ser = serial.Serial('COM3', 9600)

# Create or open the 'SerialLogs.txt' file in append mode
with open('SerialLogs.txt', 'a') as log_file:
    while True:
        try:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            # Write the line to the log file
            log_file.write(line + '\n')
            log_file.flush()  # Flush the buffer to ensure data is written immediately
            
            # Print the received data to the console
            print(line)
        
        except KeyboardInterrupt:
            print("Logging stopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}")

# Close the serial port
ser.close()
