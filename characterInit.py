#!/usr/bin/python

from getAbilityScores import getAbilityScores,getPresetAbilityScores,generateModifier
from backgrounds import background
import os
import sys
from collections import OrderedDict
import time
from cursesWriter import cursesWriter,cursesOptionMenu,cursesSplashScreen,cursesAbilityByRand,cursesAbilityByPreset,cursesAbilityByScoreCost,cursesAssignScores

MAIN_HEADER = "DnD Character Creator (written by Jeremy Landis)\n"

def selectAbilityScoresByPoints():
	points = 27
	scoreCost = { 8:0,
		      9:1,
		     10:2,
		     11:3,
		     12:4,
		     13:5,
		     14:7,
		     15:9}
	sys.stderr.write("\nYou have chosen to assign ability scores by the points system. Acceptable scores to assign are from 8 through 15. You get 27 points to spend. Scores and their cost are tabulated below:\n%6s %6s\n" % ("Score","Cost"))
	for score in sorted(scoreCost.keys()):
		sys.stderr.write("%6d %6d\n" % (score,scoreCost[score]))
	abilityItems = OrderedDict([
			("Strength","Unassigned"),
			("Dexterity","Unassigned"),
			("Constitution","Unassigned"),
			("Intelligence","Unassigned"),
			("Wisdom","Unassigned"),
			("Charisma","Unassigned")
			])
	time.sleep(1)
	while "Unassigned" in abilityItems.values():
		printAbilitySelection(abilityItems)
		properInput = False
		sys.stderr.write("Available points: %2d\n\n" % points)
		while not properInput:
			try:
				choiceInput = raw_input(">>>> ").split()
				if len(choiceInput) == 1 and int(choiceInput[0]) in [x*-1 for x in range(1,len(abilityItems)+1)]:
					abilityIndex = -1*int(choiceInput[0])
					if abilityItems[abilityItems.keys()[abilityIndex-1]] == "Unassigned":
						sys.stderr.write("That ability isn't assigned, no change\n")
					else:
						points += scoreCost[abilityItems[abilityItems.keys()[abilityIndex-1]][0]]
						abilityItems[abilityItems.keys()[abilityIndex-1]] = "Unassigned"
				elif len(choiceInput) == 2:
					abilityIndex,value2Assign = [int(x) for x in choiceInput]
					if not value2Assign in range(8,16) or not abilityIndex in range(1,len(abilityItems)+1): raise ValueError
					if not abilityItems[abilityItems.keys()[abilityIndex-1]] == "Unassigned":
						if points + scoreCost[abilityItems[abilityItems.keys()[abilityIndex-1]][0]] >= scoreCost[value2Assign]:
							points += scoreCost[abilityItems[abilityItems.keys()[abilityIndex-1]][0]]
					if scoreCost[value2Assign] > points:
						sys.stderr.write("\tNot enough points, try again\n")
					else:
						points -= scoreCost[value2Assign]
						abilityItems[abilityItems.keys()[abilityIndex-1]] = (value2Assign,generateModifier(value2Assign))
				else: raise ValueError
				properInput = True
			except (ValueError):
				sys.stderr.write("\tImproper input, try again.\n")
	printAbilitySelection(abilityItems)
	return abilityItems,"pointsSystem"

def abilitySelection():
	title = "Select the method for choosing base ability scores:"
	helpText = ""
	menuChoices = [("Generate random values per ch1.3",cursesAbilityByRand),
		       ("Use the presets (15,14,13,12,10,8)",cursesAbilityByPreset),
		       ("Use the score-cost system to select your abilities",cursesAbilityByScoreCost)]
	basicScores,need2assign = menuChoices[cursesOptionMenu(MAIN_HEADER,title,helpText,[x[0] for x in menuChoices])][1](MAIN_HEADER)	
	if need2assign:
		orderedScores = cursesAssignScores(MAIN_HEADER,basicScores)
	else:
		orderedScores = basicScores
	return orderedScores
def printAbilitiesAndMods(abilityScores,modifierScores):
	sys.stderr.write("Your available scores and modifiers are as follows\n")
	sys.stderr.write(" ".join(["AbilityScore".center(15,"-"),"Modifier".center(15,"-")]) + '\n')
	for s,m in reversed(sorted(zip(abilityScores,modifierScores),key=lambda x: x[0])):
		sys.stderr.write(("%2d" % s).center(15) + " " + ("%2d" % m).center(15) + '\n')
def printAbilitySelection(abilityDict,mode="stderr"):
	if mode == "stderr":
		i = 0
		sys.stderr.write("\n    %s %s\n" % ("Ability".center(13,"-")," Score (mod)"))
		for k,v in abilityDict.items():
			if type(v) == str:
				vout = v
			elif type(v) == tuple:
				if v[1] > -1:
					vout = "%5d (+%d)" % v
				else:
					vout = "%5d (%d)" % v
			else: raise TypeError
			sys.stderr.write("[%d] %13s: %s\n" % (i+1,k,vout))
			i+=1
	elif mode == "str":
		msg = ""
		i = 0
		msg += str("\n%s %s\n" % ("Ability".center(13,"-")," Score (mod)"))
		for k,v in abilityDict.items():
			if type(v) == str:
				vout = v
			elif type(v) == tuple:
				if v[1] > -1:
					vout = "%5d (+%d)" % v
				else:
					vout = "%5d (%d)" % v
			else: raise TypeError
			msg += str("%13s: %s\n" % (k,vout))
			i+=1
		return msg
	else: raise ValueError

class abilitySet:
	def __init__(self):
		self.abilities = abilitySelection()
	def __repr__(self):
		return printAbilitySelection(self.abilities,mode="str")
class character:
	def __init__(self):
		self.abilities = abilitySet()
		self.background = background()

splashScreen = ""
with open('splashScreen.txt','r') as f:
	for line in f:
		splashScreen += line

cursesSplashScreen(splashScreen)
me = character()
