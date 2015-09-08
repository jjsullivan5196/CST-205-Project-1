showInformation("Pick two images, each with the undesired abberation on one side of the frame.\nFirst image with abberation on the RIGHT side of the frame.\nSecond image with abberation on the LEFT side of the frame.")
#Ask user for two pictures, one with the abberation on each side of the frame. Create a copy of the first image to modify.
pic1 = makePicture(pickAFile())
pic2 = makePicture(pickAFile())
pic3 = duplicatePicture(pic1)

#List pixels for each.
pix1 = getAllPixels(pic1)
pix2 = getAllPixels(pic2)
pix3 = getAllPixels(pic3)

#Find the vertical center
width = getWidth(pic1)
center = (width/2) - 1

#Transpose pixels from each side of the image over to the other, so that the abberation is removed.
for pixl1,pixl2,pixl3 in zip(pix1,pix2,pix3):
  if( getX(pixl1) > center):
    setColor(pixl3, getColor(pixl2))
  else:
    setColor(pixl3, getColor(pixl1))

show(pic3)
writePictureTo(pic3,pickAFile())