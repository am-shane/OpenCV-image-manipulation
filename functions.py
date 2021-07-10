from __future__ import print_function
import cv2
import tkinter as tk
import imghdr
from tkinter import filedialog
from tkinter import ttk  
import numpy as np
from builtins import input
largeFont= ("Verdana", 24)
normalFont = ("Calibri", 16)
smallFont = ("Calibri", 12)

######################### misc functions ######################################
'''saves the image'''
def save(img, ext, itCheck):
    if itCheck == 1:
        img = cv2.imread("temp.png")
    if itCheck == 0:
        img = img
    print("\n choose where to save your image using the file browser")
    save = filedialog.asksaveasfile() #open save file dialog
    #print(str(save))
    save = str(save) #saves location as a string
    save = save[25:-29] #pulls only the information needed (location/name)
    print("saving to: ", save)
    cv2.imwrite((str(save)+"."+str(ext)), img) #adds correct file extention and saves to chosen location
    print("save completed")
########################################################
    
##def checkComplete():
##    checker = 0

########################################################
    
'''creates a popup box with message, title, and button headings of choice'''
def popUp(msg, title, button):
    pop = tk.Tk()
    pop.wm_title(title)
    label = ttk.Label(pop, text=msg, font=normalFont)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(pop, text=button, command = pop.destroy)
    B1.pack()

######################################################
    
'''runs the appropriate function based on user choice'''
def funcChoose(operation, img, itCheck):
    if itCheck == 1:
        img = cv2.imread("temp.png")
    if itCheck == 0:
        img = img
    if operation == "1":
        anaglyph(img)
    if operation == "2":
        binary(img)
    if operation == "3":
        pyramid(img)
    if operation == "4":
        greyscale(img)
    if operation == "5":
        keypoints(img)
    if operation == "6":
        colorInvert(img)
    if operation == "7":
        resize(img)
    if operation == "8":
        removeChannel(img)
    if operation == "9":
        saturation(img)
    if operation == "10":
        flip(img)
        
############################################################################

########################## image processing functions ########################################
'''creates an anaglyph'''
def anaglyph(img):
    img1 = img
    img2 = img
    shift = int(input("what should the shift value (how much it 'pops') of the anaglyph be? \n 5-15 yields best results: ")) 

    #get width
    w = img1.shape[1]
    #get height
    h = img1.shape[0]

    ana = np.zeros((h,w + (shift),3),np.uint8)
    hCount = 0
    while hCount < h:
        #iterate through all rows
            #iterate through all pixels in the row
        wCount = 0
        while wCount < w:
            ana[hCount][wCount][2] = img1[hCount][wCount][2]
                #copys red channel
            
            ana[hCount][wCount + shift][0] = img2[hCount][wCount][0]
            ana[hCount][wCount + shift][1] = img2[hCount][wCount][1]
                #copy the blue and green channels
                #accounts for shift value
            wCount += 1
        hCount += 1
    cv2.imwrite("temp.png", ana)
    img = cv2.imread("temp.png")
    cv2.imshow("anaglyph!", img) #shows image
    print("operation complete! Conversion to anaglyph successful.")

#################################################
'''creates binary image'''    
def binary(img):
    greyscale(img)

    upperBound = int(input("enter the upper boundary of a threshhold from 0 to 255:  "))
    lowerBound = int(input("enter the lower boundary of a threshhold from 0 to 255:  "))
    #uper enters upper and lower boundaries for a color threshold
    print("your inputed threshold is from", lowerBound, "to", upperBound)
    w = img.shape[1]
    #get the height of image
    h = img.shape[0]
    # iterate though all the rows in the image
    hCount = 0
    while hCount < h:
        #iterate through all the pixels in one row
        wCount = 0
        while wCount < w:
            one = int(img[hCount][wCount][0])
            two = int(img[hCount][wCount][1])
            three = int(img[hCount][wCount][2])
            if one > upperBound:
                img[hCount][wCount][0] = int(255)
            elif one < lowerBound:
                img[hCount][wCount][0] = int(0)
            if two > upperBound:
                img[hCount][wCount][1] = int(255)
            elif two < lowerBound:
                img[hCount][wCount][1] = int(0)
            if three > upperBound:
                img[hCount][wCount][2] = int(255)
            elif three < lowerBound:
                img[hCount][wCount][2] = int(0)
            wCount += 1
        hCount += 1
    cv2.imwrite("temp.png", img)
    img = cv2.imread("temp.png")
    cv2.imshow("binary img", img) #shows image
    print("operation complete! Conversion to binary successful")

############################################
''' creates an image pyramid '''    
def pyramid(img):
    number = int(input("enter a number of levels to build for the image pyramid: "))
    runs = 0
    condition = True
    while condition == True:
        w = img.shape[1]
        h = img.shape[0]
        newW = int(w/2)
        newH = int(h/2)
        smallerImg = cv2.resize(img, (newW, newH))
        ##smallerImg = cv2.resize(orginal image, (width, height))
        secondimg = "number pyramid" + str(runs)
        cv2.imshow(secondimg, smallerImg)
        runs = (runs + 1)
        img = smallerImg
        if runs == number:
            condition = False
    print("operation complete! Image pyramid is displayed")

##########################################
''' creates a greyscale image '''            
def greyscale(img):
    #get width
    w = img.shape[1]
    #get the height
    h = img.shape[0]
    # iterate though all the rows
    hCount = 0
    while hCount < h:
        #iterate pixels in row
        wCount = 0
        while wCount < w:
            one = int(img[hCount][wCount][0])
            two = int(img[hCount][wCount][1])
            three = int(img[hCount][wCount][2])
            img[hCount][wCount][0] = int((one+two+three)/3)
            img[hCount][wCount][1] = int((one+two+three)/3) #averages each of the 3 RBG integers together to form greyscale
            img[hCount][wCount][2] = int((one+two+three)/3)
            wCount += 1
        hCount += 1
    cv2.imwrite("temp.png", img)
    img = cv2.imread("temp.png")
    print("operation complete! Conversion to greyscale successful")
    cv2.imshow("greyscale image", img)
###############################################
''' finds keypoints of the image '''    
def keypoints(img):
    image = img
    OGimage = img
    numLevels = 1 # number of image resolutions to get features from
    numBlurs = 3 # number of times to get a Difference
    for i in range(numLevels):
        #list to store all the Differences for the level
        imgList = []
        for j in range(numBlurs):
            # blur image
            image2 = cv2.GaussianBlur(image, (15,15), 0)
            # subtract from prior image
            sub = abs(image-image2)
            # save Diff
            imgList.append(sub)
            # Display result
            image = image2
        w = imgList[1].shape[1] #gets width and height
        h = imgList[1].shape[0]
        xVals = [] #create empty list for x and y coordinates
        yVals = []
        hCount = 0
        while hCount < (h-1):
            wCount = 0
            while wCount < (w-1):
                avgList = [] #create empty list for averages found below
                for x in range (-1,2):
                    for y in range (-1,2): #total of 9 loops
                        red0 = float(imgList[0][hCount+x][wCount+y][0])
                        green0 = float(imgList[0][hCount+x][wCount+y][1])
                        blue0 = float(imgList[0][hCount+x][wCount+y][2])
                        a0 = (red0+green0+blue0)/3 #averages each 
                        avgList.append(a0) #appends average to list of averages
                        red1 = float(imgList[1][hCount+x][wCount+y][0])
                        green1 = float(imgList[1][hCount+x][wCount+y][1])
                        blue1 = float(imgList[1][hCount+x][wCount+y][2])
                        a1 = (red1+green1+blue1)/3 #average each
                        avgList.append(a1) #appends average to list of averages
                        red2 = float(imgList[2][hCount+x][wCount+y][0])
                        green2 = float(imgList[2][hCount+x][wCount+y][1])
                        blue2 = float(imgList[2][hCount+x][wCount+y][2])
                        a2 = (red2+green2+blue2)/3 #average each
                        avgList.append(a2) #appends average to list of averages
                redCord = float(imgList[1][hCount][wCount][0])
                greenCord = float(imgList[1][hCount][wCount][1])
                blueCord = float(imgList[1][hCount][wCount][2])
                centerC = (redCord+greenCord+blueCord)/3 #finds averages of each and assigns result to centerC
                if centerC == min(avgList) or centerC == max(avgList):
                    xVals.append(wCount) #appends wcount and hcount to respective list of coordinates
                    yVals.append(hCount)  
                wCount += 1
            hCount += 1
        for i in range(len(xVals)):
            cv2.circle(OGimage,(xVals[i],yVals[i]),1,(240,0,0),-1) #circles keypoints in blue using found coordinates, in blue
            cv2.imshow("Keypoints (blue areas)",OGimage)#shows final image with keypoints circled
        newH = int(image.shape[0]*0.5)
        newW = int(image.shape[1]*0.5)
        image = cv2.resize(image, (newW, newH))
        print("operation complete! Keypoints have been found.")
#####################################################
''' inverts colors / creates negative image '''        
def colorInvert(img):
    img = cv2.bitwise_not(img)
    print("color invert")
    cv2.imwrite("temp.png", img)
    img = cv2.imread("temp.png")
    cv2.imshow("color inverted image",img)
    print("operation complete! Colors of the image have been inverted.")

####################################################
''' resizes image '''
 
def resize(img):
    print("do you want to manually resize the image (input desired resolution), or resize by scaling up or down?")
    resizeType = input("manually: input 1 \n scaling: input 2 \n 1 or 2?: ")
    if resizeType == "1":
        #allows user to manually choose new resolution
        height, width = img.shape[:2]
        print("current height: ", height)
        print("current width: ", width)
        newHeight = float(input("input your new height: "))
        newWidth = float(input("input your new width: "))
        if newHeight > height:
            x = float(newHeight / height)
        if newHeight < height:
            x = float(newHeight / height)
        if newWidth > width:
            y = float(newWidth / width)
        if newWidth < width:
            y  = float(newWidth / width)
        img = cv2.resize(img, None, fx = x, fy = y, interpolation = cv2.INTER_CUBIC)
        cv2.imshow("resized image", img)
       #user can resize by a ratio 
    if resizeType == "2":
        x = float(input("what ratio would you like to resize the image to (ex. 0.1, 0.5, 1.5, 2): "))
        img = cv2.resize(img, None, fx = x, fy = x, interpolation = cv2.INTER_CUBIC)
        cv2.imshow("resized image", img)
    elif resizeType != "1" or resizeType != "2":
        print("you must choose 1 or 2")
        resize(img)
    cv2.imwrite("temp.png", img)
    img = cv2.imread("temp.png")
    print("operation complete! Image has been resized.")

#########################################################
''' removes chosen color channel (red, blue, or green) '''

def removeChannel(img):
    print("check")
    colorToRemove = input("what color channel would you like to remove (red,blue,green)?:")
    if colorToRemove == "red":
        img[:,:,2] = np.zeros([img.shape[0], img.shape[1]])#gives all red channels value of 0
        cv2.imshow('red channel removed',img)
        print("red channel has been removed")
    if colorToRemove == "blue":
        img[:,:,0] = np.zeros([img.shape[0], img.shape[1]])#gives all blue channels value of 0
        cv2.imshow('blue channel removed',img)
        print("blue channel has been removed")

    if colorToRemove == "green":
        img[:,:,1] = np.zeros([img.shape[0], img.shape[1]])#gives all green channels value of 0
        cv2.imshow('green channel removed',img)
        print("green channel has been removed")
    cv2.imwrite("temp.png", img)
    img = cv2.imread("temp.png")

#################################################################
''' changes saturation by adjusting contrast and brightness'''

def saturation(img):
    image = img
    new_image = np.zeros(image.shape, image.dtype)
    alpha = 1.0 #contrast control
    beta = 0    # brightness control
    try:
        alpha = float(input("Enter the alpha(contrast) value 1.0-3.0:"))
        beta = int(input("Enter the beta (brightness) value 0-100:"))
    except ValueError:
        print("enter a valid number within the values listed")
    #new_image(i,j) = alpha * image(i,j) + beta
    for y in range(image.shape[0]): #iterate through pixels
        for x in range(image.shape[1]):
            for z in range(image.shape[2]):
                new_image[y,x,z] = np.clip(alpha*image[y,x,z] + beta, 0, 255) #adjust acoding to the new values
    img = new_image
    cv2.imwrite("temp.png", img)
    img = cv2.imread("temp.png")
    cv2.imshow("adjusted saturation", img)
    print("saturation has been adjusted")

######################################################################
'''flips the image on x or y axis'''

def flip(img):
    print("do you want to flip the image on \n the X-axis: 1 \n the Y-axis: 2")
    XorY = str(input("choose 1 or 2:"))
    if XorY == "1":
        ogimg = img
        newimg = cv2.flip(ogimg, 0)
        img = newimg
        cv2.imshow("X-axis flipped", img)
    elif XorY == "2":
        ogimg = img
        newimg = cv2.flip(ogimg, 1)
        img = newimg
        cv2.imshow("Y-axis flipped", img)
    else:
        print("Invalid number")
        flip(img)
    cv2.imwrite("temp.png", img)
    img = cv2.imread("temp.png")
    
        


