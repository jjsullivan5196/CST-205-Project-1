#marksimilarities.py -- marks similarlly colored pixels bewteen a few images
#Create lists for images and individual pixels of those images
pictures = list()
picxels = list()

#Ask user for folder and replacement color for similarities
picfolder = pickAFolder()
replaceColor = pickAColor()

#Populate picture and pixel lists
for x in range(0,8):
  pictures.append(makePicture(picfolder + str(x + 1) + ".png"))
  picxels.append(getAllPixels(pictures[x]))

#Create a safe copy of the first image to compare against
pictureSafe = duplicatePicture(pictures[0])
picxelsSafe = getAllPixels(pictureSafe)

#Iterate through images and compare
for x in range(1,8):
  #Three set iteration for first image, test image, and the safe copy
  for pix1, pix2, pixSafe in zip(picxels[0], picxels[x], picxelsSafe):
    origColor = getColor(pixSafe) #Color of pixel from safe image
    compColor = getColor(pix2) #Color of pixel from test image
    dist = distance(origColor, compColor) #Distance of color
    if ( dist < 9):
      setColor(pix1, replaceColor)

#Show and write results
show(pictures[0])
writePictureTo(pictures[0], pickAFile())