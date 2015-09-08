pictures = list()
picxels = list()
picfolder = pickAFolder()
replaceColor = pickAColor()

for x in range(0,8):
  pictures.append(makePicture(picfolder + str(x + 1) + ".png"))
  picxels.append(getAllPixels(pictures[x]))

pictureSafe = duplicatePicture(pictures[0])
picxelsSafe = getAllPixels(pictureSafe)

for x in range(1,8):
  for pix1, pix2, pixSafe in zip(picxels[0], picxels[x], picxelsSafe):
    origColor = getColor(pixSafe)
    compColor = getColor(pix2)
    dist = distance(origColor, compColor)
    if ( dist < 3):
      setColor(pix1, replaceColor)

show(pictures[0])
writePictureTo(pictures[0], pickAFile())