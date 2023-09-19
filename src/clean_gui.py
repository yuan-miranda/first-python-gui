import tkinter

window = tkinter.Tk()
text = tkinter.Label(window, text="Hello, World!", bg="black", fg="white")

text.pack(anchor="nw")

window.title("urmom")
window.geometry("256x64")
window.configure(bg="black")

window.mainloop()