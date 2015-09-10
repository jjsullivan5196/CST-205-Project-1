import os
import struct
    
def rgb_to_hex(rgb):
  return '%02x%02x%02x' % rgb  
def hex_to_rgb(hexc):
  h1, h2, h3 = hexc[0:4], '0x' + hexc[4:6], '0x' + hexc[6:8]
  return (int(h1, 16), int(h2, 16), int(h3, 16))

pic = list()
pix = list()
picfolder = pickAFolder()

for file in os.listdir(picfolder):
  if file.endswith(".png"):
    index = len(pic)
    pic.append(makePicture(picfolder + file))
    pix.append(getAllPixels(pic[index]))
    
width = getWidth(pic[0])
height = getHeight(pic[0])

newpic = makeEmptyPicture(width, height)
newpix = getAllPixels(newpic)

for idx, pixel in enumerate(newpix):
  sample = list()
  for pixs in pix:
    color = (getRed(pixs[idx]), getGreen(pixs[idx]), getBlue(pixs[idx]))
    hexcolor = rgb_to_hex(color)
    sample.append(int(hexcolor, 16))
  mode = hex(max(set(sample), key=sample.count))
  newcolor = hex_to_rgb(mode)
  setRed(pixel, newcolor[0])
  setGreen(pixel, newcolor[1])
  setBlue(pixel, newcolor[2])

show(newpic)
  
  
  