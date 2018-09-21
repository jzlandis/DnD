#!/usr/bin/python

import random
import math

def generateModifier(score):
    return math.floor((score-10)/2)

def getAbilityScores():
    scores = [sum(sorted([int(round(5*random.random(),0))+1 for x in range(4)])) for y in range(6)]
    modifiers = [modifier(score) for score in scores]
    return scores,modifiers

s,m = abilityScores()
print "Your ability scores are   %s" % ", ".join(["%2d" % x for x in s])
print "The related modifiers are %s" % ", ".join(["%2d" % x for x in m])
