#Authors: Joshua Howard, Eric Ybarra, Mercedes Garcia, William Barajas

#CST 205 Final Project
#animals = ['monkey','lion','bear','elephant']
def playAnySound():
  file = pickAFile()
  sound = makeSound(file)
  play(sound)
  
#This function will allow user to listen to sound clip and guess the animal.
def monkey():
  print "Listen Carefully to the following sound...."
  playAnySound()# chosen file is "monkey.wav"
  requestString("Guess the animal: ")
  if (answer == 'monkey'):
    print "Good job! It is correct!"
  
  
  
def zooGame():
  animals = [monkey,lion,elephant,bear]
  
  print "      Welcome to 'Zoo Escape'"
  
  #Testing again for William 
  print "Testing"

