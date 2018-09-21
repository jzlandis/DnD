#!/usr/bin/python

import random
import math
import sys
import time
from standardRolls import rollDie

def generateModifier(score):
    return int(math.floor((score-10)/2))

def getAbilityScores():
    scores = []
    modifiers = []
    for i in range(6):
	rolls = [rollDie(6) for x in range(4)]
        scores.append(sum(sorted(rolls)[-3:]))
        modifiers.append(generateModifier(scores[-1]))
	sys.stderr.write("%dth four d6 rolls are %s, top 3 sum to %2d, this will yield a modifier of %2d\n" % (i+1,", ".join(["%2d" % x for x in rolls]),scores[-1],modifiers[-1]))
        time.sleep(0.1)
    #scores = [sum(sorted([int(round(5*random.random(),0))+1 for x in range(4)])) for y in range(6)]
    #modifiers = [generateModifier(score) for score in scores]
    return scores,modifiers
def getPresetAbilityScores():
    scores = [15,14,13,12,10,8]
    modifiers = [generateModifier(score) for score in scores]
    return scores,modifiers

#s,m = getAbilityScores()
#print "Your ability scores are   %s" % ", ".join(["%2d" % x for x in s])
#print "The related modifiers are %s" % ", ".join(["%2d" % x for x in m])
