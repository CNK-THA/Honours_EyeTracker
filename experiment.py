from PIL import Image, ImageTk
import tkinter as tk
import os
#https://stackoverflow.com/questions/51066746/fullscreen-slideshow-using-python-2

import os
import glob


from datetime import datetime



class App(tk.Tk):
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


        if not self.keyPressed and self.keyPressed != None:
            file = open("userResponse.txt", "a")
            file.write(str(self.track_img_ndex) + ',' + '-' + ',' + str(self.delay) + '\n')
            file.close()
            file = open('read.txt', 'w')
            file.close()


        self.keyPressed = False #Reset it back



        if self.track_img_ndex < len(self.pictures):
            x = self.pictures[self.track_img_ndex]
            self.track_img_ndex +=1
            original_image = Image.open(x)

            imgWidth, imgHeight = original_image.size
            if imgWidth > self.w or imgHeight > self.h:
                ratio = min(self.w / imgWidth, self.h / imgHeight)
                imgWidth = int(imgWidth * ratio)
                imgHeight = int(imgHeight * ratio)
                #pilImage = pilImage.resize((imgWidth, imgHeight), Image.ANTIALIAS)


            #resized = original_image.resize((self.w, self.h),Image.ANTIALIAS)
            resized = original_image.resize((imgWidth, imgHeight), Image.ANTIALIAS)
            new_img = ImageTk.PhotoImage(resized)
            self.picture_display.config(image=new_img)
            self.picture_display.image = new_img
            self.title(os.path.basename(x))
##            self.after(self.delay, self.show_slides) #FIX THIS RUSHING FORWARD FROM PREVIOUS PRESSING.

        else:
            print("End of list. Experiment completed!")
            self.quit()


if __name__ == "__main__":

    while(True):
        input('Image file opened, ready to begin experiment!!')
        break
    
##    delay = 20000 #timebefore moving on no response, 20 seconds
    # image_files = ["./Phishing emails/4 December CommBank Alert.jpg",
    #      "./Phishing emails/051119-commbiz-phish_50split_l.png",
    #      "./Phishing emails/120220-confirm-account-phish2_50split_l.png"]


#THESE ARE REAL
##    dir_path = os.path.dirname(os.path.realpath(__file__)) + '\Phishing emails\*.*' #forward slashes for Linux directory, backward slashes for windows
##    image_files = glob.glob(dir_path)

#NOT THESE
##    print(image_files)
##    for file in image_files:
##        print(file.split('\\')[5])

#THESE ARE REAL AS WELL
##    app = App(image_files)
##    app.show_slides()
##    app.mainloop()

