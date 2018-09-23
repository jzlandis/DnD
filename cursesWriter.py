#!/usr/bin/python

import os,sys
import curses
import time
from getAbilityScores import getAbilityScores,getPresetAbilityScores,generateModifier
from collections import OrderedDict

def drawMenu(stdscr,title,body,previousInputs,feedbackText):
	curses.echo()
	k = 0
	cursor_x = 0
	cursor_y = 0

	stdscr.clear()
	stdscr.refresh()

	stdscr.addstr("%s\n" % title)
	stdscr.addstr("%s\n" % body)
	for i in previousInputs:
		stdscr.addstr(">>>> %s\n" % i)
	
	stdscr.addstr(">>>> ")
	return stdscr.getstr()

def cursesWriter(title,body,previousInputs,feedbackText=""):
	return curses.wrapper(drawMenu,title,body,previousInputs,feedbackText)

def optionMenu(stdscr,header,title,helpText,choices,indexOrigin):
	curses.echo()
	stdscr.clear()
	stdscr.refresh()
	for i in [header,title,helpText]:
		if i != "":
			stdscr.addstr("%s\n" % i)
	stdscr.addstr("\n")
	indexLength = 2 + len(str(indexOrigin+len(choices)))
	indexCounter = 1*indexOrigin
	for choice in choices:
		stdscr.addstr("%s : %s\n" % (str("["+str(indexCounter)+"]").ljust(indexLength),choice))
		indexCounter += 1
	selected = None
	while True	:
		stdscr.addstr(">>>> ")
		try:
			selected = int(stdscr.getstr())
			if not selected in range(indexOrigin,indexOrigin+len(choices)): raise ValueError
			break
		except ValueError:
			stdscr.addstr("\tInvalid input, try again\n")
	return selected
def splashScreenWriter(stdscr,splashScreen):
	curses.noecho()
	stdscr.clear()
	stdscr.refresh()
	stdscr.addstr(splashScreen)
	stdscr.addstr("\nASCII art created with PyFiglet\nPress Any Button to Continue\n")
	x = stdscr.getch()
def abilityByRand(stdscr,header,title,helpText):
	curses.echo()
	stdscr.clear()
	stdscr.refresh()
	for i in [header,title,helpText]:
		if i != "":
			stdscr.addstr("%s\n" % i)
	stdscr.addstr("%s %s %s\n" % ("Rolls".center(7,"-"),"Top3Sum".center(9,"-"),"Modifier"))
	scoreOutput = getAbilityScores()
	for rolls,top3sum,mod in scoreOutput:
		stdscr.addstr("%s %s %s\n" % (",".join([str(x) for x in rolls]),str(top3sum).rjust(2).center(9),str(mod).rjust(2).center(8)))
	stdscr.addstr("Press any key to continue to the assignment of these scores to abilities\n")
	curses.noecho()
	x = stdscr.getch()
	return [x[1:] for x in scoreOutput],True
def abilityByPreset(stdscr,header,title,helpText):
	curses.echo()
	stdscr.clear()
	stdscr.refresh()
	for i in [header,title,helpText]:
		if i != "":
			stdscr.addstr("%s\n" % i)
	stdscr.addstr("%s %s\n" % ("Score".center(9,"-"),"Modifier".center(9,"-")))
	scoreOutput = getPresetAbilityScores()
	for score,mod in scoreOutput:
		stdscr.addstr("%s %s\n" % (str("%2d" % score).center(9," "),str("%2d" % mod).center(9," ")))
	stdscr.addstr("Press any key to continue to the assignment of these scores to abilities\n")
	curses.noecho()
	x = stdscr.getch()
	return scoreOutput,True
def abilityByScoreCost(stdscr,header,title,helpText):
	curses.echo()
	stdscr.clear()
	stdscr.refresh()
	points = 27
	scoreCost = { 8:0,
		      9:1,
		     10:2,
		     11:3,
		     12:4,
		     13:5,
		     14:7,
		     15:9}
	abilityItems = OrderedDict([
			("Strength","Unassigned"),
			("Dexterity","Unassigned"),
			("Constitution","Unassigned"),
			("Intelligence","Unassigned"),
			("Wisdom","Unassigned"),
			("Charisma","Unassigned")
			])
	while "Unassigned" in abilityItems.values():
		stdscr.clear()
		stdscr.refresh()
		for i in [header,title,helpText]:
			if i != "":
				stdscr.addstr("%s\n" % i)
		stdscr.addstr("You have chosen to assign ability scores by the points system. Acceptable scores to assign are from 8 through 15. You get 27 points to spend. Scores and their cost are tabulated below:\n%6s %6s\n" % ("Score","Cost"))
		for score in sorted(scoreCost.keys()):
			stdscr.addstr("%6d %6d\n" % (score,scoreCost[score]))
		stdscr.addstr(printAbilityDict(abilityItems))
		stdscr.addstr("Available points: %2d\n\n" % points)
		while True:
			try:
				stdscr.addstr(">>>> ")
				choiceInput = stdscr.getstr().split()
				if len(choiceInput) == 1 and int(choiceInput[0]) in [x*-1 for x in range(1,len(abilityItems)+1)]:
					abilityIndex = -1*int(choiceInput[0])
					if abilityItems[abilityItems.keys()[abilityIndex-1]] == "Unassigned":
						stdscr.addstr("That ability isn't assigned, no change\n")
					else:
						points += scoreCost[abilityItems[abilityItems.keys()[abilityIndex-1]][0]]
						abilityItems[abilityItems.keys()[abilityIndex-1]] = "Unassigned"
						break
				elif len(choiceInput) == 2:
					abilityIndex,value2Assign = [int(x) for x in choiceInput]
					if not value2Assign in range(8,16) or not abilityIndex in range(1,len(abilityItems)+1): raise ValueError
					if not abilityItems[abilityItems.keys()[abilityIndex-1]] == "Unassigned":
						if points + scoreCost[abilityItems[abilityItems.keys()[abilityIndex-1]][0]] >= scoreCost[value2Assign]:
							points += scoreCost[abilityItems[abilityItems.keys()[abilityIndex-1]][0]]
					if scoreCost[value2Assign] > points:
						stdscr.addstr("\tNot enough points, try again\n")
					else:
						points -= scoreCost[value2Assign]
						abilityItems[abilityItems.keys()[abilityIndex-1]] = (value2Assign,generateModifier(value2Assign))
						break
				else: raise ValueError
			except (ValueError):
				stdscr.addstr("\tImproper input, try again.\n")
	return abilityItems
def assignScores(stdscr,header,basicScores,title,helpText):
	curses.echo()
	stdscr.clear()
	stdscr.refresh()
	availableScores = list([x[0] for x in basicScores])
	s = list([x[0] for x in basicScores])
	m = list([x[1] for x in basicScores])
	abilityItems = OrderedDict([
			("Strength","Unassigned"),
			("Dexterity","Unassigned"),
			("Constitution","Unassigned"),
			("Intelligence","Unassigned"),
			("Wisdom","Unassigned"),
			("Charisma","Unassigned")
			])
	while "Unassigned" in abilityItems.values():
		stdscr.clear()
		stdscr.refresh()
		for i in [header,title,helpText]:
			if i != "":
				stdscr.addstr("%s\n" % i)
		stdscr.addstr(printAbilityDict(abilityItems))
		stdscr.addstr("Available scores: %s\n" % list(reversed(sorted(availableScores))))
		while True:
			try:
				stdscr.addstr(">>>> ")
				choiceInput = stdscr.getstr().split()
				if len(choiceInput) == 1 and int(choiceInput[0]) in [x*-1 for x in range(1,len(abilityItems)+1)]:
					abilityIndex = -1*int(choiceInput[0])
					currentlyAssigned = abilityItems[abilityItems.keys()[abilityIndex-1]]
					if currentlyAssigned == "Unassigned":
						stdscr.addstr("\tThat ability isn't assigned, no change\n")
					else:
						availableScores.append(currentlyAssigned[0])
						abilityItems[abilityItems.keys()[abilityIndex-1]] = "Unassigned"
				elif len(choiceInput) == 2:
					abilityIndex,value2Assign = [int(x) for x in choiceInput]
					if not value2Assign in [x[0] for x in basicScores] or not abilityIndex in range(1,len(abilityItems)+1): raise ValueError
					if choiceInput[0] == "": raise ValueError
					if not abilityItems[abilityItems.keys()[abilityIndex-1]] == "Unassigned":
						abilityItems[abilityItems.keys()[abilityIndex-1]] == "Unassigned"
						availableScores.append(abilityItems[abilityItems.keys()[abilityIndex-1]][0])
					if not value2Assign in availableScores:
						for k,v in abilityItems.items():
							if v[0] == value2Assign:
								abilityItems[k] = "Unassigned"
								availableScores.append(value2Assign)
								break
					availableScores.remove(value2Assign)
					abilityItems[abilityItems.keys()[abilityIndex-1]] = (value2Assign,m[s.index(value2Assign)])
				break
			except ValueError:
				stdscr.addstr("\tInvalid input, try again\n")
	return abilityItems
def cursesOptionMenu(header,title,helpText,choices,indexOrigin=0):
	return curses.wrapper(optionMenu,header,title,helpText,choices,indexOrigin)
def cursesSplashScreen(splashScreen):
	return curses.wrapper(splashScreenWriter,splashScreen)
def cursesAbilityByRand(header,title="Generating random ability scores...",helpText=""):
	return curses.wrapper(abilityByRand,header,title,helpText)
def cursesAbilityByPreset(header,title="The preset scores and modifiers are as follows:",helpText=""):
	return curses.wrapper(abilityByPreset,header,title,helpText)
def cursesAbilityByScoreCost(header,title="Select your ability scores using the score-cost system below:",helpText=""):
	return curses.wrapper(abilityByScoreCost,header,title,helpText)
def cursesAssignScores(header,basicScores,title="Assign the available scores to each ability:",helpText="Assign your ability scores to abilities:\nAt the prompt input the index of the ability followed by the score to be assigned to it. If the score is already assigned to another ability try removing it from that one by using the negative index.\n"):
	return curses.wrapper(assignScores,header,basicScores,title,helpText)
def printAbilityDict(abilityDict):
	msg = ""
	msg += str("     %s %s\n" % ("Ability".center(13,"-"),"Score (mod)"))
	i = 1
	for k,v in abilityDict.items():
		if type(v) == str:
			vout = v
		elif type(v) == tuple:
			if v[1] > -1:
				vout = "%5d (+%d)" % v
			else:
				vout = "%5d (%d)" % v
		else: raise TypeError
		msg += str("[%d] %13s: %s\n" % (i,k,vout))
		i+=1
	return msg
