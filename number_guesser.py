import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("please type a number larger than 0 next time. ")
        quit()
else:
    print("please type a number larger than 0 next time. ")
    quit()        

random_number  = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
     user_guess = int(user_guess)

    else:
      print("please type a number larger than 0 next time. ")
      continue
   
    if user_guess == random_number:
      print("You guessed it right!")
      break
    elif user_guess > random_number:
           print("You were above the random number!")
    else:
           print("You were below the random number!")

print("you got it in", guesses, "guesses") 
   

    




