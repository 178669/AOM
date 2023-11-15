from tkinter import *
import tkinter as tk
import serial
import SerialControl as Ser
from Pages import *

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
        for F in (StartPage, ChoicePage, DonatePage, TokenPage, ShopPage, ShopPage2, 
            Item1Desc_1, Item1Desc_2, Item1Desc_3, 
            Item2Desc_1, Item2Desc_2, Item2Desc_3,
            Item3Desc_1, Item3Desc_2, Item3Desc_3,
            Item4Desc_1, Item4Desc_2, Item4Desc_3,
            Item5Desc_1, Item5Desc_2, Item5Desc_3,
            Item6Desc_1, Item6Desc_2, Item6Desc_3):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    #displays current frame passed as input
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def refresh(self):
    self.destroy()
    self.__init__()
    self.attributes('-fullscreen', True)
'''
arduino = serial.Serial(
port='/dev/ttyUSB0',
baudrate=9600,
bytesize=serial.EIGHTBITS,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
timeout=2,
xonxoff=False,
rtscts=False,
dsrdtr=False,
writeTimeout=5)
'''
app = startApp()
app.attributes('-fullscreen', True)#enable this for demo
app.mainloop()

