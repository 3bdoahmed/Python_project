import random

def guessGame():
    guessNum = random.randint(1,100)
    guess = None
    counter = 0


    while guess != guessNum:
        guess = int(input("please Guess a number between 1 and 100: "))

        if counter == 10:
          print("unformally you loss, the guess Number is ", guessNum)
          break

        if guess < guessNum:
            print("Higher! ")
            counter +=1
        elif guess > guessNum:
            print("lower! ")
            counter +=1
        else:
            print("Congratulations! You've guessed the number.")
            counter = 0
            break

guessGame()