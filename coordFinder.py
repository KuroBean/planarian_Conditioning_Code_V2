import pyautogui
import time

def print_cursor_coordinates():
  x, y = pyautogui.position()
  print(f"X: {x}, Y: {y}")

try:
  while True:
    print_cursor_coordinates()
    time.sleep(1)
except KeyboardInterrupt:
  print("Exiting...")
