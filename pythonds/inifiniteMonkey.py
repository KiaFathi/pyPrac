import string
import random

testStr = "methinks it is like a weasel"

def generateStr(strLen):
  alphabet = "abcdefghijklmnopqrstuvwxyz "
  res = ""
  for i in range(strLen):
    res = res + alphabet[random.randrange(27)]

  return res

def scoreStr(target, testString):
  length = len(target)
  numSame = 0.0
  for i in range(length):
    if target[i] == testString[i]:
      numSame += 1

  return numSame / length

def mainMonkey(testStr):
  newstring = generateStr(len(testStr))
  best = 0
  newScore = scoreStr(testStr, newstring)
  while(newScore < 1):
    if(newScore >= best):
      print(newScore, newstring)
      best = newScore
    newstring = generateStr(len(testStr))
    newScore = scoreStr(testStr, newstring)

def generateLetter():
  alphabet = "abcdefghijklmnopqrstuvwxyz "
  newLetter = alphabet[random.randrange(27)]
  return newLetter

def scoreList(goalList, newList):
  length = len(goalList)
  numSame = 0.0
  for i in range(length):
    if goalList[i] == newList[i]:
      numSame += 1
    else:
      newList[i] = generateLetter();

  return numSame / length

def betterMonkey(goalStr):
  bestScore = 0.0
  rounds = 0
  goalArr = list(goalStr)
  testArr = list(generateStr(len(goalStr)))
  
  while(bestScore < 1.0):
    rounds += 1
    score = scoreList(goalArr, testArr)
    if(score > bestScore):
      print(rounds, score, ''.join(testArr))
      bestScore = score
  
  return ''.join(testArr)


print(betterMonkey(testStr))
