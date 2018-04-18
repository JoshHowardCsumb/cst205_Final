#Authors: Joshua Howard, Eric Ybarra, Mercedes Garcia, William Barajas

#CST 205 Final Project
#testing 1,2,3

#IMPORTANT!!
#Change the path to your GitHub pathway
path = "C:/Users/baraj/OneDrive/Documents/GitHub/cst205_Final/Files"
#global variables that are needed in the program
global variables
global guesses
#frome of the picture
bg = path + '/ZooMapBackGround.jpg'
bg = makePicture(bg)
#number of guesses
guesses = 3
#pathways to images after path has been changed to specific user
variables ={"monkey":"False", "elephant":"False","bear":"False", "lion":"False", "win":0}
desertOasisImage = path + '/desert oasis.jpg'
elephantImage = path+ '/elephant.jpg'
lushJungleImage = path + '/lush jungle.jpg'
monkeyImage = path + '/monkey.jpg'
lostForestImage = path + '/lost forest.jpg'
bearImage = path + '/bear.jpg'
wildSaharaImage = path + '/wild sahara.jpg'
lionImage = path + '/lion.jpg'
mapOverlayImage = path + '/map_overlay.jpg'

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

def guessesLeft(): #This function should keep track of the number of guesses the user has
  global guesses
  guesses -= 1
  #if guesses are used up the program ends
  if guesses <= 0: 
    showInformation("You have no more tries left better luck next time")
    exit()
  else:
    guesses = str(guesses)
    showInformation("You have " + guesses + " tries left")  
    guesses = int(guesses)
    return

def end(userInput):#The purpose of this function is to quit the game if the user were to input "exit".
  while(userInput == "exit"):
    if(userInput == "exit"):
      print ""
      printNow ("  Done.")
      exit() 
#This function is called upon if an incorrect area is inserted  
def incorrect():
  showInformation("Enter one of the four locations. For help enter 'help'")
  userInput()
def userInput(): #This function will allow the user to traverse the zoo from differenct areas(1-4)
  global variables
  if variables["win"] == 4:
    winningCondition()
    end("exit")
  else:
    show(bg)
    userInput = requestString("What area would you like to go? ")
    printNow(userInput)
    if (userInput == "exit"):
      end(userInput)#Will end/exit game
    if(userInput == "help"):#Will provides instructions to what locations you can go to.
      zooGame() 
      printNow(userInput)  
    if(userInput == "lush jungle"):#Area1
      lushJungle()
      printNow(userInput)
    if(userInput == "desert oasis"):#Area2
      desertOasis()   
      printNow(userInput)
    if(userInput == "lost forest"):#Area3
      lostForest()
      printNow(userInput)
    if(userInput == "wild sahara"):#Area4
      wildSahara()
    else:
      if variables["win"] == 4:
        end("exit")
      elif guesses == 0:
        exit()
      else:
        incorrect()
#Entrance of the zoo
def entrance():
  showInformation("You are at the Entrance of the zoo. You have 4 areas to choose from.")
  showInformation("Desert Oasis, Lush Jungle, Lost Forest and Wild Sahara")
  showInformation("please enter you response in lower case")
  userInput()
                                    
#This function will allow user to listen to a sound clip and guess the animal.
def monkey():
  global guesses
  global variables
  #Will send the user back to the entrance if they already cleared this area
  if variables["monkey"] == "True":
    showInformation("Wait, You already cleared this area")
    userInput()
  else:
    #sound is played and user has to guess the animal
    showInformation( "Listen Carefully to the following sound....")
    monkeySound = path + '/monkey.wav'
    monkeySound= makeSound(monkeySound)
    play(monkeySound)
    answer = requestString("Guess the animal: ")
    if (answer == 'monkey'):
      showInformation("Good job! It is correct!")
      monkey = path + '/monkey.jpg'
      monkey = makePicture(monkey)
      pyCopy(monkey, bg, 625, 175, "green")
      repaint(bg)
      variables["win"] +=1
      variables["monkey"] = "True"
      userInput()
    else:
      showInformation("Sorry, you guessed wrong!")
      guessesLeft()
      if guesses > 0:
        lushJungle()
      else:
        print "Bye"
        
def elephant():
  global guesses 
  global variables
  if variables["elephant"] == "True":
    showInformation("Wait, You already cleared this area")
    userInput()
    #sound is played and user has to guess the animal
  else:
    showInformation( "Listen Carefully to the following sound....")
    elephantSound = path + '/elephant.wav'
    elephantSound= makeSound(elephantSound)
    play(elephantSound) 
    answer = requestString("Guess the animal: ")
    if (answer == 'elephant'):
      showInformation("Good job! It is correct!")
      elephant = path + "/elephant.jpg"
      elephant = makePicture(elephant)
      pyCopy(elephant, bg, 51, 90,"green")
      repaint(bg)
      variables["win"] +=1
      variables["elephant"] = "True"
      userInput()
    else:
      showInformation("Sorry, you guessed wrong!")
      guessesLeft()
      if guesses > 0:
        desertOasis()
      else:
        print "Bye"
    
def bear():
  global guesses
  global variables
  if variables["bear"] == "True":
    showInformation("Wait, You already cleared this area")
    userInput()
     #sound is played and user has to guess the animal
  else:
    showInformation( "Listen Carefully to the following sound....")
    bearSound = path + '/bear.wav'
    bearSound= makeSound(bearSound)
    play(bearSound)
    answer = requestString("Guess the animal: ")
    if (answer == 'bear'):
      showInformation("Good job! It is correct!")
      bear = path +'/bear.jpg'
      bear = makePicture(bear)
      pyCopy(bear, bg, 124, 480,"green")
      repaint(bg)
      variables["win"] += 1
      variables["bear"] = "True"
      userInput()
    else:
      showInformation("Sorry, you guessed wrong!")
      guessesLeft()
      if guesses > 0:
        lostForest()
      else:
        print "Bye"

def lion():
  global variables
  if variables["lion"] == "True":
    showInformation("Wait, You already cleared this area")
    userInput()
     #sound is played and user has to guess the animal
  else:
    showInformation( "Listen Carefully to the following sound....")
    lionSound = path + '/lion.wav'
    lionSound= makeSound(lionSound)
    play(lionSound)
    answer = requestString("Guess the animal: ")
    if (answer == 'lion'):
      showInformation("Good job! It is correct!")
      variables["lion"] = "True"
      lion = path + '/lion.jpg'
      lion = makePicture(lion)
      pyCopy(lion, bg, 500, 400, "green")
      repaint(bg)
      variables["win"] +=1

      userInput()
    else:
      showInformation("Sorry, you guessed wrong!")
      guessesLeft()
      if guesses > 0:
        wildSahara()
      else:
        print "Bye"
#Area1
def lushJungle():
  showInformation("Welcome to Area Lush Jungle!!!")
  monkey()

#Area2
def desertOasis():
  showInformation("Welcome to Desert Oasis!!!")
  elephant()

#Area3
def lostForest():
  showInformation("Welcome to Lost Forest!!!")
  bear()
#Area4
def wildSahara():
  showInformation("Welcome to Wild Sahara!!!")
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
  print "  There is 'Lush Jungle', 'Desert Oasis', 'Lost Forest', and 'Wild Sahara'"
  print ""
  print "  Once you go to an area you will be prompted to listen for an animal." 
  print "  After you hear the animal sound, you have to guess which animal it is." 
  print "  You are allowed a total of 3 wrong guesses before and you lose the game." 
  print "  But if you guess all of the animals right within the allowed number of guesses you will win."
  print ""
  print "  1) Type 'help' to redisplay this introduction"
  print "  2) Type 'exit' to quit at any time"
  
  entrance()

# This function displays the text to the user saying they won the game  
def winningCondition():
  
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