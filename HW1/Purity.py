import math
import re


def readFreq(num):
    supList = []
    patternList = []
    f = open("patterns/pattern-" + str(num) + ".txt")
    line = f.readline()
    while line:
        patternSplit = line.split(" ", 1)
        supList.append(int(patternSplit[0]))
        patternList.append(re.findall(r"\d+", patternSplit[1]))
        line = f.readline()
    f.close()
    return supList, patternList


def readAll(num):
    dataset = []
    f = open("topic-" + str(num) + ".txt")
    line = f.readline()
    while line:
        temp = []
        topicSplit = line.split()
        for i in topicSplit:
            temp.append(i)
        dataset.append(temp)
        line = f.readline()
    f.close()
    return dataset


def writeFile(num, resDict):
    f = open("purity/purity-" + str(num) + ".txt", "w")
    for item in resDict:
        f.write(str(item[1]) + " [" + str(item[0]) + "]\n")
    f.close()


def getUnionLen(allDict, num):
    lenDict = {}
    for i in range(0, 5):
        if i != num:
            newList = allDict[num] + allDict[i]
            unionList = list(filter(lambda x: newList.count(x) == 1, newList))
            lenDict[i] = len(unionList)
    return lenDict


def purity(supDict, patternDict, allDict, num):
    purDict = {}
    thisLen = len(allDict[num])
    lenDict = getUnionLen(allDict, num)
    for i in range(0, len(patternDict[num])):
        pattern = patternDict[num][i]
        key = pattern[0]
        for item in range(1, len(pattern)):
            key += " " + pattern[item]
        thisFreq = supDict[num][i]
        part1 = thisFreq / thisLen
        part2 = 0.0
        for j in range(0, 5):
            if j != num:
                otherFreq = 0
                allTopic = allDict[j]
                for k in allTopic:
                    if set(pattern).issubset(set(k)):
                        otherFreq += 1
                res = (thisFreq + otherFreq) / lenDict[j]
                if part2 < res:
                    part2 = res
        purDict[key] = math.log2(thisFreq) + math.log2(part1) - math.log2(part2)
    return purDict


if __name__ == '__main__':
    supDict = {}
    patternDict = {}
    allDict = {}
    for i in range(0, 5):
        supDict[i], patternDict[i] = readFreq(i)
        allDict[i] = readAll(i)
    for i in range(0, 5):
        purDict = purity(supDict, patternDict, allDict, i)
        purDict = sorted(purDict.items(), key=lambda x: x[1], reverse=True)
        writeFile(i, purDict)
