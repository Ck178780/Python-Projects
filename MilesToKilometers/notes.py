import tkinter

window = tkinter.Tk()
window.title("My first GUI program") # Set a title
window.minsize(width=500, height=300)

# Creating a label:
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack() # Use the packer to pack the label on the screen.

# Keep the window on the screen:
window.mainloop() # This line of code should always be at the end of the program