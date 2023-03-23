# This program prints out the coordinates of the mouse cursor, this can be used to tweak the values
import pyautogui

# Get the current position of the mouse cursor
x, y = pyautogui.position()

# Print the coordinates
print("x-coordinate:", x)
print("y-coordinate:", y)
