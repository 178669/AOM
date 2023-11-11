from tkinter import *
import tkinter as tk
"""
window = tk.Tk()

window.configure(bg="pink")
window.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1) #weight allows for resizing
window.geometry("800x800")
"""
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
        for F in (StartPage, Page1, Page2):
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
        self.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=10, weight=1)
        self.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=0, weight=1) #weight allows for resizing

        b_startimg = tk.PhotoImage(file='images/b_pink.png')
        img_label = tk.Label(self, image=b_startimg)
        #img_label.photo = b_startimg
        #img_label.pack()


        #b_start = tk.Button(self, text="Start a Trade", width=200, command=lambda:controller.show_frame(Page1))
        b_start = tk.Button(self, image=b_startimg, command=lambda: controller.show_frame(Page1), borderwidth=0, bg="white", activebackground="white")
        b_start.photo = b_startimg
        b_start.grid(row=3, rowspan=1, column=3, columnspan=3, sticky="nsew")

        RENT_CLOTHES = tk.Label(self, text="TRADE CLOTHES", bg="white", fg="pink", font=('Gloucester MT Extra Condensed', 275))
        RENT_CLOTHES.grid(row=2, column=3, columnspan=3)

"""
        b_startimg = tk.PhotoImage(file='images/startbutton.png')
        img_label = tk.Label(image=b_startimg) 
"""




class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


"""
home_frame = Frame(window)
home_frame.grid(row=0, column=1)
home_frame.rowconfigure(0, minsize=50, weight=1)
"""

"""
lbl_value = tk.Label(master=window, text="Start a Trade")
lbl_value.grid(row=0, column=0, columnspan=3)

b_home = tk.Button(master=window, text="Back to Home", width=50)
b_home.grid(row=4, column=0, sticky="nsw")

b_start = tk.Button(master=window, text="Start a Trade", width=200)
b_start.grid(row=1, rowspan=2, column=1, columnspan=3, sticky="nsew")

btn_increase = tk.Button(master=window, text="Tokens", width=50)
btn_increase.grid(row=4, column=4, sticky="nse")
"""

app = startApp()
app.geometry("1920x1080")
app.mainloop()