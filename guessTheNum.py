import sys
import random
print("Guess the number MC")
#upp=int(input("Enter poss upp bnd"))
#r=random.randint(1,upp)

#guess=input("Guess?")
corrr=[]
guesses=[]
for k in range (1,10):
	corrr.append(random.randint(1,10))
	guess=int(input("Guess: "))
	guesses.append(guess)
	if guess==corrr[-1]:
		print("Congrats! u got it in the",k,"th attempt")
		sys.exit()
	print("The corr ans was",corrr[-1])
print("Loser :(")
print(guesses)
print(corrr)		
