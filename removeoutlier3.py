pic1 = makePicture(pickAFile())
pic2 = makePicture(pickAFile())
pic3 = duplicatePicture(pic1)

pix1 = getAllPixels(pic1)
pix2 = getAllPixels(pic2)
pix3 = getAllPixels(pic3)

width = getWidth(pic1)
center = (width/2) - 1

for pixl1,pixl2,pixl3 in zip(pix1,pix2,pix3):
  if( getX(pixl1) > center):
    setColor(pixl3, getColor(pixl2))
  else:
    setColor(pixl3, getColor(pixl1))

show(pic3)
writePictureTo(pickAFile())