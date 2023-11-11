import customtkinter
from tkinter import *

#customtkinter.set_appearance_mode("F59CFF")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("PinkTheme.json")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
#app.configure(bg="F59CFF")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Start a Trade", command=button_function, width=200, height=80)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()