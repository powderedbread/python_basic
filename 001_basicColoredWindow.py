#gui tools
import tkinter as tk 

root = tk.Tk()  #initializes the main window
root.title("Basic Colored Window")

# Set the size of the window
root.geometry("500x500")
root.configure(bg="orange")

# Start the main event loop
root.mainloop()
