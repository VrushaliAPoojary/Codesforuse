from pynput.mouse import Button, Controller
import time

# Create mouse controller
mouse = Controller()

# Set a delay before the auto-clicker starts
time.sleep(3)

# Define the number of clicks
# num_clicks = 1000

# Perform the clicks
for i in range(2000):
    mouse.click(Button.left)  # Clicks the left mouse button
    time.sleep(0.1)           # Small delay between clicks

    print("Auto-clicking finished.")