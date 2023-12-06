import tkinter as tk
import SerialControl as Ser
from PIL import Image, ImageTk
from itertools import count, cycle

s = 1.55 # s for scale
'''
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(0, weight=1)
    
        b_startimg = tk.PhotoImage(file='Images/b_start.png')

        
        #b_start = tk.Button(self, text="Start a Trade", width=200, command=lambda:controller.show_frame(Page1))
        titleimg = tk.PhotoImage(file='Images/StartTitle.png')
        title = tk.Label(self, image=titleimg, borderwidth=0)
        title.photo=titleimg
        title.grid(row=1, column=0)
        
        b_start = tk.Button(self, image=b_startimg, command=lambda: controller.show_frame(ChoicePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0, bd=0, pady=0, padx=0, height=100)
        b_start.photo = b_startimg
        b_start.grid(row=3, column=0)
        
        cloudimg = tk.PhotoImage(file='Images/Clouds.png')
        cloud = tk.Label(self, image=cloudimg, borderwidth=0)
        cloud.photo=cloudimg
        cloud.grid(row=5, column=0)
        
        fillT=tk.LabelFrame(self, height=100, borderwidth=0, highlightthickness=0, bg="white")
        fillT.grid(row=0)
        fill1=tk.LabelFrame(self, height=100, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=4)
        fill2=tk.LabelFrame(self, height=50, borderwidth=0, highlightthickness=0, bg="white")
        fill2.grid(row=2)
'''
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(0, weight=1)
    
        b_startimg = tk.PhotoImage(file='Images/pgone2.png')

        
        #b_start = tk.Button(self, text="Start a Trade", width=200, command=lambda:controller.show_frame(Page1))
        titleimg = tk.PhotoImage(file='Images/pgone1.png')
        title = tk.Label(self, image=titleimg, borderwidth=0, highlightthickness=0)
        title.photo=titleimg
        title.grid(row=1, column=0)
        
        b_start = tk.Button(self, image=b_startimg, command=lambda: controller.show_frame(ChoicePage), borderwidth=0, highlightthickness=0, bd=0, pady=0, padx=0, height=473)
        b_start.photo = b_startimg
        b_start.grid(row=2, column=0)
        
        cloudimg = tk.PhotoImage(file='Images/pgone3.png')
        cloud = tk.Label(self, image=cloudimg, borderwidth=0, highlightthickness=0)
        cloud.photo=cloudimg
        cloud.grid(row=3, column=0)

'''
class ChoicePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, minsize=int(50*s), weight=0)
        self.columnconfigure(3, minsize=int(270*s), weight=0)  # weight allows for resizing

        b_donateimg = tk.PhotoImage(file='Images1024/b_donate.png')
        b_shopimg = tk.PhotoImage(file='Images1024/b_shop.png')
        b_tradeimg = tk.PhotoImage(file='Images1024/b_trade.png')

        img1 = tk.PhotoImage(file='Images1024/oneimg.png')
        img2 = tk.PhotoImage(file='Images1024/twoimg.png')
        img3 = tk.PhotoImage(file='Images1024/threeimg.png')

        imglab1 = tk.Label(self, image=img1, borderwidth=0)
        imglab2 = tk.Label(self, image=img2, borderwidth=0) 
        imglab3 = tk.Label(self, image=img3, borderwidth=0)

        imglab1.photo=img1
        imglab2.photo=img2
        imglab3.photo=img3

        imglab1.grid(row=1, column=1, columnspan=2)
        imglab2.grid(row=3, column=1, columnspan=2)
        imglab3.grid(row=5, column=1, columnspan=2)

        title=tk.Label(self, height=1, highlightthickness=0, borderwidth=0,fg="pink", bg="white", text="SELECT AN OPTION", font=('Ubuntu Condensed', int(60*s)))
        title.grid(row=0, column=2, columnspan=3)

        fillL=tk.LabelFrame(self, width=int(180*s), borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)
        #fill3=LabelFrame(self, width=50, borderwidth=0, highlightthickness=0, bg="white")
        #fill3.grid(row=0, column=2)

        b_donate = tk.Button(self, image=b_donateimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_donate.photo = b_donateimg
        b_donate.grid(row=1, column=2, columnspan=3)
        donatelabel = tk.Label(self,text= "Donate washed clothing items to the bin below. \nGain 1 Shop Credit per Item.", font=('Ubuntu Condensed', int(20*s)), justify="center", bg="white")
        donatelabel.grid(row=2, column=2, columnspan=3)

        b_shop = tk.Button(self, image=b_shopimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_shop.photo = b_shopimg
        b_shop.grid(row=3, column=2, columnspan=3)
        shoplabel = tk.Label(self, text= "Browse through our washed clothes and select one to rent. \nPick up your item at the Clothing Collection Window", font=('Ubuntu Condensed', int(20*s)), justify="center", bg="white", highlightthickness=0)
        shoplabel.grid(row=4, column=2, columnspan=3)

        b_trade = tk.Button(self, image=b_tradeimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_trade.photo = b_tradeimg
        b_trade.grid(row=5, column=2, columnspan=3)
        tradelabel = tk.Label(self, text= "Once you are done wearing your item, redonate it and take another", font=('Ubuntu Condensed', int(20*s)), justify="center", bg="white")
        tradelabel.grid(row=6, column=2, columnspan=3)
'''
class ChoicePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        #self.rowconfigure(6, minsize=int(50*s), weight=0)
        #self.columnconfigure(3, minsize=int(270*s), weight=0)  # weight allows for resizing
        
        frag1img = tk.PhotoImage(file='Images/choicepg1.png')
        b_donateimg = tk.PhotoImage(file='Images/choicepg2.png')
        frag3img = tk.PhotoImage(file='Images/choicepg3.png')
        b_shopimg = tk.PhotoImage(file='Images/choicepg4.png')
        frag5img = tk.PhotoImage(file='Images/choicepg5.png')

        frag1 = tk.Label(self, image=frag1img, borderwidth=0)
        frag3 = tk.Label(self, image=frag3img, borderwidth=0) 
        frag5 = tk.Label(self, image=frag5img, borderwidth=0)

        frag1.photo=frag1img
        frag3.photo=frag3img
        frag5.photo=frag5img

        frag1.grid(row=1)
        frag3.grid(row=3)
        frag5.grid(row=5)

        b_donate = tk.Button(self, image=b_donateimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0, height=264)
        b_donate.photo = b_donateimg
        b_donate.grid(row=2)

        b_shop = tk.Button(self, image=b_shopimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0, height=261)
        b_shop.photo = b_shopimg
        b_shop.grid(row=4)


class DonatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        donateTimg = tk.PhotoImage(file='Images/donate1.png')
        b_doneimg = tk.PhotoImage(file='Images/donate2.png')
        
        donateT = tk.Label(self, image=donateTimg, borderwidth=0)
        b_done = tk.Button(self, image=b_doneimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0, height=372)
        donateT.photo = donateTimg
        b_done.photo = b_doneimg
        
        donateT.grid(row=0)
        b_done.grid(row=1)
        
        
class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
    def unload(self):
        self.config(image=None)
        self.frames = None
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
    

class TokenPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(2, weight=1)


        token1img = tk.PhotoImage(file='Images/token1.png')
        b_doneimg = tk.PhotoImage(file='Images/token3.png')
        token2img = tk.PhotoImage(file='Images/token2.png')

        token1 = tk.Label(self, image=token1img, borderwidth=0)
        b_done = tk.Button(self, image=b_doneimg, command=lambda: controller.show_frame(ChoicePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0, height=386)
        token2 = tk.Label(self, image=token2img, borderwidth=0)
        token1.photo = token1img
        b_done.photo = b_doneimg
        token2.photo = token2img
        token1.grid(row=0)
        token2.grid(row=1)
        
        b_homeimg = tk.PhotoImage(file='Images/b_home.png')
        b_home = tk.Button(self, image=b_homeimg,borderwidth=0, highlightthickness=0, width = 141, height = 137,command=lambda: controller.show_frame(StartPage))
        b_home.photo = b_homeimg
        b_home.grid(row=0, sticky='ne')
        #GIF.grid(row=1)
        #GIF.lift()
        
        lbl = ImageLabel(self, borderwidth=0, highlightthickness=0)
        lbl.grid(row=1)
        lbl.load('Images/NFCGIF.gif')
    
        # set first image on canvas
        #self.image_on_canvas = self.canvas.create_image(300, 353, image=self.my_images[self.my_image_number])
        b_done.grid(row=2)
        
        
class ShopPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        
        Avail = [1, 1, 1, 1, 1, 0, 0, 0, 0]

        self.rowconfigure(0, minsize=336)
        self.rowconfigure(4, minsize=182)
        
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        
        baseimg = tk.PhotoImage(file='Images/ShopPage.png')
        base = tk.Label(self, image=baseimg, borderwidth=0)
        base.photo = baseimg
        base.grid(row=0, column=0, rowspan=5, columnspan=3)

        DescPg = [Item1, Item1, Item1, Item1, Item1, Item1, Item1, Item1, Item1]
        
        NA = tk.PhotoImage(file='NA/NA.png')
        img = []
        img.append(tk.PhotoImage(file='Item1/Shop.png'))
        img.append(tk.PhotoImage(file='Item2/Shop.png'))
        img.append(tk.PhotoImage(file='Item3/Shop.png'))
        img.append(tk.PhotoImage(file='Item4/Shop.png'))
        img.append(tk.PhotoImage(file='Item5/Shop.png'))
        
        imglab = []
        i=0
        for i in range(len(Avail)):
            if Avail[i] == 1:
                imglab.append(tk.Button(self, image=img[i], borderwidth=0, command=lambda: controller.show_frame(DescPg[i])))
            if Avail[i] == 0:
                imglab.append(tk.Label(self, image = NA, borderwidth=0))
        
        imglab[0].grid(row=1, column=0)
        imglab[1].grid(row=1, column=1)
        imglab[2].grid(row=1, column=2)
        imglab[3].grid(row=2, column=0)
        imglab[4].grid(row=2, column=1)
        imglab[5].grid(row=2, column=2)
        imglab[6].grid(row=3, column=0)
        imglab[7].grid(row=3, column=1)
        imglab[8].grid(row=3, column=2)
        i=0
        for i in range(len(Avail)):
            if Avail[i] == 1:
                imglab[i].photo = img[i]
                imglab[i].lift()
            else:
                imglab[i].photo = NA
                imglab[i].lift()




class Item1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        
        rat = 'Item1'

        nameimg = tk.PhotoImage(file=rat+'/Top.png')
        name = tk.Label(self, image=nameimg, borderwidth=0, highlightthickness=0)
        name.photo = nameimg
        name.grid(row=0, column=0, columnspan=2)

        frameimg = tk.PhotoImage(file='DescPage/Frame.png')
        frame = tk.Label(self, image=frameimg, borderwidth=0, highlightthickness=0)
        frame.photo = frameimg
        frame.grid(row=1, column=0, columnspan=2)

        LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
        LArr = tk.Button(self, image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        LArr.photo = LArrimg
        LArr.grid(row=2, column=0)

       

        tableimg = tk.PhotoImage(file=rat+'/Table.png')
        table = tk.Label(self, image=tableimg, borderwidth=0)
        table.photo = tableimg
        table.grid(row=3, column=0, columnspan=2)

        Acqimg = tk.PhotoImage(file='DescPage/View.png')
        Acq = tk.Button(self, image=Acqimg, borderwidth=0, height = 284, width = 540, highlightthickness=0)
        Acq.photo = Acqimg
        Acq.grid(row=4, column=0)

        Viewimg = tk.PhotoImage(file='DescPage/Acquire.png')
        View = tk.Button(self, image=Viewimg, borderwidth=0, height = 284, width = 540, highlightthickness=0)
        View.photo = Viewimg
        View.grid(row=4, column=1)
        
        
        item = tk.Label(self, image=itempic[0], borderwidth=0)
        item.photo = itempic[0]
        item.grid(row=1, column=0, columnspan=2)
        #changepic(item, itempic[1])

        itempic = []
        itempic.append(tk.PhotoImage(file='Item1/Front.png'))
        itempic.append(tk.PhotoImage(file='Item1/Side.png'))
        itempic.append(tk.PhotoImage(file='Item1/Back.png'))

        def forward(image_number):
            global item
            global RArr
            global button_back

            item.grid_forget()
            item = tk.Label(image=itempic[image_number-1])
            button_foward = Button(root)

        def back():
            global item
            global RArr
            global button_back

        
        RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
    
        RArr = tk.Button(self,command=lambda: changepic(item, itempic[1]), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        RArr.photo = RArrimg
        RArr.grid(row=2, column=1)

        LArr = tk.Button(self,command=lambda: changepic(item, itempic[1]), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        LArr.photo = RArrimg
        LArr.grid(row=2, column=1)
