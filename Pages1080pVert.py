import tkinter as tk
import SerialControl as Ser
from PIL import Image, ImageTk
from itertools import count, cycle


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

class AcquirePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(2, weight=1)


        token1img = tk.PhotoImage(file='Images/Acquire.png')
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

def Go(controller, target, page):
    DescPg = [Item1, Item2, Item3, Item4, Item5, Item1, Item1, Item1, Item1]
    controller.show_frame(DescPg[page])

    Ser.controlmotor(target, 5)
    

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

        b_homeimg = tk.PhotoImage(file='Images/b_home.png')
        b_home = tk.Button(self, image=b_homeimg,borderwidth=0, highlightthickness=0, width = 141, height = 137,command=lambda: controller.show_frame(StartPage))
        b_home.photo = b_homeimg
        b_home.grid(row=0, column=2, sticky ='ne')
        b_home.lift()

        DescPg = [Item1, Item2, Item3, Item4, Item5, Item1, Item1, Item1, Item1]
        
        NA = tk.PhotoImage(file='NA/NA.png')
        img = []
        img.append(tk.PhotoImage(file='Item1/Shop.png'))
        img.append(tk.PhotoImage(file='Item2/Shop.png'))
        img.append(tk.PhotoImage(file='Item3/Shop.png'))
        img.append(tk.PhotoImage(file='Item4/Shop.png'))
        img.append(tk.PhotoImage(file='Item5/Shop.png'))
        
        imglab = []
        '''
        for i in range(len(Avail)):
            if Avail[i] == 1:
                imglab.append(tk.Button(self, image=img[i], borderwidth=0, command=lambda: controller.show_frame(DescPg[i])))
            if Avail[i] == 0:
                imglab.append(tk.Button(self, image = NA, borderwidth=0))
        '''
        
        imglab.append(tk.Button(self, image=img[0], borderwidth=0, command=lambda: Go(controller, 1, 0)))
        imglab.append(tk.Button(self, image=img[1], borderwidth=0, command=lambda: Go(controller, 2, 1)))
        imglab.append(tk.Button(self, image=img[2], borderwidth=0, command=lambda: Go(controller, 3, 2)))
        imglab.append(tk.Button(self, image=img[3], borderwidth=0, command=lambda: Go(controller, 4, 3)))
        imglab.append(tk.Button(self, image=img[4], borderwidth=0, command=lambda: Go(controller, 5, 4)))
        imglab.append(tk.Button(self, image = NA, borderwidth=0))
        imglab.append(tk.Button(self, image = NA, borderwidth=0))
        imglab.append(tk.Button(self, image = NA, borderwidth=0))
        imglab.append(tk.Button(self, image = NA, borderwidth=0))

        imglab[0].grid(row=1, column=0)
        imglab[1].grid(row=1, column=1)
        imglab[2].grid(row=1, column=2)
        imglab[3].grid(row=2, column=0)
        imglab[4].grid(row=2, column=1)
        imglab[5].grid(row=2, column=2)
        imglab[6].grid(row=3, column=0)
        imglab[7].grid(row=3, column=1)
        imglab[8].grid(row=3, column=2)
  
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

        b_homeimg = tk.PhotoImage(file='Images/b_home.png')
        b_home = tk.Button(self, image=b_homeimg,borderwidth=0, highlightthickness=0, width = 141, height = 137,command=lambda: controller.show_frame(StartPage))
        b_home.photo = b_homeimg
        b_home.grid(row=0, column = 1, sticky='ne')
        b_home.lift()

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

        Acqimg = tk.PhotoImage(file='DescPage/Acquire.png')
        Acq = tk.Button(self, image=Acqimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(AcquirePage))
        Acq.photo = Acqimg
        Acq.grid(row=4, column=0)

        Viewimg = tk.PhotoImage(file='DescPage/View.png')
        View = tk.Button(self, image=Viewimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(ShopPage))
        View.photo = Viewimg
        View.grid(row=4, column=1)
        
        itempic = []
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Front.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Side.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Back.png')))
        
        item = tk.Label(self, image=itempic[0], borderwidth=0)
        item.photo = itempic[0]
        item.grid(row=1, column=0, columnspan=2)
        #changepic(item, itempic[1])

        def forward(self, item, itempic, num):
            lnum = num
            if num+1 < 3:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num+1])
                self.item.photo=itempic[num+1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num+1 >= 3:
                num = -1
                lnum = 0
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[0])
                self.item.photo=itempic[0]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, num + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, lnum - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

        def backward(self, item, itempic, num):
            rnum = num
            if num-1 > -1:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num-1])
                self.item.photo=itempic[num-1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num-1 <= -1:
                num = 3
                rnum = 2
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[2])
                self.item.photo=itempic[2]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, num - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, rnum + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

        RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
        LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')

        RArr = tk.Button(self,command=lambda: forward(self, item, itempic, 0), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        RArr.photo = RArrimg
        RArr.grid(row=2, column=1)

        LArr = tk.Button(self,command=lambda: backward(self, item, itempic, 0), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        LArr.photo = LArrimg
        LArr.grid(row=2, column=0)

class Item2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        

        rat = 'Item2'

        nameimg = tk.PhotoImage(file=rat+'/Top.png')
        name = tk.Label(self, image=nameimg, borderwidth=0, highlightthickness=0)
        name.photo = nameimg
        name.grid(row=0, column=0, columnspan=2)

        b_homeimg = tk.PhotoImage(file='Images/b_home.png')
        b_home = tk.Button(self, image=b_homeimg,borderwidth=0, highlightthickness=0, width = 141, height = 137,command=lambda: controller.show_frame(StartPage))
        b_home.photo = b_homeimg
        b_home.grid(row=0, column = 1, sticky='ne')
        b_home.lift()

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

        Acqimg = tk.PhotoImage(file='DescPage/Acquire.png')
        Acq = tk.Button(self, image=Acqimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(AcquirePage))
        Acq.photo = Acqimg
        Acq.grid(row=4, column=0)

        Viewimg = tk.PhotoImage(file='DescPage/View.png')
        View = tk.Button(self, image=Viewimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(ShopPage))
        View.photo = Viewimg
        View.grid(row=4, column=1)
        
        itempic = []
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Front.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Side.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Back.png')))
        
        item = tk.Label(self, image=itempic[0], borderwidth=0)
        item.photo = itempic[0]
        item.grid(row=1, column=0, columnspan=2)
        #changepic(item, itempic[1])

        def forward(self, item, itempic, num):
            lnum = num
            if num+1 < 3:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num+1])
                self.item.photo=itempic[num+1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num+1 >= 3:
                num = -1
                lnum = 0
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[0])
                self.item.photo=itempic[0]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, num + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, lnum - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

        def backward(self, item, itempic, num):
            rnum = num
            if num-1 > -1:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num-1])
                self.item.photo=itempic[num-1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num-1 <= -1:
                num = 3
                rnum = 2
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[2])
                self.item.photo=itempic[2]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, num - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, rnum + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

        RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
        LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')

        RArr = tk.Button(self,command=lambda: forward(self, item, itempic, 0), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        RArr.photo = RArrimg
        RArr.grid(row=2, column=1)

        LArr = tk.Button(self,command=lambda: backward(self, item, itempic, 0), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        LArr.photo = LArrimg
        LArr.grid(row=2, column=0)

class Item3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        

        rat = 'Item3'

        nameimg = tk.PhotoImage(file=rat+'/Top.png')
        name = tk.Label(self, image=nameimg, borderwidth=0, highlightthickness=0)
        name.photo = nameimg
        name.grid(row=0, column=0, columnspan=2)


        b_homeimg = tk.PhotoImage(file='Images/b_home.png')
        b_home = tk.Button(self, image=b_homeimg,borderwidth=0, highlightthickness=0, width = 141, height = 137,command=lambda: controller.show_frame(StartPage))
        b_home.photo = b_homeimg
        b_home.grid(row=0, column = 1, sticky='ne')
        b_home.lift()

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

        Acqimg = tk.PhotoImage(file='DescPage/Acquire.png')
        Acq = tk.Button(self, image=Acqimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(AcquirePage))
        Acq.photo = Acqimg
        Acq.grid(row=4, column=0)

        Viewimg = tk.PhotoImage(file='DescPage/View.png')
        View = tk.Button(self, image=Viewimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(ShopPage))
        View.photo = Viewimg
        View.grid(row=4, column=1)
        
        itempic = []
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Front.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Side.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Back.png')))
        
        item = tk.Label(self, image=itempic[0], borderwidth=0)
        item.photo = itempic[0]
        item.grid(row=1, column=0, columnspan=2)
        #changepic(item, itempic[1])

        def forward(self, item, itempic, num):
            lnum = num
            if num+1 < 3:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num+1])
                self.item.photo=itempic[num+1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num+1 >= 3:
                num = -1
                lnum = 0
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[0])
                self.item.photo=itempic[0]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, num + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, lnum - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

        def backward(self, item, itempic, num):
            rnum = num
            if num-1 > -1:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num-1])
                self.item.photo=itempic[num-1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num-1 <= -1:
                num = 3
                rnum = 2
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[2])
                self.item.photo=itempic[2]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, num - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, rnum + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

        RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
        LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')

        RArr = tk.Button(self,command=lambda: forward(self, item, itempic, 0), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        RArr.photo = RArrimg
        RArr.grid(row=2, column=1)

        LArr = tk.Button(self,command=lambda: backward(self, item, itempic, 0), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        LArr.photo = LArrimg
        LArr.grid(row=2, column=0)


class Item4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        

        rat = 'Item4'

        nameimg = tk.PhotoImage(file=rat+'/Top.png')
        name = tk.Label(self, image=nameimg, borderwidth=0, highlightthickness=0)
        name.photo = nameimg
        name.grid(row=0, column=0, columnspan=2)

        b_homeimg = tk.PhotoImage(file='Images/b_home.png')
        b_home = tk.Button(self, image=b_homeimg,borderwidth=0, highlightthickness=0, width = 141, height = 137,command=lambda: controller.show_frame(StartPage))
        b_home.photo = b_homeimg
        b_home.grid(row=0, column = 1, sticky='ne')
        b_home.lift()

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

        Acqimg = tk.PhotoImage(file='DescPage/Acquire.png')
        Acq = tk.Button(self, image=Acqimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(AcquirePage))
        Acq.photo = Acqimg
        Acq.grid(row=4, column=0)

        Viewimg = tk.PhotoImage(file='DescPage/View.png')
        View = tk.Button(self, image=Viewimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(ShopPage))
        View.photo = Viewimg
        View.grid(row=4, column=1)
        
        itempic = []
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Front.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Side.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Back.png')))
        
        item = tk.Label(self, image=itempic[0], borderwidth=0)
        item.photo = itempic[0]
        item.grid(row=1, column=0, columnspan=2)
        #changepic(item, itempic[1])

        def forward(self, item, itempic, num):
            lnum = num
            if num+1 < 3:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num+1])
                self.item.photo=itempic[num+1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num+1 >= 3:
                num = -1
                lnum = 0
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[0])
                self.item.photo=itempic[0]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, num + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, lnum - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

        def backward(self, item, itempic, num):
            rnum = num
            if num-1 > -1:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num-1])
                self.item.photo=itempic[num-1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num-1 <= -1:
                num = 3
                rnum = 2
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[2])
                self.item.photo=itempic[2]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, num - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, rnum + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

        RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
        LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')

        RArr = tk.Button(self,command=lambda: forward(self, item, itempic, 0), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        RArr.photo = RArrimg
        RArr.grid(row=2, column=1)

        LArr = tk.Button(self,command=lambda: backward(self, item, itempic, 0), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        LArr.photo = LArrimg
        LArr.grid(row=2, column=0)


class Item5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")

        rat = 'Item5'

        nameimg = tk.PhotoImage(file=rat+'/Top.png')
        name = tk.Label(self, image=nameimg, borderwidth=0, highlightthickness=0)
        name.photo = nameimg
        name.grid(row=0, column=0, columnspan=2)

        b_homeimg = tk.PhotoImage(file='Images/b_home.png')
        b_home = tk.Button(self, image=b_homeimg,borderwidth=0, highlightthickness=0, width = 141, height = 137,command=lambda: controller.show_frame(StartPage))
        b_home.photo = b_homeimg
        b_home.grid(row=0, column = 1, sticky='ne')
        b_home.lift()

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

        Acqimg = tk.PhotoImage(file='DescPage/Acquire.png')
        Acq = tk.Button(self, image=Acqimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(AcquirePage))
        Acq.photo = Acqimg
        Acq.grid(row=4, column=0)

        Viewimg = tk.PhotoImage(file='DescPage/View.png')
        View = tk.Button(self, image=Viewimg, borderwidth=0, height = 284, width = 540, highlightthickness=0, command=lambda: controller.show_frame(ShopPage))
        View.photo = Viewimg
        View.grid(row=4, column=1)
        
        itempic = []
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Front.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Side.png')))
        itempic.append(ImageTk.PhotoImage(Image.open(rat+'/Back.png')))
        
        item = tk.Label(self, image=itempic[0], borderwidth=0)
        item.photo = itempic[0]
        item.grid(row=1, column=0, columnspan=2)
        #changepic(item, itempic[1])

        def forward(self, item, itempic, num):
            lnum = num
            if num+1 < 3:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num+1])
                self.item.photo=itempic[num+1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num+1 >= 3:
                num = -1
                lnum = 0
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[0])
                self.item.photo=itempic[0]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, num + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, lnum - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

        def backward(self, item, itempic, num):
            rnum = num
            if num-1 > -1:
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[num-1])
                self.item.photo=itempic[num-1]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                #self.item.lift()

            if num-1 <= -1:
                num = 3
                rnum = 2
                self.item = item
                self.itempic = itempic
                self.item.grid_forget()
                self.item.configure(image = itempic[2])
                self.item.photo=itempic[2]
                #self.item.photo = itempic[num+1]
                self.item.grid(row=1, column=0, columnspan=2)
                
            self.item.grid(row=1, column=0, columnspan=2)
            LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')
            LArr = tk.Button(self ,command=lambda: backward(self, self.item, self.itempic, num - 1), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            LArr.photo = LArrimg
            LArr.grid(row=2, column=0)
            LArr.lift()

            RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
            RArr = tk.Button(self ,command=lambda: forward(self, self.item, self.itempic, rnum + 1), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
            RArr.photo = RArrimg
            RArr.grid(row=2, column=1)
            RArr.lift()

        RArrimg = tk.PhotoImage(file='DescPage/RArrow.png')
        LArrimg = tk.PhotoImage(file='DescPage/LArrow.png')

        RArr = tk.Button(self,command=lambda: forward(self, item, itempic, 0), image=RArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        RArr.photo = RArrimg
        RArr.grid(row=2, column=1)

        LArr = tk.Button(self,command=lambda: backward(self, item, itempic, 0), image=LArrimg, borderwidth=0, height = 134, width = 540, highlightthickness=0)
        LArr.photo = LArrimg
        LArr.grid(row=2, column=0)

