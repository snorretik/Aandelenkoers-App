import tkinter
from PIL import ImageTk, Image

window = tkinter.Tk()
window.title("Plotting the plot!")
window.geometry("750x500") 

def displayplot():
    # Load the image
    global photo
    image = Image.open("plot.png")
    photo = ImageTk.PhotoImage(image)

    # Label widget to display the image
    label = tkinter.Label(window, image=photo)
    
    label.pack(side="top")

def setbutton():
    button = tkinter.Button(window, width=10, height=2, text='plot', command=displayplot)
    button.pack(side="bottom")

# Add button to screen
setbutton()

# Run the application
window.mainloop()