# Guess the Number Game


import random

# a = int(input('Enter a Number : '))
# b = int(input('Enter a Number : '))
RandNumber = random.randint(1,100)
# print(RandNumber)

UserGuess = None
guesses = 0
while(UserGuess!=RandNumber) :
    UserGuess = int(input('Enter a Number : '))

    if (UserGuess==RandNumber) :
        print("You Guesssed It Right!")
    else :
        print("You Guesssed It Wrong!")


    if(RandNumber>UserGuess) :
        print(f'Your Guess is Smaller than Random Number')
    elif(RandNumber<UserGuess) :
        print(f'Your Guess is Greater than Random Number ')
    elif(RandNumber==UserGuess) :
        print(f'Your Guessed number {UserGuess} is same as {RandNumber} ')

    guesses +=1
print(f"You Guessed the Number in {guesses} Guesses")

with open('Hi-Score.txt','r') as f :
    HiScore = int(f.read())

if (guesses<HiScore) :
    print("You have broken the highest record")
    with open('Hi-Score.txt','w') as f :
        f.write(str(guesses))
   

