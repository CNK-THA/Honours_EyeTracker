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
        if len(row) == 5 and row[4] == 'next': #has the word next
            image.append(x)
            image.append(y)
            data.append(image)
            image = []
            x = []
            y = []



import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import os
import glob
##https://www.expyriment.org/



dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Phishing emails/*.*' #forward slashes for Linux directory, backward slashes for windows
image_files = glob.glob(dir_path)
##print(image_files)

countIndex = 0
x = None
y = None



for image in image_files:
    thisImage = data[countIndex] #gives array containing the tuple
    countIndex += 1
    x = thisImage[0]
    y = thisImage[1]
    img = Image.open(image)
    reScale1 = img.size

    x_max = max(x)
    y_max = max(y)
    print('max x', x_max)
    print('max y', y_max)

    print(reScale1, 'image size')

    for count in range (0,len(x)):

        x[count] = x[count] * reScale1[0]
        y[count] = y[count] * reScale1[1]




    plt.hist2d(x,y, bins=[np.arange(0,reScale1[0], 10),np.arange(0,reScale1[1], 10)], cmin=7) #5 is how large the dots are, cmin is the area of interest
    plt.gca().invert_yaxis()
    plt.imshow(img,  aspect ='auto')
    plt.show()
