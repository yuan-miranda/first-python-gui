# My first GUI program using TKinter library in Python

import tkinter

# Initialize the window
window = tkinter.Tk()

# Make a text using tkinter Label
text = tkinter.Label(window, text="Hello, World!", bg="black", fg="white")

# Put the text on the window, "nw" means north-west or top left
text.pack(anchor="nw")

# Set window title (the thing on very top left)
window.title("urmom")

# Set the window size/dimension
window.geometry("256x64")

# Make the window screen black obviously
window.configure(bg="black")

# Run the main program or the window
window.mainloop()