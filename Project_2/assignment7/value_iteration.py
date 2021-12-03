# Author : Michael Bonnet
# ID     : 1001753296
# Class  : CSE 4309-001 FA2021

###############
### Imports ###
###############

import sys
import numpy as np
import math
import csv

#####################
### Preprocessing ###
#####################

non_terminal_reward = float(sys.argv[2])
gamma               = float(sys.argv[3])
K                   = int(sys.argv[4])

#####################
### File Handling ### 
#####################

data = []
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

###########################
### Functions & Globals ###
###########################

movements = {"Up": "^",
             "Right": ">",
             "Down": "v",
             "Left": "<"}


def transition(sprime, s, a):
    returnVal = 0
    if a == "Up":
        newState = (s[0]-1, s[1])  # up
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.8

        newState = (s[0], s[1]-1)  # left
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.1

        newState = (s[0], s[1]+1)  # right
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.1

    elif a == "Left":
        newState = (s[0], s[1]-1)  # left
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.8

        newState = (s[0]-1, s[1])  # up
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.1

        newState = (s[0]+1, s[1])  # down
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.1

    elif a == "Down":
        newState = (s[0]+1, s[1])  # down
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.8

        newState = (s[0], s[1]-1)  # left
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.1

        newState = (s[0], s[1]+1)  # right
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.1

    elif a == "Right":
        newState = (s[0], s[1]+1)  # right
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.8

        newState = (s[0]-1, s[1])  # up
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.1

        newState = (s[0]+1, s[1])  # down
        if not valid(newState):
            newState = s
        if newState == sprime:
            returnVal += 0.1
    return returnVal


def valid(s):
    if s[0] >= 0 and s[0] < len(data):
        if s[1] >= 0 and s[1] < len(data[1]):
            if data[s[0]][s[1]] == 'X':
                return False
            return True
    return False


def R(state):
    val = data[state[0]][state[1]]
    if val == '.':
        return non_terminal_reward
    elif val == 'X':
        return 0
    else:
        return float(val)


def findmax(state, U, N, action):
    val = 0
    for i in range(N[0]):
        for j in range(N[1]):
            val += (transition((i, j), state, action) * U[i][j])
    return val


def valueIteration():
    N = len(data), len(data[0])
    pi = np.chararray(N, unicode=True)
    Uprime = np.zeros(N)
    
    for loop in range(K):
        U = Uprime.copy()
        
        for i in range(N[0]):
            
            for j in range(N[1]):
                if data[i][j] == 'X':
                    Uprime[i][j] = 0
                    pi[i][j] = 'x'
                elif data[i][j] != '.':
                    Uprime[i][j] = float(data[i][j])
                    pi[i][j] = 'o'
                else:
                    maxVal = 0
                    
                    for action in movements:
                        val = findmax((i, j), U, N, action)
                        maxVal = max(val, maxVal)
                        if val == maxVal:
                            pi[i][j] = movements[action]
                    
                    Uprime[i][j] = R((i, j)) + gamma * maxVal
    return U, pi




###################################
### Value Iteration Calculation ###
###################################

utilities, policy = valueIteration()

print("utilities:")
for i in range(len(utilities)):
    for j in range(len(utilities[0])):
        print("{:6.3f}".format(utilities[i][j]), end=' ')
    print()

print("\npolicy:")
for i in range(len(policy)):
    for j in range(len(policy[0])):
        print("{:6s}".format(policy[i][j]), end=' ')
    print()
