#!/usr/bin/python

from standardRolls import rollDie
import sys

def chooseBackground():
    possBackgrounds = []
    with open("./backgroundTraits.txt",'r') as f:
        for line in f:
            if line.startswith("/background = "):
                possBackgrounds.append(" ".join([x[0].upper() + x[1:].lower() for x in line.replace("/background = ","").strip().split()]))
    sys.stderr.write("\nChoose your background:\n")
    iOuter = None
    for i,j in enumerate(possBackgrounds):
        sys.stderr.write("%4s %s\n" % ("["+str(i)+"]",j))
        iOuter = i*1
    sys.stderr.write("%4s %s\n" % ("["+str(iOuter+1)+"]","Pick at random for me"))
    while True:
        try:
            choice = int(raw_input(">>>> "))
            if not int(choice) in range(len(possBackgrounds)) and int(choice) != iOuter+1:
                raise ValueError
            else: break
        except (ValueError):
            sys.stderr.write("\tInput unacceptable, try again.\n")
    if choice == iOuter+1:
        choiceBackground = possBackgrounds[rollDie(len(possBackgrounds))-1]
    else:
        choiceBackground = possBackgrounds[choice]
    sys.stderr.write("Your background will be \"%s\"\n\n" % choiceBackground)
    return choiceBackground
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
    for q,qSel in qualitiesSelected:
	sys.stderr.write("%-12s: %s\n" % (q[0].upper()+q[1:].lower(),qSel))

class background:
    def __init__(self):
        self.name = chooseBackground()
        self.backgroundQualities = chooseBackgroundQualities(self.name.lower())
        #with open("./backgroundTraits.py",'r') as f:
            #backgroundFound = False
            #for line in f:
                #if line.startwith("/background = "):

