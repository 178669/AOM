from tkinter import *
import tkinter as tk
import time
import serial
import numpy
#from PIL import Image, ImageTk
"""
window = tk.Tk()

window.configure(bg="pink")
window.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1) #weight allows for resizing
window.geometry("800x800")
"""


def controlmotor():
    '''Motor Notes:
        - 10:1 Gear Ratio [Wood Gear]
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
    alt = True
    try:
        arduino.write("Counter".encode())
        data = arduino.readline()
        if data:
            print(data)
            alt = True
        time.sleep(5)
        controller.show_frame(StartPage)
    except Exception as e:
        print(e)
        arduino.close()


class startApp(tk.Tk):
    #startApp constructor
    def __init__(self, *args, **kwargs):

        #Tk constructor
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        #weight=1 allows for resizing
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #an array of frames will be used for traversing "pages"
        self.frames = {}

        #loop for frame/page initialization
        for F in (StartPage, ChoicePage, DonatePage, TokenPage, ShopPage, ShopPage2, Item1Desc_1):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    #displays current frame passed as input
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(3, minsize=0, weight=0)
        self.columnconfigure(3, minsize=0, weight=0) #weight allows for resizing

        b_startimg = tk.PhotoImage(file='Images1024/b_pink.png')

        #b_start = tk.Button(self, text="Start a Trade", width=200, command=lambda:controller.show_frame(Page1))
        b_start = tk.Button(self, image=b_startimg, command=lambda: controller.show_frame(ChoicePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_start.photo = b_startimg
        b_start.grid(row=2, column=1, sticky="nsew")
	
        RENT_CLOTHES = tk.Label(self, text="TRADE CLOTHES", bg="white", fg="pink", font=('Ubuntu Condensed', 100))
        RENT_CLOTHES.grid(row=1, column=1)

        b_motor = tk.Button(self, command=lambda: controlmotor())
        b_motor.grid(row=4)
	   
        fillL=LabelFrame(self, width=110, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(row=0)

        fillT=LabelFrame(self, height=100, borderwidth=0, highlightthickness=0, bg="white")
        fillT.grid(row=0)

"""
        b_startimg = tk.PhotoImage(file='images/startbutton.png')
        img_label = tk.Label(image=b_startimg) 
"""


class ChoicePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, minsize=50, weight=0)
        self.columnconfigure(3, minsize=270, weight=0)  # weight allows for resizing

        b_donateimg = tk.PhotoImage(file='Images1024/b_donate.png')
        b_shopimg = tk.PhotoImage(file='Images1024/b_shop.png')
        b_tradeimg = tk.PhotoImage(file='Images1024/b_trade.png')

        img1 = tk.PhotoImage(file='Images1024/oneimg.png')
        img2 = tk.PhotoImage(file='Images1024/twoimg.png')
        img3 = tk.PhotoImage(file='Images1024/threeimg.png')

        imglab1 = Label(self, image=img1, borderwidth=0)
        imglab2 = Label(self, image=img2, borderwidth=0)
        imglab3 = Label(self, image=img3, borderwidth=0)

        imglab1.photo=img1
        imglab2.photo=img2
        imglab3.photo=img3

        imglab1.grid(row=1, column=1, columnspan=2)
        imglab2.grid(row=3, column=1, columnspan=2)
        imglab3.grid(row=5, column=1, columnspan=2)

        title=Label(self, height=1, highlightthickness=0, borderwidth=0,fg="pink", bg="white", text="SELECT AN OPTION", font=('Ubuntu Condensed', 60))
        title.grid(row=0, column=2, columnspan=3)

        fillL=LabelFrame(self, width=180, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)
        #fill3=LabelFrame(self, width=50, borderwidth=0, highlightthickness=0, bg="white")
        #fill3.grid(row=0, column=2)

        b_donate = tk.Button(self, image=b_donateimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_donate.photo = b_donateimg
        b_donate.grid(row=1, column=2, columnspan=3)
        donatelabel = tk.Label(self,text= "Donate washed clothing items to the bin below. \nGain 1 Shop Credit per Item.", font=('Ubuntu Condensed', 20), justify="center", bg="white")
        donatelabel.grid(row=2, column=2, columnspan=3)

        b_shop = tk.Button(self, image=b_shopimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_shop.photo = b_shopimg
        b_shop.grid(row=3, column=2, columnspan=3)
        shoplabel = tk.Label(self, text= "Browse through our washed clothes and select one to rent. \nPick up your item at the Clothing Collection Window", font=('Ubuntu Condensed', 20), justify="center", bg="white", highlightthickness=0)
        shoplabel.grid(row=4, column=2, columnspan=3)

        b_trade = tk.Button(self, image=b_tradeimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_trade.photo = b_tradeimg
        b_trade.grid(row=5, column=2, columnspan=3)
        tradelabel = tk.Label(self, text= "Once you are done wearing your item, redonate it and take another", font=('Ubuntu Condensed', 20), justify="center", bg="white")
        tradelabel.grid(row=6, column=2, columnspan=3)

        #


class DonatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(0, weight=1)

        b_home = tk.Button(self, text="HOME", highlightthickness=0, command=lambda: controller.show_frame(StartPage))
        b_home.grid(row=0, column=0, sticky="ne")

        donatetitle = tk.Label(self, text="DONATE", font=('Ubuntu Condensed', 132), fg="pink", bg="white")
        donatetitle.grid(row=0, column=0)

        donatetext = tk.Label(self, text="Place Item In Donation Box Below", font=('Ubuntu Condensed',50), fg="red", bg="white")
        donatetext.grid(row=1,column=0)

        """
        fill1=LabelFrame(self, height=30)
        fill1.grid(row=5, column=0)
        """

        arrimg = tk.PhotoImage(file='Images1024/downarrow.png')
        arrlab = Label(self, image=arrimg, bg="white", borderwidth=0, highlightthickness=0)
        arrlab.photo = arrimg
        arrlab.grid(row=4, column=0)

        doneimg = tk.PhotoImage(file='Images1024/b_done.png')
        b_done = tk.Button(self, image=doneimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_done.photo = doneimg
        b_done.grid(row=6, column=0)

class TokenPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)

        fill1=LabelFrame(self, height=100, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=0, column=0)

        tokentitle = tk.Label(self, text="Please Tap Your ID", font=('Ubuntu Condensed', 150), fg="pink", bg="white")
        tokentitle.grid(row=2, column=0)

        tokentitlep2 = tk.Label(self, text="to Receive Your Token", font=('Ubuntu Condensed', 100), fg="pink", bg="white")
        tokentitlep2.grid(row=3,column=0)

        b_home = tk.Button(self, text="HOME", highlightthickness=0, command=lambda: controller.show_frame(StartPage))
        b_home.grid(row=0, column=0, sticky="ne")

class ShopPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(5, weight=1)
        self.columnconfigure(3, weight=1)

        fill1=LabelFrame(self, height=1, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=0, column=0)

        tokentitle = tk.Label(self, text="SHOP", font=('Ubuntu Condensed', 100), fg="pink", bg="white")
        tokentitle.grid(row=0, column=2, columnspan=2)

        b_home = tk.Button(self, text="HOME", highlightthickness=0, command=lambda: controller.show_frame(StartPage), width=8)
        b_home.grid(row=0, column=6, sticky="ne")

        item1img = PhotoImage(file='ClothesImages1024/greyblousere.png')
        item1 = tk.Button(self, image=item1img, command=lambda: controller.show_frame(Item1Desc_1))
        item1.photo = item1img
        item1.grid(row=3,column=1)

        item2img = PhotoImage(file='ClothesImages1024/redtop.png')
        item2 = tk.Button(self, image=item2img, command=lambda: controller.show_frame(StartPage))
        item2.photo = item2img
        item2.grid(row=3,column=3)

        item3img = PhotoImage(file='ClothesImages1024/blackdress.png')
        item3 = tk.Button(self, image=item3img, command=lambda: controller.show_frame(StartPage))
        item3.photo = item3img
        item3.grid(row=3,column=4)

        fill2=LabelFrame(self, width=80, borderwidth=0, highlightthickness=0, bg="white")
        fill2.grid(row=0, column=0, rowspan=3)

        fill3=LabelFrame(self, width=3, borderwidth=0, highlightthickness=0, bg="white")
        fill3.grid(row=3, column=2, rowspan=3)

        b_next = tk.Button(self, text="Next Page", highlightthickness=0, command=lambda: controller.show_frame(ShopPage2))
        b_next.grid(row=4, column=3, columnspan=1)

class ShopPage2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(5, weight=1)
        self.columnconfigure(3, weight=1)

        fill1=LabelFrame(self, height=2, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=0, column=0)

        shoptitle = tk.Label(self, text="SHOP", font=('Ubuntu Condensed', 100), fg="pink", bg="white")
        shoptitle.grid(row=0, column=2, columnspan=2)

        b_home = tk.Button(self, text="HOME", highlightthickness=0, command=lambda: controller.show_frame(StartPage), width=8)
        b_home.grid(row=0, column=6, sticky="ne")

        item1img = PhotoImage(file='ClothesImages1024/blueblouse.png')
        item1 = tk.Button(self, image=item1img, command=lambda: controller.show_frame(Item1Desc))
        item1.photo = item1img
        item1.grid(row=3,column=1)

        item2img = PhotoImage(file='ClothesImages1024/purpletop.png')
        item2 = tk.Button(self, image=item2img, command=lambda: controller.show_frame(StartPage))
        item2.photo = item2img
        item2.grid(row=3,column=3)

        item3img = PhotoImage(file='ClothesImages1024/furjacket.png')
        item3 = tk.Button(self, image=item3img, command=lambda: controller.show_frame(StartPage))
        item3.photo = item3img
        item3.grid(row=3,column=4)

        fill2=LabelFrame(self, width=80, borderwidth=0, highlightthickness=0, bg="white")
        fill2.grid(row=0, column=0, rowspan=3)

        fill3=LabelFrame(self, width=3, borderwidth=0, highlightthickness=0, bg="white")
        fill3.grid(row=3, column=2, rowspan=3)

        b_next = tk.Button(self, text="Next Page")
        b_next.grid(row=4, column=3, columnspan=1)

#def DescPg

class Item1Desc_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(5, weight=1)
        self.columnconfigure(3, weight=1)

        item1title = tk.Label(self, text="RED FLORAL TUBE TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=1, columnspan=3)
	
        fill1=LabelFrame(self, width=100, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=0, column=0)
	
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))

        item1img1 = PhotoImage(file='ClothesImages1024/redtop.png')
        item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')

        item1_list = [item1img1, item1img2, item1img3]

        item1 = tk.Label(self, image=item1_list[1])
        item1.photo = item1_list[1]
        item1.grid(row=2,column=1, columnspan=1)

        
 

app = startApp()
app.attributes('-fullscreen', True)
app.geometry("1920x1080")
app.mainloop()
