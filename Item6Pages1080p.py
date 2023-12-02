import tkinter as tk
from Pages1080p import *


class Item6Desc_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(4, weight=1)
        item1title = tk.Label(self, text="RED FLORAL TUBE TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
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
        item1img1 = tk.PhotoImage(file='ClothesImages1024/redtopdup.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
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
        item1title = tk.Label(self, text="RED FLORAL TUBE TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
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
        item1img1 = tk.PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
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
        item1title = tk.Label(self, text="RED FLORAL TUBE TOP", font=('Ubuntu Condensed', 50), fg="pink", bg="white")
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
        item1img1 = tk.PhotoImage(file='ClothesImages1024/redtopback.png')
        #item1img2 = PhotoImage(file='ClothesImages1024/redtopside.png')
        #item1img3 = PhotoImage(file='ClothesImages1024/redtopback.png')
        item1 = tk.Label(self, image=item1img1)
        item1.photo = item1img1
        item1.grid(row=1,column=2, rowspan=8)
        filltopinfo = tk.LabelFrame(self, height=20)
        filltopinfo.grid(row=1, column=4)
        info = tk.Label(self, text="Brand: Forever21\nSize: Medium \nDimensions: \nFits Like: Small/Medium\n", font=('Ubuntu Condensed', 35), fg="pink", bg="white")
        info.grid(row=2, column=4, rowspan=3)
        rentimg = tk.PhotoImage(file='Images1024/b_purchase.png')
        allimg = tk.PhotoImage(file='Images1024/b_all.png')
        b_rent = tk.Button(self, image=rentimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_all = tk.Button(self, image=allimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)      
        b_rent.photo = rentimg
        b_all.photo = allimg
        b_rent.grid(row=5, column=4)
        b_all.grid(row=6, column=4)
        fillL=tk.LabelFrame(self, width=1, borderwidth=0, highlightthickness=0, bg="white")
        fillL.grid(column=0)  
        fillR=tk.LabelFrame(self, width=40, borderwidth=0, highlightthickness=0, bg="white")
        fillR.grid(column=5)