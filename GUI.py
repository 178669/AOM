from tkinter import *
import tkinter as tk
#
window = tk.Tk()

window.configure(bg="pink")
window.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1) #weight allows for resizing
window.geometry("800x800")


"""
home_frame = Frame(window)
home_frame.grid(row=0, column=1)
home_frame.rowconfigure(0, minsize=50, weight=1)
"""

"""
lbl_value = tk.Label(master=window, text="Start a Trade")
lbl_value.grid(row=0, column=0, columnspan=3)
"""
b_home = tk.Button(master=window, text="Back to Home", width=50)
b_home.grid(row=4, column=0, sticky="nsw")

b_start = tk.Button(master=window, text="Start a Trade", width=200)
b_start.grid(row=1, rowspan=2, column=1, columnspan=3, sticky="nsew")

btn_increase = tk.Button(master=window, text="Tokens", width=50)
btn_increase.grid(row=4, column=4, sticky="nse")



window.mainloop()