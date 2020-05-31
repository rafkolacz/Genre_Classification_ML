import Audio_Functions as audio
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.ttk as ttk
import threading
import time


# Error for wrong data format (not mp3 or wav)
class ExtensionError(Exception):
    pass


# class for main GUI
class GenreWindow:
    def __init__(self, master):
        self.master = master
        # some basic options
        master.title("Genre Predictor")
        master.resizable(False, False)
        master.geometry("400x140+900+400")

        # Welcoming labels
        self.myLabel1 = Label(master, text=" Hello, welcome in Genre Predictor!")
        self.myLabel1.grid(row=1, column=1)
        self.myLabel2 = Label(master, text="Please pick your songs location:")
        self.myLabel2.grid(row=2, column=1)

        # Browsing Button
        self.browseButton = Button(master, text="Browse",  command=self.openFile)
        self.browseButton.grid(row=4, column=1)

        # Action Button
        self.predictButton = ttk.Button(master, text="Predict", command=self.func)
        self.predictButton.grid(row=5, column=1)

    # function used when wrong file is picked
    def alert(self):
        self.alert = Toplevel()
        self.alert.title("Error")
        self.alert.resizable(False,False)
        self.alert.geometry("220x50+900+400")
        self.alertLabel = Label(self.alert, text="Wrong file, use only mp3, wav").pack()
        self.myButton = Button(self.alert, text="Close", command=self.alert.destroy).pack()

    # function for cleaning location label
    def cleanLabel(self):
        global location_str
        self.myLabel4 = Label(root, textvariable=location_str)
        self.myLabel4.grid(row=3, column=1)

    # loading label
    def progressBar(self):
        self.progressWindow = Toplevel()
        self.progressWindow.title("Progression")
        self.progressWindow.resizable(False,False)
        self.progressWindow.geometry("220x50+900+400")
        loading = ["Loading.", "Loading..", "Loading..."]
        for i in range(100):
            i = 0
            for j in range(3):
                self.loadLabel = Label(self.progressWindow, text=loading[j])
                self.loadLabel.grid(row = 0,column = 0)
                time.sleep(1)



    # file selection
    def openFile(self):
        global filename # 2 global values for better performance
        global location_str
        filename = askopenfilename()    # seek file
        if not location_str:            # erase nonempty label
            self.cleanLabel()
        location_str.set(filename)      # show current file location (with label below)

        self.myLabel4 = Label(root, textvariable=location_str)
        self.myLabel4.grid(row=3, column=1)
        return 0

    # execute function from Audio_Function (prediction)
    # returns genre
    def genrePred(self):
        global genre
        try:                            # checking if file extension is acceptable
            if not filename.endswith(('.mp3', '.wav')):
                raise ExtensionError
            self.progressBar()

            genre = audio.prediction(filename)  # function from Audio_Function

            # Label that shows genre (need  something to erase old genres!)
            self.myLabel5 = Label(root, text="Songs genre is: " + genre)
            self.myLabel5.grid(row=6, column=1)
            self.progressWindow.destroy()
        except ExtensionError:
            self.alert()

    def func(self):
        self.thread1 = threading.Thread(target=self.genrePred)
        self.thread1.start()
# Main window
root = Tk()

# for better performance 3 values are local
location_str = StringVar()  # location of music file (for gui)
filename = ''               # location of music file
genre = ''                  # genre
gui = GenreWindow(root)
root.mainloop()


