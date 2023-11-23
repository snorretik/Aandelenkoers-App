import tkinter
from PIL import ImageTk, Image

def displayfunction():
    # Create the main window
    window = tkinter.Tk()
    window.title("Plotting the plot!")
    window.geometry("750x500")    
    
    # Load the image
    image = Image.open("plot.png")
    photo = ImageTk.PhotoImage(image)

    # Label widget to display the image
    label = tkinter.Label(window, image=photo)
    label.pack()
    
    window.mainloop()

# Run the application
displayfunction()