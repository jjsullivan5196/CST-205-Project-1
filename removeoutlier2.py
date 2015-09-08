pic1 = makePicture(pickAFile())
pic2 = makePicture(pickAFile())
replaceColor = pickAColor()

width = getWidth(pic1)
center = (width/2) - 1

pix1 = getAllPixels(pic1)
pix2 = getAllPixels(pic2)

newpic = duplicatePicture(pic1)
newpix = getAllPixels(newpic)

for pixl1,pixl2,newpixl in zip(pix1, pix2, newpix):
  origColor = getColor(pixl1)
  compColor = getColor(pixl2)
  dist = distance(origColor, compColor)
  
  if ( distance > 15 ):
    setColor(newpixl, replaceColor)

for pixl1,pixl2,newpixl in zip(pix1, pix2, newpix):
  if( getColor(newpixl) == replaceColor ):
    if( getX(newpixl) > center):
      setColor(newpixl, getColor(pixl2))
    if( getX(newpixl) < center):
      setColor(newpixl, getColor(pixl1))
    
show(newpic)