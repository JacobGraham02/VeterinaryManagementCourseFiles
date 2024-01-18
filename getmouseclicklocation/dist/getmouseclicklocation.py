from pynput.mouse import Listener, Button

# Function called on a mouse click
def on_click(x, y, button, pressed):
    # Check if the left button was pressed
    if pressed and button == Button.left:
        # Print the click coordinates
        print(f'x={x} and y={y}')

# Initialize the Listener to monitor mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()