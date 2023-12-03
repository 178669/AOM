def __init__(self, main):
    # canvas for image
    self.canvas = Canvas(main, width=60, height=60)
    self.canvas.grid(row=0, column=0)

    # images
    self.my_images = []
    self.my_images.append(PhotoImage(file="ball1.gif"))
    self.my_images.append(PhotoImage(file="ball2.gif"))
    self.my_images.append(PhotoImage(file="ball3.gif"))
    self.my_image_number = 0

    # set first image on canvas
    self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.my_images[self.my_image_number])

    # button to change image
    self.button = Button(main, text="Change", command=self.onButton)
    self.button.grid(row=1, column=0)


# ----------------

def onButton(self):
    # next image
    self.my_image_number += 1

    # return to first image
    if self.my_image_number == len(self.my_images):
        self.my_image_number = 0

    # change image
    self.canvas.itemconfig(self.image_on_canvas, image=self.my_images[self.my_image_number])

def animate(self):
    if self._image_id is None:
        self._image_id = self.display.create_image(...)
    else:
        self.itemconfig(self._image_id, image= the_new_image)
    self.display.after(self.gif["delay"],