#Authors: Joshua Howard, Eric Ybarra, Mercedes Garcia, William Barajas

#CST 205 Final Project
#testing 1,2,3

#IMPORTANT!!
#ENTER YOUR IMAGE LOCATIONS HERE!!
desertOasisImage = 'C:\Users\AlexS\cst205_Final\Images\desert_oasis.jpg'
elephantImage = 'C:\Users\AlexS\cst205_Final\Images\elephant.jpg'
lushJungleImage = 'C:\Users\AlexS\cst205_Final\Images\lush_jungle.jpg'
monkeyImage = 'C:\Users\AlexS\cst205_Final\Images\monkey.jpg'
lostForestImage = 'C:\Users\AlexS\cst205_Final\Images\lost_forest.jpg'
bearImage = 'C:\Users\AlexS\cst205_Final\Images\bear.jpg'
wildSaharaImage = 'C:\Users\AlexS\cst205_Final\Images\wild_sahara.jpg'
lionImage = 'C:\Users\AlexS\cst205_Final\Images\lion.jpg'
mapOverlayImage = 'C:\Users\AlexS\cst205_Final\Images\map_overlay.jpg'

canvas = makeEmptyPicture(800,600)
desertOasis = makePicture(desertOasisImage)
elephant = makePicture(elephantImage)
lushJungle = makePicture(lushJungleImage)
monkey = makePicture(monkeyImage)
lostForest = makePicture(lostForestImage)
bear = makePicture(bearImage)
wildSahara = makePicture(wildSaharaImage)
lion = makePicture(lionImage)
mapOverlay = makePicture(mapOverlayImage)

#just a random add picture function
def addPic():
  return makePicture(pickAFile())
  
#shows the initial map  
def makeMap():  
  copyInto(desertOasis, canvas, 0, 0)   
  copyInto(lushJungle, canvas, 400, 0)   
  copyInto(lostForest, canvas, 0, 300)
  copyInto(wildSahara, canvas, 400, 300)   
  chromakeyLoc(mapOverlay, canvas, 0, 0, "red")
  repaint(canvas)
  
#not working yet 
def addAnimalPic(animal):
  if animal == "elephant":
    copyInto(elephant, canvas, 30, 30)
  repaint(canvas)
  

#enter the source picture that has the background color that you want to emit that you want to add over the target picture at the target x and y location.
#enter "red" or "green" for the sourceBgColor   
def chromakeyLoc(sourcePic, targetPic, targetX, targetY, sourceBgColor):
  for x in range(0, getWidth(sourcePic)):
    for y in range(0, getHeight(sourcePic)):
      p = getPixel(sourcePic,x,y)
      sourceColor = getColor(p)
      #if the background is red
      if sourceBgColor == "red" and getGreen(p) + getBlue(p) < getRed(p):
        continue
      else:      
        setColor(getPixel(targetPic, x+targetX, y+targetY), sourceColor)
      #if the background is green
      if sourceBgColor == "green" and getRed(p) + getBlue(p) < getGreen(p):
        continue
      else:      
        setColor(getPixel(targetPic, x+targetX, y+targetY), sourceColor)
  return targetPic

def playAnySound():
  file = pickAFile()
  sound = makeSound(file)
  play(sound)
def guesses(): #This function should keep track of the number of guesses the user has
  #global guesses = 4
  showInformation("You have x number of guesses")  

def end(userInput):#The purpose of this function is to quit the game if the user were to input "exit".
  while(userInput == "exit"):
    if(userInput == "exit"):
      print ""
      printNow ("  Done.")
      break  

def userInput(): #This function will allow the user to traverse the zoo from differenct areas(1-4)
  userInput = requestString("What area would you like to go? ")
  printNow(userInput)
  end(userInput)#Will end/exit game
  if(userInput == "help"):#Will re-start game and provide instructions.
    zooGame() 
    printNow(userInput)  
  if(userInput == "area1"):#Area1
    area1()
    printNow(userInput)
  if(userInput == "area2"):#Area2
    area2()   
    printNow(userInput)
  if(userInput == "area3"):#Area3
    area3()
    printNow(userInput)
  if(userInput == "area4"):#Area4
    area4()
                   
#This function will allow user to listen to sound clip and guess the animal.
def monkey():
  showInformation( "Listen Carefully to the following sound....")
  playAnySound()# chose file "monkey.wav"
  answer = requestString("Guess the animal: ")
  if (answer == 'monkey'):
    showInformation("Good job! It is correct!")
  else:
    showInformation("Sorry, you guessed wrong!")
        
def elephant():
  showInformation( "Listen Carefully to the following sound....")
  playAnySound()# chose file 
  answer = requestString("Guess the animal: ")
  if (answer == 'elephant'):
    showInformation("Good job! It is correct!")
  else:
    showInformation("Sorry, you guessed wrong!")
    
def bear():
  showInformation( "Listen Carefully to the following sound....")
  playAnySound()# chose file 
  answer = requestString("Guess the animal: ")
  if (answer == 'bear'):
    showInformation("Good job! It is correct!")
  else:
    showInformation("Sorry, you guessed wrong!")

def lion():
  showInformation( "Listen Carefully to the following sound....")
  playAnySound()# chose file 
  answer = requestString("Guess the animal: ")
  if (answer == 'lion'):
    showInformation("Good job! It is correct!")
  else:
    showInformation("Sorry, you guessed wrong!")
#Area1
def area1():
  showInformation("Welcome to Area 1!")
  monkey()
  

#Area2
def area2():
  showInformation("Welcome to Area 2!")
  elephant()

#Area3
def area3():
  showInformation("Welcome to Area 3!")
  bear()

#Area4
def area4():
  showInformation("Welcome to Area 4!")
  lion()


def zooGame():
  print ""
  print "    Welcome to 'Zoo Escape Game'" 
  print ""
  print "  Instructions: "
  print ""
  print "  4 animal have just escaped!"
  print "  You are the zookeeper and you have to find and capture the animals to return them to their cages."
  print "  You will traverse a map of the zoo by typing the name of the different area you want to go to." 
  print "  There is Area1, Area 2, Area3, and Area 4"
  print ""
  print "  Once you go to an area you will be prompted to listen for an animal." 
  print "  After you hear the animal sound, you have to guess which animal it is." 
  print "  You are allowed a total of 2 wrong guesses before and you lose the game." 
  print "  But if you guess all of the animals right within the allowed number of guesses you will win."
  print ""
  print "  1) Type 'help' to redisplay this introduction"
  print "  2) Type 'exit' to quit at any time"
  
  userInput()

# This function displays an image to the user saying they won the game  
def winningCondition():
  bg = makePicture('C:/Users/Eric/Documents/GitHub/cst205_Final/Images/ZooMapBackGround.jpg')
  monkey = makePicture('C:/Users/Eric/Documents/GitHub/cst205_Final/Images/monkey.jpg')
  pyCopy(monkey, bg, 625, 175, "green")
  
  elephant = makePicture('C:/Users/Eric/Documents/GitHub/cst205_Final/Images/elephant.jpg')
  pyCopy(elephant, bg, 51, 90,"green")
  
  bear = makePicture('C:/Users/Eric/Documents/GitHub/cst205_Final/Images/bear.jpg')
  pyCopy(bear, bg, 124, 480,"green")
  
  lion = makePicture('C:/Users/Eric/Documents/GitHub/cst205_Final/Images/lion.jpg')
  pyCopy(lion, bg, 500, 400, "green")
  
  str = "Congratulations!!! All the animals are back in their habitats"
  myFont = makeStyle(sansSerif,italic+bold,25)
  addTextWithStyle(bg, 70, 40,str,myFont,white)
  repaint(bg)

def pyCopy(source, target, targetX, targetY, sourceColor):
  if sourceColor == "green":
    for x in range(0, getWidth(source)):
      for y in range(0, getHeight(source)):
        p = getPixel(source,x,y)
        if ((getRed(p) + getBlue(p)) > getGreen(p)):
          color = getColor(p)
          setColor(getPixel(target, x+targetX, y+targetY), color)

#test 123
#second bla 