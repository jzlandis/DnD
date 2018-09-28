#!/usr/bin/python

from standardRolls import rollDie
from cursesWriter import cursesOptionMenu
#cursesOptionMenu(header,title,helpText,choices,indexOrigin=0):
import sys

MAIN_HEADER = "DnD Character Creator (written by Jeremy Landis)\n"

def chooseBackground():
    possBackgrounds = []
    with open("./backgroundTraits.txt",'r') as f:
        for line in f:
            if line.startswith("/background = "):
                possBackgrounds.append(" ".join([x[0].upper() + x[1:].lower() for x in line.replace("/background = ","").strip().split()]))
    possBackgrounds.append("Choose at random")
    backgroundChoice = possBackgrounds[cursesOptionMenu(MAIN_HEADER,"Choose your background:","",possBackgrounds)]
    if backgroundChoice == possBackgrounds[-1]:
	backgroundChoice = possBackgrounds[rollDie(len(backgroundChoice)-2)]
    print backgroundChoice
    return backgroundChoice

def chooseBackgroundQualities(backgroundName):
    with open("./backgroundTraits.txt",'r') as f:
        read = False
        qualities = {}
        quality = ""
        for line in f:
            if line.startswith("/background = "):
                if read == True:
                    break
                if backgroundName in line:
                    read = True
            if read and not line.startswith("/background = "):
                if line.startswith("/"):
                    quality = line.replace("/","").strip()
                else:
                    if not quality in qualities.keys():
                        qualities[quality] = []
                    qualities[quality].append(line.strip())
    sys.stderr.write("Now choose the qualities associated with your background:\n")
    qualitiesSelected = []
    qualitiesToSelect = sorted(qualities.keys())
    sys.stderr.write("You will choose a %s and %s\n" % (", ".join(qualitiesToSelect[:-1]),qualitiesToSelect[-1]))
    for q in qualitiesToSelect:
        sys.stderr.write("\nWould you like to see all options for your %s or select at random?\n" % q)
        sys.stderr.write("[0] See all\n[1] Select at random\n")
        while True:
            choice = raw_input(">>>> ")
            try:
                if int(choice) in [0,1]:
                    break
            except ValueError:
                sys.stderr.write("\tInvalid input, try again\n")
        if int(choice) == 0:
	    sys.stderr.write("Use the indexes to select your %s\n" % q)
            for i,j in enumerate(qualities[q]):
                sys.stderr.write("%4s %s\n" % ("[" + str(i) + "]",j))
            while True:
                qChoice = raw_input(">>>> ")
                try:
                    if int(qChoice) in range(len(qualities[q])):
                        sys.stderr.write("You have chosen \"%s\" for your %s\n" % (qualities[q][int(qChoice)],q))
                        qualitiesSelected.append((q,qualities[q][int(qChoice)]))
			break
                    else: raise ValueError
                except ValueError:
                    sys.stderr.write("\tInvalid input, try again\n")
        else:
	    qChoice = rollDie(len(qualities[q]))-1
	    qualitiesSelected.append((q,qualities[q][int(qChoice)]))
	    sys.stderr.write("\"%s\" has been randomly selected as your %s\n" % (qualities[q][int(qChoice)],q))
    sys.stderr.write("\nHere is a summary of your selected background qualitites.\nYou will be a %s\n" % (" ".join([x[0].upper() + x[1:] for x in backgroundName.split()])))
    sys.stderr.write(printBackgroundQualities(qualitiesSelected))
    return qualitiesSelected

def printBackgroundQualities(qualitiesList):
    msg = "\n"
    ljustSize = max([len(x[0]) for x in qualitiesList]) + 1
    for q,qSel in qualitiesList:
	msg += str("%s: %s\n" % (str(q[0].upper()+q[1:].lower()).ljust(ljustSize+1),qSel))
    return msg

class background:
    def __init__(self):
        self.name = chooseBackground()
        self.backgroundQualities = chooseBackgroundQualities(self.name.lower())
    def __repr__(self):
	return " ".join([x[0].upper() + x[1:].lower() for x in self.name.split()]) + '\n' +  printBackgroundQualities(self.backgroundQualities)
