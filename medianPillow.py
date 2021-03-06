#medianPillow.py -- Same method as medianfinal.py but using Python 3 and the Pillow PIL-fork
#*NOTE: the .show() method works fine on Mac/Win, requires xv installed on linux. Install xv if you don't see an image.
import os, sys
from statistics import median
import tkinter as tk
from tkinter.filedialog import askdirectory,asksaveasfilename
from tkinter.messagebox import showinfo,showwarning,showerror,askquestion
from PIL import Image

def main():
    root = tk.Tk()
    root.withdraw()
    showinfo('Median Filter', 'Select a directory with visually similar images') #Ask user for image directory
    picDir = askdirectory()
    pixels = list()
    tempPic = 0

    for file in os.listdir(picDir): #Populate lists
        if file.endswith((".png", ".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG")):
            tempPic = Image.open(picDir + os.sep + file)
            pixels.append(tempPic.getdata())
    if(len(pixels) < 2): #Not enough images exception
        showerror('Error', 'Not enough images. Please restart with the correct directory')
        return false

    newPicture = Image.new(tempPic.mode, tempPic.size) #Create new picture with matching dimensions
    newPixels = list(newPicture.getdata())

    for idx, pixel in enumerate(newPixels): #The medianfinal method, the Pillow way
        r,g,b = list(),list(),list()
        for pix in pixels:
            r.append(pix[idx][0])
            g.append(pix[idx][1])
            b.append(pix[idx][2])
        newPixels[idx] = (int(median(r)),int(median(g)),int(median(b)))

    newPicture.putdata(newPixels)
    newPicture.show()
    askSave = askquestion('Save', 'Would you like to save the new image?', icon='info')
    if(askSave == 'yes'):
        fileName = asksaveasfilename()
        newPicture.save(fileName)
        return true
    else:
        return true

main()