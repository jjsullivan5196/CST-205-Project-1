#medianfinal.py -- Simple median filter that takes many images, converts RGB to hex color, sorts, and finds median color for each pixel in a set of similar images.
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

  for file in os.listdir(picFolder):                                       #Iterate through directory for images
    if file.endswith((".png", ".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG")):  #Filter for image file extensions
      index = len(pictures)                                                #Keep index for pixels list
      pictures.append(makePicture(picFolder + file))                       #Append all pngs to pictures list
      pixels.append(getAllPixels(pictures[index]))                         #Append pixels for every image to pixels list
  if (len(pictures) < 2):
    showError("Did not find enough images, restart with the correct directory.")
    return false
  
  #Create a blank image with matching dimensions to write our results to
  newPicture = makeEmptyPicture(getWidth(pictures[0]), getHeight(pictures[0]))
  newPixels = getAllPixels(newPicture)  #Get pixels for this one too in order to edit

  for idx,pixel in enumerate(newPixels):
    r,g,b = list(),list(),list()
    for pix in pixels:
      r.append(getRed(pix[idx]))
      g.append(getGreen(pix[idx]))
      b.append(getBlue(pix[idx]))
    setColorTup(pixel, (median(r),median(g),median(b)))
  
  show(newPicture)
  askSave = requestString("Save new image? (Type yes or no)")
  if( askSave == 'yes' ):
    writePictureTo(newPicture, pickAFile())
  else:
    return true

main()