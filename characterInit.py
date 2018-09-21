#!/usr/bin/python

from getAbilityScores import getAbilityScores,getPresetAbilityScores
import os
import sys

def abilitySelection():
	menuItems = [
		{"Generate random values per ch1.3" : getAbilityScores},
		{"Use the presets (15,14,13,12,10,8)" : getPresetAbilityScores}
		]
	sys.stderr.write("Select the method for choosing abilities:\n")
	#os.system('clear')
	for item in menuItems:
		sys.stderr.write("[" + str(menuItems.index(item)) + "] " + item.keys()[0] + '\n')
	properInput = False
	while not properInput:
		choice = raw_input(">>> ")
		try:
			if int(choice) in range(len(menuItems)):
				properInput = True
				s,m = menuItems[int(choice)].values()[0]()
			else: raise ValueError
		except (ValueError,IndexError):
			sys.stderr.write("\tImproper input, try again.\n")
			pass
	return s,m
def printAbilitiesAndMods(abilityScores,modifierScores):
	sys.stderr.write("Your available scores and modifiers are as follows\n")
	sys.stderr.write(" ".join(["AbilityScore".center(15,"-"),"Modifier".center(15,"-")]) + '\n')
	for s,m in reversed(sorted(zip(abilityScores,modifierScores),key=lambda x: x[0])):
		sys.stderr.write(("%2d" % s).center(15) + " " + ("%2d" % m).center(15) + '\n')
class character:
	def __init__(self):
		s,m = abilitySelection()
		printAbilitiesAndMods(s,m)
character()
