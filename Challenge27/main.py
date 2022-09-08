# Challenge 27
#
# Player 1 types in a word
# Player 2 has to guess the word in 5 lives
# The display would look like this

VERBOSE = True

import os

def VerbosePrint(*Data):
	if VERBOSE:
		print("[DEBUG]:", *Data)

def Main():
	os.system("clear")
	
	global Health
	global RoundCount
	global Word
	global Letters
	global FoundLetters
	
	Health = 5
	RoundCount = 0
	Word = input("What is the word?: ")
	Letters = list(Word)
	FoundLetters = [False] * len(Letters)
	
	def Round():
		global Health
		global RoundCount
		global CorrectGuessMade

		RoundCount = RoundCount + 1
		
		os.system("clear")
		DisplayWord = ""
	
		for i in range(0, len(Letters)):
			if FoundLetters[i]:
				DisplayWord = DisplayWord + Letters[i]
			else:
				DisplayWord = DisplayWord + "*"
	
		print("Lives:", Health)
		print("Round:", RoundCount)
		print("Current Word:", DisplayWord)
		print()
	
		def CheckScore():
			Count = 0
			for i in range(0, len(FoundLetters)):
				if FoundLetters[i]:
					Count = Count + 1
	
			return Count == len(FoundLetters)
		
		if Health == 0:
			print("You have lost!")
			input("\nPress enter for a new game.")
			Main()
		elif CheckScore():
			print("You have won!")
			input("\nPress enter for a new game.")
			Main()
		else:
			Guess = input()
		
			CorrectGuessMade = False
			for i in range(0, len(Letters)):
				if Letters[i] == Guess and not FoundLetters[i]:
					
					FoundLetters[i] = True
					CorrectGuessMade = True
		
			if not CorrectGuessMade:
				Health = Health - 1
		
			Round()
		
	Round()
Main()