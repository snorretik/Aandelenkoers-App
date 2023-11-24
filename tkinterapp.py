import pandas
import matplotlib.pyplot as plt
from createplot import mergingData
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
# from PIL import ImageTk, Image

window = Tk()
window.title("Plotting the plot!")
window.geometry("750x600") 

def displayplot():
    # importing DataFrame
    df = mergingData()

    # creating plotconditions
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Close_x'])
    ax.plot(df['Date'], df['Close_y'])

    # create element with which to display plot in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side="top")

    # create a toolbar to go with the plot
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

def setbutton():
    button = Button(window, width=10, height=2, text='plot', command=displayplot)
    button.pack(side="bottom")

# Add button to screen
setbutton()

# Run the application
window.mainloop()