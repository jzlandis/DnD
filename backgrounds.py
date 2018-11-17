#!/usr/bin/python

import sys
sys.dont_write_bytecode = True
from standardRolls import rollDie
from cursesWriter import cursesOptionMenu,cursesSplashScreen,cursesSummary

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
        backgroundChoice = possBackgrounds[rollDie(len(possBackgrounds)-1)-1]
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
    qualitiesSelected = []
    qualitiesToSelect = sorted(qualities.keys())
    intermediatePrompt = MAIN_HEADER + "\n" + "\n".join(["Now choose the qualities associated with your background:","You will choose a %s and %s\n" % (", ".join(qualitiesToSelect[:-1]),qualitiesToSelect[-1])])
    cursesSplashScreen(intermediatePrompt)
    for q in qualitiesToSelect:
        choice = cursesOptionMenu(MAIN_HEADER,"\nWould you like to see all options for your %s or select at random?\n" % q,"",["See all","Select at random"])
        resultWrite = str(MAIN_HEADER)
        if choice == 0:
            qChoice = cursesOptionMenu(MAIN_HEADER,"\nUse the indexes to select your %s\n" % q,"",qualities[q])
            qualitiesSelected.append((q,qualities[q][int(qChoice)]))
            resultWrite += "\nYou have chosen \"%s\" for your %s\n" % (qualities[q][int(qChoice)],q)
        else:
            qChoice = rollDie(len(qualities[q]))-1
            qualitiesSelected.append((q,qualities[q][int(qChoice)]))
            resultWrite += "\n\"%s\" has been randomly selected as your %s\n" % (qualities[q][int(qChoice)],q)
        cursesSplashScreen(resultWrite)
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
