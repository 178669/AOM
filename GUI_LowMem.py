from tkinter import *
import tkinter as tk
import serial
import SerialControl as Ser
from Pages1080pVert import *
#from playsound import playsound

#from pykeyboard import PyKeyboard
class startApp(tk.Tk):
    #startApp constructor
    def __init__(self, *args, **kwargs):

        #Tk constructor
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #an array of frames will be used for traversing "pages"
        self.frames = {}

        #loop for frame/page initialization
        for F in (StartPage, ChoicePage, DonatePage, TokenPage, ShopPage,
            Item1, Item2, Item3, Item4, Item5, AcquirePage):
            frame = F(container, self)
            self.frames[F] = frame
            #frame.grid(row=0, column=0, sticky="nw")
        self.show_frame(StartPage)

    #displays current frame passed as input
    def show_frame(self, cont):
        keylist = [StartPage, ChoicePage, DonatePage, TokenPage, ShopPage,
        Item1, Item2, Item3, Item4, Item5, AcquirePage]
        last = keylist.index(cont)-1
        self.frames[keylist[last]].grid_remove()
        #playsound('Drip.mp3')
        frame = self.frames[cont]
        frame.grid(row=0, column = 0, sticky="nw")
        frame.tkraise()

portarr = Ser.portarr
HPorJetson = Ser.HPorJetson
arduino = serial.Serial(
port= portarr[HPorJetson],
baudrate=9600,
bytesize=serial.EIGHTBITS,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
timeout=2,
xonxoff=False,
rtscts=False,
dsrdtr=False,
writeTimeout=5)

app = startApp()
#app.attributes('-fullscreen', True)#enable this for demo
#app.configure(cursor='none')
app.mainloop()

