#!/usr/bin/python

from getAbilityScores import getAbilityScores,getPresetAbilityScores,generateModifier
from backgrounds import background
import os
import sys
from collections import OrderedDict
import time
from cursesWriter import cursesWriter,cursesOptionMenu,cursesSplashScreen,cursesAbilityByRand,cursesAbilityByPreset,cursesAbilityByScoreCost,cursesAssignScores

MAIN_HEADER = "DnD Character Creator (written by Jeremy Landis)\n"

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
