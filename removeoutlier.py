pictures = list()
picxels = list()
picfolder = pickAFolder()
replaceColor = pickAColor()

for x in range(0,8):
  pictures.append(makePicture(picfolder + str(x + 1) + ".png"))
  picxels.append(getAllPixels(pictures[x]))

for x in range(1,8):
  for pix1, pix2 in zip(picxels[0], picxels[x]):
    if( getColor(pix1) == getColor(pix2) ):
      setColor(pix1, replaceColor)

show(pictures[0])
writePictureTo(pictures[0], pickAFile())