#medianfinal.py -- Simple median filter that takes many images, converts RGB to hex color, sorts, and finds median color for each pixel in a set of similar images.
#Output is an image with all median color pixels
import os

#rgb2hex() -- takes RGB color tuple (0 - 255 range) and converts to hex triplet
#Method sourced from: http://stackoverflow.com/a/3380739
def rgb2hex(rgb):
  return '%02x%02x%02x' % rgb  

#hex2rbg() -- takes hex color triplet and converts to rgb color tuple
#Method sourced from: http://stackoverflow.com/a/4296268
def hex2rgb(hexc):
  h1, h2, h3 = hexc[0:4], '0x' + hexc[4:6], '0x' + hexc[6:8]
  return (int(h1, 16), int(h2, 16), int(h3, 16))

#avgColor() -- takes a list of hex colors in int form and averages them together into one hex triplet
def avgColor(hexc):
  r,g,b = 0,0,0
  length = len(hexc)
  for colors in hexc:
    color = hex2rgb(hex(colors))
    r += color[0]
    g += color[1]
    b += color[2]
  return rgb2hex((r/length, g/length, b/length))
  
#Main method:
def main():
  showInformation("Pick a folder with a set of visually similar images.")
  picFolder = pickAFolder()  #Choose folder with images
  pictures = list()          #Create list for pictures
  pixels = list()            #Create list for pixels of every image

  for file in os.listdir(picFolder):                                       #Iterate through directory for images
    if file.endswith((".png", ".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG")):  #Filter for image file extensions
      index = len(pictures)                                                #Keep index for pixels list
      pictures.append(makePicture(picFolder + file))                       #Append all pngs to pictures list
      pixels.append(getAllPixels(pictures[index]))                         #Append pixels for every image to pixels list
  if (len(pictures) < 2):
    showError("Did not find enough images, restart with the correct directory.")
    return false
  
  #Create a blank image with matching dimensions to write our results to
  width = getWidth(pictures[0])
  height = getHeight(pictures[0])
  newPicture = makeEmptyPicture(width, height)
  newPixels = getAllPixels(newPicture)  #Get pixels for this one too in order to edit

  #Iterate through blank image and grab matching pixels from sample images
  for idx, pixel in enumerate(newPixels):
    sample = list()  #Our sample list, one hex color in int form for the corresponding pixel from each image
    for pixs in pixels: #Iterate through all images pixel lists
      color = (getRed(pixs[idx]), getGreen(pixs[idx]), getBlue(pixs[idx])) #Grab color values from pixel corresponding to the pixel in the first for loop for each image
      hexcolor = rgb2hex(color)  #Convert color to hex
      sample.append(int(hexcolor, 16)) #Add to sample list
    #Find median color
    sample.sort() #Sort list for median
    length = len(sample) #Take length of the sample list
    if((length % 2) == 0): #Determine odd/even length. If even, average the median. If odd, pick the median. In either case, return median RGB color.
      index1 = length/2
      index2 = index1 + 1
      hexavg = avgColor([sample[index1], sample[index2]])
      newcolor = hex2rgb(hexavg)
    else:
      index = length/2
      newcolor = hex2rgb(hex(sample[index]))
    #Set the pixel to the median color determined above in newcolor
    setRed(pixel, newcolor[0])
    setGreen(pixel, newcolor[1])
    setBlue(pixel, newcolor[2])
  
  show(newPicture)
  askSave = requestString("Save new image? (Type yes or no)")
  if( askSave == 'yes' ):
    writePictureTo(newPicture, pickAFile())
  else:
    return true

main()