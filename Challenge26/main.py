# Challenge 26
#
# The computer generates a 4 digit code
# The user types in a 4 digit code. Their guess.
# The computer tells them how many digits they guessed correctly
# Extension : the computer tells them how many digits are
# guessed correctly in the correct place and how many digits have
# been guessed correctly but in the wrong place.
# The user gets 12 guesses to either win – guess the right code. Or
# lose – run out of guesses.

VERBOSE = False

import random
import os
import time
path = os.path

def VerbosePrint(*Data):
	if VERBOSE:
		print("[DEBUG]:", *Data)

Numbers = [None, None, None, None]
FoundNumbers = [False, False, False, False]
History = []
RoundCount = 1
Health = 12

def CheckWin():
	I = 0
	for FoundItem in range(0, len(FoundNumbers)):
		if FoundNumbers[FoundItem] == True:
			I = I + 1

	return I == 4
	
random.seed(time.time())

for Number in range(0, len(Numbers)):
	Numbers[Number] = random.randint(0, 9)

print(open("Challenge26/homescreen.txt").read())
VerbosePrint("Chosen Numbers:", Numbers, "\n")
input("\n\nPress enter to begin!")

def Round():
	global RoundCount
	global Health
	
	os.system("clear")

	print(open("Challenge26/logo.txt").read())
	
	print("\x1b[33mRound:\x1b[0m", RoundCount)
	print("\x1b[33mHealth:\x1b[0m", Health)

	print()
	if len(History) > 0:
		for Entry in range(0, len(History)):
			print(History[Entry])
			
	CurrentDisplay = ""
	
	for Number in range(0, len(Numbers)):
		if FoundNumbers[Number]:
			CurrentDisplay = CurrentDisplay + "\x1b[32m[{}]\x1b[0m ".format(Numbers[Number])
		else:
			CurrentDisplay = CurrentDisplay + "\x1b[31m[?]\x1b[0m "
			
	print(CurrentDisplay)

	if Health == 0:
		print("\x1b[31m", open("Challenge26/failscreen.txt").read(), "\x1b[0m")
		exit(0)
	
	if CheckWin():
		print("\x1b[32m\n", open("Challenge26/successscreen.txt").read(), "\x1b[0m")
		exit(0)
	else:
		Number = input("")
		try:
			Number = int(Number)
		except:
			Round()
		
		Found = False
		for Value in range(0, len(Numbers)):
			if Numbers[Value] == Number:
				FoundNumbers[Value] = True
				Found = True
		
		if not Found:
			Health = Health - 1
		
		History.append(CurrentDisplay)
		RoundCount = RoundCount + 1
		
		Round()

Round()