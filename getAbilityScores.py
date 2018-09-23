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
    rollCollector = []
    for i in range(6):
	rolls = [rollDie(6) for x in range(4)]
	rollCollector.append(rolls)
        scores.append(sum(sorted(rolls)[-3:]))
        modifiers.append(generateModifier(scores[-1]))
    return zip(rollCollector,scores,modifiers)
def getPresetAbilityScores():
    scores = [15,14,13,12,10,8]
    modifiers = [generateModifier(score) for score in scores]
    return zip(scores,modifiers)
