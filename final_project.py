#Authors: Joshua Howard, Eric Ybarra, Mercedes Garcia, William Barajas

#CST 205 Final Project
#testing 1,2,3
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
  if(userInput == "lush jungle"):#Area1
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

#Entrance of the zoo
def entrance():
  showInformation("You are at the Entrance of the zoo. You have 4 areas to choose from.")
  showInformation("Desert Oasis, Lush Jungle, Lost Forest and Wild Sahara")
  showInformation("please enter you response in lower case")
  userInput()
  
                   
                                                         
#This function will allow user to listen to sound clip and guess the animal.
def monkey():
  showInformation( "Listen Carefully to the following sound....")
  playAnySound()# chose file "monkey.wav"
  repeat = requestString("Would you like to listen to sound again? Enter 'yes' or 'no'")
  if(repeat == 'yes'):
    playAnySound()
  if(repeat == 'no'):
    print "Now, time to guess..."
  answer = requestString("Guess the animal: ")
  if (answer == 'monkey'):
   showInformation("Good job! It is correct!")
  else:
   showInformation("Sorry, you guessed wrong!")
        
def elephant():
  showInformation( "Listen Carefully to the following sound....")
  playAnySound()# chose file 
  repeat = requestString("Would you like to listen to sound again? Enter 'yes' or 'no'")
  if(repeat == 'yes'):
    playAnySound()
  if(repeat == 'no'):
    print "Now, time to guess..."
  answer = requestString("Guess the animal: ")
  if (answer == 'elephant'):
    showInformation("Good job! It is correct!")
  else:
    showInformation("Sorry, you guessed wrong!")
    
def bear():
  showInformation( "Listen Carefully to the following sound....")
  playAnySound()# chose file 
  repeat = requestString("Would you like to listen to sound again? Enter 'yes' or 'no'")
  if(repeat == 'yes'):
    playAnySound()
  if(repeat == 'no'):
    print "Now, time to guess..."
  answer = requestString("Guess the animal: ")
  if (answer == 'bear'):
    showInformation("Good job! It is correct!")
  else:
    showInformation("Sorry, you guessed wrong!")

def lion():
  showInformation( "Listen Carefully to the following sound....")
  playAnySound()# choose file "lion-roar.wav" file
  repeat = requestString("Would you like to listen to sound again? Enter 'yes' or 'no'")
  if(repeat == 'yes'):
    playAnySound()
  if(repeat == 'no'):
    print "Now, time to guess..."
  answer = requestString("Guess the animal: ")
  if (answer == 'lion'):
    showInformation("Good job! It is correct!")
  else:
    showInformation("Sorry, you guessed wrong!")
#Area1
def LushJungle():
  showInformation("Welcome to Area Lush Jungle!!!")
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
  
  entrance()

#test 123
#second bla 