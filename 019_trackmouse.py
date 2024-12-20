from pynput.mouse import Listener
import time

def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")
    # This will print mouse position even outside the program's window

with Listener(on_move=on_move) as listener:
    listener.join()  # This will keep the listener running in the background
