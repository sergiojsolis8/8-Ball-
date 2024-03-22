#importing module to use its function(random)
import random

#Name of who will be asking the question to *8 ball
name= "Sergio"

#Question for the 8 ball
question = "Are you a boy?"

#Leaving answer blank to use else/if answers below
answer = ""

#Giving the 8 Ball 9 possible answers
random_number = random.randint(1,9)

#else/if lines of code for 8 ball to return once a random number has been picked
if random_number == 1:
  answer= ("Yes - definitely")
elif random_number== 2:
  answer=("It is decidedly so")
elif random_number== 3:
  answer=("Without a doubt")
elif random_number == 4:
  answer=("Reply Hazy, Try again")
elif random_number == 5:
  answer=("Ask again later")
elif random_number == 6:
  answer=("Better not tell you now")
elif random_number == 7:
  answer=("My sources say no")
elif random_number == 8:
  answer=("Outlook not so good")
elif random_number == 9:
  answer=("Very Doubtful")
else: 
  answer = "Error"

#Question being asked by person
print(name  + " asks: " + question)

#Result of 8 Ball being asked a question 
print("Magic 8-Balls answer: " + answer)
