import tkinter as tk
import SerialControl as Ser

s = 1.55 # s for scale
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

        RENT_CLOTHES = tk.Label(self, text="TRADE CLOTHES", bg="white", fg="pink", font=('Ubuntu Condensed', 100*s))
        RENT_CLOTHES.grid(row=1, column=1)

        #b_motor = tk.Button(self, command=lambda: Ser.controlmotor(1, 6))
        #b_motor.grid(row=4)

        fillL=tk.LabelFrame(self, width=110*s, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(row=0)

        fillT=tk.LabelFrame(self, height=100*s, borderwidth=0, highlightthickness=0, bg="white")
        fillT.grid(row=0)


class ChoicePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, minsize=50*s, weight=0)
        self.columnconfigure(3, minsize=270*s, weight=0)  # weight allows for resizing

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

        title=tk.Label(self, height=1, highlightthickness=0, borderwidth=0,fg="pink", bg="white", text="SELECT AN OPTION", font=('Ubuntu Condensed', 60*s))
        title.grid(row=0, column=2, columnspan=3)

        fillL=tk.LabelFrame(self, width=180*s, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)
        #fill3=LabelFrame(self, width=50, borderwidth=0, highlightthickness=0, bg="white")
        #fill3.grid(row=0, column=2)

        b_donate = tk.Button(self, image=b_donateimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_donate.photo = b_donateimg
        b_donate.grid(row=1, column=2, columnspan=3)
        donatelabel = tk.Label(self,text= "Donate washed clothing items to the bin below. \nGain 1 Shop Credit per Item.", font=('Ubuntu Condensed', 20*s), justify="center", bg="white")
        donatelabel.grid(row=2, column=2, columnspan=3)

        b_shop = tk.Button(self, image=b_shopimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_shop.photo = b_shopimg
        b_shop.grid(row=3, column=2, columnspan=3)
        shoplabel = tk.Label(self, text= "Browse through our washed clothes and select one to rent. \nPick up your item at the Clothing Collection Window", font=('Ubuntu Condensed', 20*s), justify="center", bg="white", highlightthickness=0)
        shoplabel.grid(row=4, column=2, columnspan=3)

        b_trade = tk.Button(self, image=b_tradeimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_trade.photo = b_tradeimg
        b_trade.grid(row=5, column=2, columnspan=3)
        tradelabel = tk.Label(self, text= "Once you are done wearing your item, redonate it and take another", font=('Ubuntu Condensed', 20*s), justify="center", bg="white")
        tradelabel.grid(row=6, column=2, columnspan=3)

class DonatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(0, weight=1)

        homeimg = tk.PhotoImage(file='Images1024/homebutton.png')
        b_home = tk.Button(self,image=homeimg, command=lambda: controller.show_frame(StartPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_home.image = homeimg
        b_home.grid(row=0, column=0, sticky="ne")

        donatetitle = tk.Label(self, text="DONATE", font=('Ubuntu Condensed', 132*s), fg="pink", bg="white")
        donatetitle.grid(row=0, column=0)

        donatetext = tk.Label(self, text="Place Item In Donation Box Below", font=('Ubuntu Condensed',50*s), fg="red", bg="white")
        donatetext.grid(row=1,column=0)

        """
        fill1=LabelFrame(self, height=30)
        fill1.grid(row=5, column=0)
        """

        arrimg = tk.PhotoImage(file='Images1024/downarrow.png')
        arrlab = tk.Label(self, image=arrimg, bg="white", borderwidth=0, highlightthickness=0)
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

        fill1=tk.LabelFrame(self, height=100*s, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=0, column=0)

        tokentitle = tk.Label(self, text="Please Tap Your ID", font=('Ubuntu Condensed', 75*s), fg="pink", bg="white")
        tokentitle.grid(row=2, column=0)

        tokentitlep2 = tk.Label(self, text="to Receive Your Token", font=('Ubuntu Condensed', 50*s), fg="pink", bg="white")
        tokentitlep2.grid(row=3,column=0)

        homeimg = tk.PhotoImage(file='Images1024/homebutton.png')
        b_home = tk.Button(self,image=homeimg, command=lambda: controller.show_frame(StartPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_home.image = homeimg
        b_home.grid(row=0, column=0, sticky="ne")

class ShopPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(5, weight=1)
        self.columnconfigure(3, weight=1)

        fill1=tk.LabelFrame(self, height=1, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=0, column=0)

        tokentitle = tk.Label(self, text="SHOP", font=('Ubuntu Condensed', 100*s), fg="pink", bg="white")
        tokentitle.grid(row=0, column=2, columnspan=2)

        
        homeimg = tk.PhotoImage(file='Images1024/homebutton.png')
        b_home = tk.Button(self,image=homeimg, command=lambda: controller.show_frame(StartPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_home.image = homeimg
        b_home.grid(row=0, column=5, sticky="ne")

        item1img = tk.PhotoImage(file='Item1/Shop.png')
        item1 = tk.Button(self, image=item1img, command=lambda: controller.show_frame(Item1Desc_1))
        item1.photo = item1img
        item1.grid(row=3,column=1)

        item2img = tk.PhotoImage(file='Item2/Shop.png')
        item2 = tk.Button(self, image=item2img, command=lambda: controller.show_frame(Item2Desc_1))
        item2.photo = item2img
        item2.grid(row=3,column=3)

        item3img = tk.PhotoImage(file='Item3/Shop.png')
        item3 = tk.Button(self, image=item3img, command=lambda: controller.show_frame(Item3Desc_1))
        item3.photo = item3img
        item3.grid(row=3,column=4)

        fill2=tk.LabelFrame(self, width=80, borderwidth=0, highlightthickness=0, bg="white")
        fill2.grid(row=0, column=0, rowspan=3)

        fill3=tk.LabelFrame(self, width=3, borderwidth=0, highlightthickness=0, bg="white")
        fill3.grid(row=3, column=2, rowspan=3)

        neximg = tk.PhotoImage(file='Images1024/b_next.png')
        b_next = tk.Button(self, image=neximg, text="Next Page", command=lambda: controller.show_frame(ShopPage2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_next.photo = neximg
        b_next.grid(row=4, column=3)

class ShopPage2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(5, weight=1)
        self.columnconfigure(3, weight=1)

        fill1=tk.LabelFrame(self, height=2, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=0, column=0)

        shoptitle = tk.Label(self, text="SHOP", font=('Ubuntu Condensed', 100*s), fg="pink", bg="white")
        shoptitle.grid(row=0, column=2, columnspan=2)

        
        homeimg = tk.PhotoImage(file='Images1024/homebutton.png')
        b_home = tk.Button(self,image=homeimg, command=lambda: controller.show_frame(StartPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_home.image = homeimg
        b_home.grid(row=0, column=5, sticky="ne")

        item1img = tk.PhotoImage(file='Item4/Shop.png')
        item1 = tk.Button(self, image=item1img, command=lambda: controller.show_frame(Item4Desc_1))
        item1.photo = item1img
        item1.grid(row=3,column=1)

        item2img = tk.PhotoImage(file='Item5/Shop.png')
        item2 = tk.Button(self, image=item2img, command=lambda: controller.show_frame(Item5Desc_1))
        item2.photo = item2img
        item2.grid(row=3,column=3)

        item3img = tk.PhotoImage(file='Item6/Shop.png')
        item3 = tk.Button(self, image=item3img, command=lambda: controller.show_frame(Item6Desc_1))
        item3.photo = item3img
        item3.grid(row=3,column=4)

        fill2=tk.LabelFrame(self, width=80*s, borderwidth=0, highlightthickness=0, bg="white")
        fill2.grid(row=0, column=0, rowspan=3)

        fill3=tk.LabelFrame(self, width=3, borderwidth=0, highlightthickness=0, bg="white")
        fill3.grid(row=3, column=2, rowspan=3)

        backimg = tk.PhotoImage(file='Images1024/b_back.png')
        b_back = tk.Button(self, image=backimg, text="Next Page", command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_back.photo = backimg
        b_back.grid(row=4, column=3)
#

class Item1Desc_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="B/W STRIPED BUTTON UP", font=('Ubuntu Condensed', 50*s), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item1Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item1Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item1/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20*s, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: RAW DE\nSize: Medium \nDimensions: \nFits Like: Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)
        fillR=tk.LabelFrame(self, width=40*s, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)
        
class Item1Desc_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="B/W STRIPED BUTTON UP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item1Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item1Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item1/Side.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: RAW DE\nSize: Medium \nDimensions: \nFits Like: Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)

class Item1Desc_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="B/W STRIPED BUTTON UP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item1Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item1Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item1/Back.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: RAW DE\nSize: Medium \nDimensions: \nFits Like: Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)



class Item2Desc_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="RED FLORAL TUBE TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item2Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item2Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item2/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)
        
class Item2Desc_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="RED FLORAL TUBE TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item2Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item2Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item2/Side.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)

class Item2Desc_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="RED FLORAL TUBE TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item2Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item2Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item2/Back.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)



class Item3Desc_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="GREY FUR JACKET", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item3Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item3Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item3/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: H&M\nSize: Small \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)
        
class Item3Desc_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="GREY FUR JACKET", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item3Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item3Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item3/Side.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: H&M\nSize: Small \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)

class Item3Desc_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="GREY FUR JACKET", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item3Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item3Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item3/Back.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: H&M\nSize: Small \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)

class Item4Desc_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="TEAL FLOWY TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item4Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item4Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item4/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: AMERICAN EAGLE\nSize: Medium \nDimensions: \nFits Like: Medium/Large\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)
        
class Item4Desc_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="TEAL FLOWY TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item4Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item4Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item4/Side.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: AMERICAN EAGLE\nSize: Medium \nDimensions: \nFits Like: Medium/Large\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)

class Item4Desc_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="TEAL FLOWY TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item4Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item4Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item4/Back.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: AMERICAN EAGLE\nSize: Medium \nDimensions: \nFits Like: Medium/Large\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)

class Item5Desc_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="B/W STRIPED BUTTON UP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item5Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item5Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item5/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)
        
class Item5Desc_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="B/W STRIPED BUTTON UP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item5Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item5Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item5/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)

class Item5Desc_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="B/W STRIPED BUTTON UP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item5Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item5Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item5/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)


class Item6Desc_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="B/W STRIPED BUTTON UP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item6Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item6Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item6/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)
        
class Item6Desc_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="B/W STRIPED BUTTON UP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item6Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item6Desc_3), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item6/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)

class Item6Desc_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="B/W STRIPED BUTTON UP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
        item1title.grid(row=0, column=2, columnspan=3)
        L_img = tk.PhotoImage(file='Images1024/arrowl.png')
        R_img = tk.PhotoImage(file='Images1024/arrowr.png')
        L_but=tk.Button(self,image=L_img, command=lambda: controller.show_frame(Item6Desc_2), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        L_but.photo=L_img
        L_but.grid(row=1, column=1, rowspan=8)
        R_but=tk.Button(self,image=R_img, command=lambda: controller.show_frame(Item6Desc_1), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        R_but.photo=R_img
        R_but.grid(row=1, column=3, rowspan=8)
        #image = Image.open("ClothesImages/redtop.png")
        #resized = image.resize((500, 624))
        item1img1 = tk.PhotoImage(file='Item6/Desc.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20, borderwidth=0, bg="white", highlightthickness=0)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)