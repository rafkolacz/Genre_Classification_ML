import Audio_Functions as audio
from tkinter import *
from tkinter.filedialog import askopenfilename

filename = ''



def cleanLabel():
    #location_str = StringVar()
    #location_str.set(" ")
    global location_str2
    myLabel4 = Label(root, textvariable=location_str2)
    myLabel4.grid(row=3, column=1)


def openFile():
    global filename
    global location_str2
    location_str = StringVar()
    filename = askopenfilename()
    if not location_str2:
        cleanLabel()
    location_str2.set(filename)
    myLabel4 = Label(root, textvariable=location_str2)
    myLabel4.grid(row=3, column=1)
    return 0


def genrePred():
    if filename == '':
        myLabel4 = Label(root, text="Please input file first!")
        myLabel4.grid(row=3, column=1)
    else:
        genre = audio.prediction(filename)
        myLabel5 = Label(root, text="Songs genre is: " + genre)
        myLabel5.grid(row=6, column=1)


# Main window
root = Tk()
root.title("Genre Predictor")
root.resizable(False, False)
root.geometry("400x140+900+400")
location_str2 = StringVar()

myLabel1 = Label(root, text=" Hello, welcome in Genre Predictor!")
myLabel1.grid(row=1, column=1)
myLabel2 = Label(root,text = "Please pick your songs location:")
myLabel2.grid(row=2, column=1)


browseButton = Button(root, text="Browse", command=openFile)
browseButton.grid(row=4, column=1)

predictButton = Button(root, text="Predict", command=genrePred)
predictButton.grid(row=5, column=1)

root.mainloop()