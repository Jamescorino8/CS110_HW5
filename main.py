# James Corino
# 4 / 25 / 23
import requests
from math import *
from JES import *

#This program creates an animation. The animation consists of a boat and a shark moving through a scene that includes a moon, a sky, and water.
def createAnimation( ):
  shark = makePicture("sharkCrop.jpg")
  moon = makePicture("moon.png")
  sky = makePicture("sky.jpg")
  water = makePicture("water.jpg")
  val = 0
  
  for num in range(0, 120): #30 frames (0 to 29)
    print("Generating frame: "+str(num))
    canvas = makeEmptyPicture(300, 200)
    #Background
    copyInto(sky, canvas, 0, 0)#Sky
    copyInto(moon, canvas, 50+getWidth(canvas)//2-num//1.2, 60+getHeight(canvas)//2-num*5)#Moon
    copyInto(water, canvas, 0, getHeight(canvas)//2+20)#Water
    #Foward
    if num < 61:
      #boat
      addArcFilled(canvas, -100+num*3.4, 50, 100, 100, 180, -180, (109, 76, 65))
      addRectFilled(canvas, -100+num*3.4+45, getHeight(canvas)//2-50, 10, 50, (61, 39, 35))
      addArcFilled(canvas, -100+num*3.4, 30, 100, 100, 0, -270, white)
      
    #Backward
    if num > 60:
      #Shark
      addText(canvas, -100+val*10, -20+getHeight(canvas)//2, "GRAAAAWWWRR!", 20, (244, 67, 54))
      copyInto(shark, canvas, -100+val*10, getHeight(canvas)//2)
      #Fast boat
      addArcFilled(canvas, 100+val*9, 50, 100, 100, 180, -180, (109, 76, 65))
      addRectFilled(canvas, 100+val*9+45, getHeight(canvas)//2-50, 10, 50, (61, 39, 35))
      addArcFilled(canvas, 100+val*9, 30, 100, 100, 0, -270, white)
      val += 1
      
    # write canvas as a JPEG frame file in frames folder
    writeFrame(num, "frames", canvas)
  
  movie = makeMovieFromInitialFile("frames\\frame000.jpg");
  writeAnimatedGif(movie, "animation.gif")
  
# Don't modify this function.
# This is program 175 in Python textbook. It writes pict to
# the indicated folder using file name frameXXX.jpg, where
# XXX is num padded with leading zeros if num less than 3 digits.
def writeFrame(num, folder, pict):
  # Have to deal with single digit vs. double digit 
  numStr=str(num)
  if num < 10:
    writePictureTo(pict,folder+"/frame00"+numStr+".jpg")
  if num >= 10 and num<100:
    writePictureTo(pict,folder+"/frame0"+numStr+".jpg")
  if num >= 100:
    writePictureTo(pict,folder+"/frame"+numStr+".jpg")

createAnimation()