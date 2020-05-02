import Audio_Functions as audio
from tkinter import *
from tkinter.filedialog import askopenfilename


class ExtensionError(Exception):
    pass


def alert():
    alert = Toplevel()
    alert.title("Error")
    alert.resizable(False,False)
    alert.geometry("220x50+900+400")
    alertLabel = Label(alert, text="Wrong file, use only mp3, wav").pack()
    myButton = Button(alert, text="Close", command=alert.destroy).pack()


def cleanLabel():
    global location_str
    myLabel4 = Label(root, textvariable=location_str)
    myLabel4.grid(row=3, column=1)


def openFile():
    global filename
    global location_str
    filename = askopenfilename()
    if not location_str:
        cleanLabel()
    location_str.set(filename)
    myLabel4 = Label(root, textvariable=location_str)
    myLabel4.grid(row=3, column=1)
    return 0


def genrePred():
    try:
        if not filename.endswith(('.mp3', '.wav')):
            raise ExtensionError
        genre = audio.prediction(filename)
        myLabel5 = Label(root, text="Songs genre is: " + genre)
        myLabel5.grid(row=6, column=1)
    except ExtensionError:
        alert()

# Main window
root = Tk()
root.title("Genre Predictor")
root.resizable(False, False)
root.geometry("400x140+900+400")

location_str = StringVar()
filename = ''

myLabel1 = Label(root, text=" Hello, welcome in Genre Predictor!")
myLabel1.grid(row=1, column=1)
myLabel2 = Label(root,text = "Please pick your songs location:")
myLabel2.grid(row=2, column=1)


browseButton = Button(root, text="Browse", command=openFile)
browseButton.grid(row=4, column=1)

predictButton = Button(root, text="Predict", command=genrePred)
predictButton.grid(row=5, column=1)

root.mainloop()