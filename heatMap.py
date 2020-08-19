# import csv
#
# import matplotlib.pyplot as plt
# import numpy as np
# import math
#
# x = []
# y = []
# with open('GazeReading.csv') as csvFile:
#     readCSV = csv.reader(csvFile, delimiter=',')
#     next(readCSV, None) #skip header
#     for row in readCSV:
#         x.append(float(row[2]))
#         y.append(float(row[3]))
        
#DEFINE GRID SIZE AND RADIUS(h)
# grid_size=1
# h=1
#
# #GETTING X,Y MIN AND MAX
# x_min=min(x)
# x_max=max(x)
# y_min=min(y)
# y_max=max(y)
#
# #CONSTRUCT GRID
# x_grid=np.arange(x_min-h,x_max+h,grid_size)
# y_grid=np.arange(y_min-h,y_max+h,grid_size)
# x_mesh,y_mesh=np.meshgrid(x_grid,y_grid)
#
# #GRID CENTER POINT
# xc=x_mesh+(grid_size/2)
# yc=y_mesh+(grid_size/2)
#
# #FUNCTION TO CALCULATE INTENSITY WITH QUARTIC KERNEL
# def kde_quartic(d,h):
#     dn=d/h
#     P=(15/16)*(1-dn**2)**2
#     return P
#
# #PROCESSING
# intensity_list=[]
# for j in range(len(xc)):
#     intensity_row=[]
#     for k in range(len(xc[0])):
#         kde_value_list=[]
#         for i in range(len(x)):
#             #CALCULATE DISTANCE
#             d=math.sqrt((xc[j][k]-x[i])**2+(yc[j][k]-y[i])**2)
#             if d<=h:
#                 p=kde_quartic(d,h)
#             else:
#                 p=0
#             kde_value_list.append(p)
#         #SUM ALL INTENSITY VALUE
#         p_total=sum(kde_value_list)
#         intensity_row.append(p_total)
#     intensity_list.append(intensity_row)

#HEATMAP OUTPUT    
# intensity=np.array(intensity_list)
# plt.pcolormesh(x_mesh,y_mesh,intensity)
# plt.plot(x,y,'ro')
# plt.colorbar()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image
#https://www.expyriment.org/

# UNUSED
# x = np.random.rayleigh(50, size=5000)
# y = np.random.rayleigh(50, size=5000)
# print(len(x))
# plt.hist2d(x,y, bins=[np.arange(0,400,5),np.arange(0,300,5)])
# fig, axl = plt.subplots(figsize=(20,20))


# img = Image.open("./../Pictures/Screenshot from 2020-07-13 13-35-15.png")
# reScale1 = img.size
# reScale = (reScale1[0]/x_max, reScale1[1]/y_max)
# print(reScale)
#
# for count in range (0,len(x)):
#     x[count] = x[count] * reScale[0]
#     y[count] = y[count] * reScale[1]



# img2 = img.resize((np.array(img.size)/10).astype(int)) UNUSED



# plt.hist2d(x,y, bins=[np.arange(0,reScale1[0], 5),np.arange(0,reScale1[1], 5)], cmin=1)
# plt.gca().invert_yaxis()
# plt.imshow(img,  aspect ='auto')
# plt.show()





from PIL import Image, ImageTk
import tkinter as tk
import os
#https://stackoverflow.com/questions/51066746/fullscreen-slideshow-using-python-2

import os
import glob


from datetime import datetime



class App(tk.Tk):
    def __init__(self, image_files, delay):
        tk.Tk.__init__(self)
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        #self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.delay = delay
        self.pictures = []
        self.track_img_ndex = 0
        for img in image_files:
            self.pictures.append(img)
        self.picture_display = tk.Label(self)
        self.picture_display.pack(expand=True, fill="both")
        self.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
        self.bind("<p>",lambda event, key='p':self.write_pressed(key))
        self.bind("<r>", lambda event, key='r': self.write_pressed(key))

        file = open("UserResponse.txt", "a")
        file.write('imageFileID' + ',' + 'userResponse' + ',' + 'timeTaken' + '\n')
        file.close()

        self.keyPressed = None

        self.timeNow = None


    def write_pressed(self, key):
        self.keyPressed = True
        file = open("UserResponse.txt", "a")
        timeTook = str(datetime.now() - self.timeNow).split(':')[2]
        file.write(str(self.track_img_ndex) + ',' + key + ',' + timeTook + '\n')
        file.close()
        #if timeTook >= 20.0:
        #    file.write(str(self.track_img_ndex) + ',' + '-' + ',' + str(self.delay) + '\n')
        #    file.close()
        file = open('read.txt', 'w')
        file.close()
        #else:
        

        self.show_slides()

    def show_slides(self):

        self.timeNow = datetime.now()


        #if not self.keyPressed and self.keyPressed != None:
        #    file = open("UserResponse.txt", "a")
        #    file.write(str(self.track_img_ndex) + ',' + '-' + ',' + str(self.delay) + '\n')
        #    file.close()
        #    file = open('read.txt', 'w')
        #    file.close()


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
            #self.after(self.delay, self.show_slides) #FIX THIS RUSHING FORWARD FROM PREVIOUS PRESSING.

        else:
            print("End of list. Experiment completed!")
            self.quit()




delay = 20000 #timebefore moving on no response, 20 seconds
# image_files = ["./Phishing emails/4 December CommBank Alert.jpg",
#      "./Phishing emails/051119-commbiz-phish_50split_l.png",
#      "./Phishing emails/120220-confirm-account-phish2_50split_l.png"]
dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Phishing emails/*.*' #forward slashes for Linux directory, backward slashes for windows
image_files = glob.glob(dir_path)



app = App(image_files, delay)
app.focus_set()
app.show_slides()
app.mainloop()



