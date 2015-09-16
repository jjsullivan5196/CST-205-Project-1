#medianfinal.py -- Simple median filter that takes many images, and goes pixel-by-pixel taking each rgb value and putting them in their own tables. They are then sorted for the median colors for each pixel.
#Output is an image with all median color pixels
import os
def median(inList):
  inList.sort()
  if((len(inList) % 2) == 0):
    idx1 = len(inList)/2
    idx2 = idx1 + 1
    return (inList[idx1] + inList[idx2])/2
  else:
    index = ((len(inList) - 1)/2) + 1
    return inList[index]
    
def setColorTup(pix, inColor):
  setRed(pix, inColor[0])
  setGreen(pix, inColor[1])
  setBlue(pix, inColor[2])
  
def main():
  showInformation("Pick a folder with a set of visually similar images.")
  picFolder = pickAFolder()  #Choose folder with images
  pictures,pixels = list(),list()

  for file in os.listdir(picFolder):                        #Iterate through directory for images
    if file.endswith((".png", ".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG")):  #Filter for image file extensions
      index = len(pictures)
      pictures.append(makePicture(picFolder + file))                       #Append all pngs to pictures list
      pixels.append(getAllPixels(pictures[index]))                           #Append pixels for every image to pixels list
  if (len(pictures) < 2):  #Exception for not enough images
    showError("Did not find enough images, restart with the correct directory.")
    return false
  
  #Create a blank image with matching dimensions to write our results to
  newPicture = makeEmptyPicture(getWidth(pictures[0]), getHeight(pictures[0]))
  newPixels = getAllPixels(newPicture)  #Get pixels for this one too in order to edit

  for idx,pixel in enumerate(newPixels):
    r,g,b = list(),list(),list()  #Create rgb lists
    for pix in pixels:  #For the current pixel in every sample image, add color values to rgb lists
      r.append(getRed(pix[idx]))
      g.append(getGreen(pix[idx]))
      b.append(getBlue(pix[idx]))
    setColorTup(pixel, (median(r),median(g),median(b))) #Get the median value from each list and set it as the rgb tuple for that pixel
  
  show(newPicture)
  askSave = requestString("Save new image? (Type yes or no)")
  if( askSave == 'yes' ):
    writePictureTo(newPicture, pickAFile())
  else:
    return true

main()