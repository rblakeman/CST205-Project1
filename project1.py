# Ryan Blakeman
# CST 205
# Project1.pys
# github.com/rblakeman/CST205-Project1

from PIL import Image, ImageFilter

def medianOdd(myList):
    listLength = len(myList)
    sortedValues = sorted(myList)
    middleIndex = (int)((listLength + 1)/2) - 1
    return sortedValues[middleIndex]


theImages = list()

redPixelList = list()
greenPixelList = list()
bluePixelList = list()

try:
    for i in range(1,9):
        theImages.append(Image.open(str(i)+".png"))
except:
    print ("Failed to load")

newImage = Image.new("RGB", theImages[1].size, (255,255,255))
newImagedata = newImage.load()

print ("The size of the images are: ")
print (theImages)

pictureWidth = theImages[1].size[0]
pictureHeight = theImages[1].size[1]

for x in range(0,pictureWidth):
    for y in range(0, pictureHeight):
        for myImage in theImages:
            myRed, myGreen, myBlue = myImage.getpixel((x,y))[:3]
            # [:3] for transparancy channel
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)

        newred = medianOdd(redPixelList)
        newgreen = medianOdd(greenPixelList)
        newblue = medianOdd(bluePixelList)

        newImagedata[x,y] = (newred, newgreen, newblue)

        redPixelList.clear()
        greenPixelList.clear()
        bluePixelList.clear()

newImage.save("new.png")
