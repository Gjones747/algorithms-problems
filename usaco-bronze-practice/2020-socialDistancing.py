# https://usaco.org/current/index.php?page=viewproblem2&cpid=1035

#imports 
import random


# input vals
N = random.randint(5, 100000)

def createNString(N):
    createdString = ""
    for i in range(N):
        stallChoice = random.randint(1,2)
        if stallChoice == 1:
            createdString = createdString + "1"
        else:
            createdString = createdString + "0"

    return createdString

NString = createNString(N)
print(NString)

startIndex = 0
biggestDistance = 0 

while True:
    index = NString.find("1", startIndex)
    if index == -1:
        index = len(NString)
        if startIndex != 0:
            newdistance = int((index-(startIndex)))
        else:
            newdistance = int((index-startIndex))
        if newdistance > biggestDistance:
            biggestDistance = newdistance
        break
    if startIndex != 0:
        newdistance = int((index-(startIndex-1))/2)
    else:
        newdistance = int((index-startIndex))
    if newdistance > biggestDistance:
        biggestDistance = newdistance
    startIndex = index+1

print(biggestDistance)


#SCUFFED ASF - works tho according to my rigorous testing.