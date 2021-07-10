'''PROGRAM ONLY FUNCTIONAL ON WINDOWS OPERATING SYSTEMS'''
import cv2
import tkinter as tk
import imghdr
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import ttk  
import numpy as np
import os
import functions
itCheck = 0
funcChooseNumList = ["1","2","3","4","5","6","7","8","9","10"] #list of potential choices
#########################################################################################################

extList = ["rgb","pbm","pgm","tiff","rast","xbm","jpeg","bmp","png","jpg","tif"]
 #list of appropriate image extentions   
print("this program allows you to perform a variety of image processing operations")
print("select your image through the file browser \n")

root = tk.Tk()
root.withdraw() #opens file browser for user to choose an image
filePath = filedialog.askopenfilename()

ext = imghdr.what(filePath) #finds the type of file extension

valid = False
while valid == False:
    if ext in extList: #checks if file choosen is in list of correct image extensions
        print("image choosen is a valid file type", "(", ext, ") \n")
        valid = True
    else:
        print("not a valid filetype, please choose a different image \n")
        #popUp("not a valid filetype", "error", "ok")
        root = tk.Tk() #promps user to choose a different image if incorrect type
        root.withdraw()
        filePath = filedialog.askopenfilename()
        ext = imghdr.what(filePath)
        
print("you have choosen: ", filePath)
print("\n each operation can be performed by inputing the corresponding letter")
print("\n the list of potential options are as follows: ")
print("create an anaglyph: 1 \n create a binary image: 2 \n create a image pyramid: 3 \n convert the image to greyscale: 4 \n find the keypoints of the image: 5 \n invert the colors of the image: 6 \n resize the image: 7 \n remove specific color channel from image: 8 \n adjust the saturation of the image: 9 \n flip the image on X or Y axis: 10 \n ")
operation = input("\n what operation would you like to perform? Choose a corresonding number 1-10:")
while operation not in funcChooseNumList: #loops until user chooses an image
    print("choose a number 1-10")
    operation = input("\n what operation would you like to perform? Choose a corresonding number 1-10:")


img = cv2.imread(filePath)
functions.funcChoose(operation, img, itCheck)#passes operation and img to functions module
print(" \n view your edited image and press any key to continue \n \n")
cv2.waitKey(0)

def repeat(img, ext, itCheck):
    cv2.destroyAllWindows() #closes image to prepare for creating another
    print("would you like to perform another function?")
    print("\n options are as follows: \n start again with a new image: 1 \n perform another function on the current image: 2 \n save the current image: 3 \n QUIT: 4") 
    anotherChoice = input("enter the corresponding number of the action you would like to take:")
    if anotherChoice == "1":
        try: 
            os.remove("temp.png")
        except:
            pass
        itCheck = 0
        print("select your image through the file browser \n")

        root = tk.Tk()
        root.withdraw() #opens file browser for user to choose an image
        filePath = filedialog.askopenfilename()

        ext = imghdr.what(filePath) #finds the type of file extension

        valid = False
        while valid == False:
            if ext in extList: #checks if file choosen is in list of correct image extensions
                print("image choosen is a valid file type", "(", ext, ") \n")
                valid = True
            else:
                print("not a valid filetype, please choose a different image \n")
                #popUp("not a valid filetype", "error", "ok")
                root = tk.Tk() #promps user to choose a different image if incorrect type
                root.withdraw()
                filePath = filedialog.askopenfilename()
                ext = imghdr.what(filePath)
                
        print("you have choosen: ", filePath)
        print("\n each operation can be performed by inputing the corresponding letter")
        print("create an anaglyph: 1 \n create a binary image: 2 \n create a image pyramid: 3 \n convert the image to greyscale: 4 \n find the keypoints of the image: 5 \n invert the colors of the image: 6 \n resize the image: 7 \n remove specific color channel from image: 8 \n adjust the saturation of the image: 9 \n flip the image on X or Y axis: 10 \n ")
        operation = input("\n what operation would you like to perform? Choose a corresonding number 1-10:")
        while operation not in funcChooseNumList: #loops until user chooses an image
            print("choose a number 1-10")
            operation = input("\n what operation would you like to perform? Choose a corresonding number 1-10:")


        img = cv2.imread(filePath)
        functions.funcChoose(operation, img, itCheck)#passes operation and img to functions module
        print(" \n view your edited image and press any key to continue \n \n")
        cv2.waitKey(0)
        
        repeat(img, ext, itCheck)

    elif anotherChoice == "2":
        itCheck = 1
        print("\n each operation can be performed by inputing the corresponding letter")
        print("\n the list of potential options are as follows: ")
        print("create an anaglyph: 1 \n create a binary image: 2 \n create a image pyramid: 3 \n convert the image to greyscale: 4 \n find the keypoints of the image: 5 \n invert the colors of the image: 6 \n resize the image: 7 \n remove specific color channel from image: 8 \n adjust the saturation of the image: 9 \n flip the image on X or Y axis: 10 \n ")
        operation = input("\n what operation would you like to perform? Choose a corresonding number 1-10:")
        while operation not in funcChooseNumList: #loops until user chooses an image
            print("choose a number 1-10")
            operation = input("\n what operation would you like to perform? Choose a corresonding number 1-10:")

        functions.funcChoose(operation, img, itCheck)#passes operation and img to functions module
        print(" \n view your edited image and press any key to continue \n \n")
        cv2.waitKey(0)

        repeat(img, ext, itCheck)
    elif anotherChoice == "3":
        functions.save(img, ext, itCheck)
        repeat(img, ext, itCheck)
    elif anotherChoice == "4":
        try: 
            os.remove("temp.png")
        except: pass
        exit()
    else:
        print("invalid Input, choose a number 1-4")
        repeat(img, ext, itcheck)

repeat(img, ext, itCheck)



