from PIL import Image, ImageTk
import tkinter as tk
import os
import glob
from datetime import datetime

"""
Author: Chanon Kachorn 44456553
Honours Eye Tracker Experiment

Last modified: 20/11/2020
"""


class App(tk.Tk):
"""
	Show each images in full screen. Next image will be presented when a key is pressed <-- either p or r.
"""
    def __init__(self, image_files):
        tk.Tk.__init__(self)
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.pictures = []
        self.track_img_ndex = 0
        for img in image_files:
            self.pictures.append(img)
        self.picture_display = tk.Label(self)
        self.picture_display.pack(expand=True, fill="both")
        self.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
        self.bind("<p>",lambda event, key='p':self.write_pressed(key))
        self.bind("<r>", lambda event, key='r': self.write_pressed(key))

        file = open("userResponse.txt", "a")
        file.write('imageFileID' + ',' + 'userResponse' + ',' + 'timeTaken' + '\n')
        file.close()

        self.keyPressed = None

        self.timeNow = None


    def write_pressed(self, key):
        self.keyPressed = True
        file = open("userResponse.txt", "a")
        timeTook = str(datetime.now() - self.timeNow).split(':')[2]
        file.write(str(self.track_img_ndex) + ',' + key + ',' + timeTook + '\n')
        file.close()

        self.show_slides()

    def show_slides(self):

        self.timeNow = datetime.now()

		#write the result to a file
        if not self.keyPressed and self.keyPressed != None:
            file = open("userResponse.txt", "a")
            file.write(str(self.track_img_ndex) + ',' + '-' + ',' + str(self.delay) + '\n')
            file.close()
            file = open('read.txt', 'w')
            file.close()


        self.keyPressed = False #Reset it back


		#resize the image so that it fits with the full screen of the computer using for experiment.
        if self.track_img_ndex < len(self.pictures):
            x = self.pictures[self.track_img_ndex]
            self.track_img_ndex +=1
            original_image = Image.open(x)

            imgWidth, imgHeight = original_image.size
            if imgWidth > self.w or imgHeight > self.h:
                ratio = min(self.w / imgWidth, self.h / imgHeight)
                imgWidth = int(imgWidth * ratio)
                imgHeight = int(imgHeight * ratio)
 
            resized = original_image.resize((imgWidth, imgHeight), Image.ANTIALIAS)
            new_img = ImageTk.PhotoImage(resized)
            self.picture_display.config(image=new_img)
            self.picture_display.image = new_img
            self.title(os.path.basename(x))

        else:
            print("End of list. Experiment completed!")
            self.quit()


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '\Phishing emails\*.*' #forward slashes for Linux directory, backward slashes for windows
    image_files = glob.glob(dir_path)
    app = App(image_files)
    app.show_slides()
    app.mainloop()

