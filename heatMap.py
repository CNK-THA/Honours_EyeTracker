import csv
#
# import matplotlib.pyplot as plt
# import numpy as np
# import math
#
data = []
image = []
x = []
y = []
with open('GazeReading.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    next(readCSV, None) #skip header
    for row in readCSV:
        x.append(float(row[2]))
        y.append(float(row[3]))
        if len(row) == 5: #ignoring the first one?
            image.append(x)
            image.append(y)
            data.append(image)
            image = []
            x = []
            y = []

print('hehehe')
##print(data)

            
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


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import os
import glob
##https://www.expyriment.org/

# UNUSED
# x = np.random.rayleigh(50, size=5000)
# y = np.random.rayleigh(50, size=5000)
# print(len(x))
# plt.hist2d(x,y, bins=[np.arange(0,400,5),np.arange(0,300,5)])
# fig, axl = plt.subplots(figsize=(20,20))

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Phishing emails/*.*' #forward slashes for Linux directory, backward slashes for windows
image_files = glob.glob(dir_path)
##print(image_files)

countIndex = 0
x = None
y = None

print('wer')

print(dir_path)
print(image_files)


for image in image_files:
    thisImage = data[countIndex] #gives array containing the tuple
    countIndex += 1
    x = thisImage[0]
    y = thisImage[1]
    img = Image.open(image)
    reScale1 = img.size

    x_max = max(x)
    y_max = max(y)
    reScale = (reScale1[0]/x_max, reScale1[1]/y_max)


    

    for count in range (0,len(x)):
        x[count] = x[count] * reScale[0]
        y[count] = y[count] * reScale[1]



# img2 = img.resize((np.array(img.size)/10).astype(int)) UNUSED



    plt.hist2d(x,y, bins=[np.arange(0,reScale1[0], 10),np.arange(0,reScale1[1], 10)], cmin=1)
    plt.gca().invert_yaxis()
    plt.imshow(img,  aspect ='auto')
    plt.show()
