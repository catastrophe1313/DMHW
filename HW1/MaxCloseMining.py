import re

def readData(num):
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


def writeFile(num, resDict, type):
    f = open(type + "/" + type + "-" + str(num) + ".txt", "w")
    for k,v in resDict.items():
        f.write(str(v) + " [" + str(k) + "]\n")
    f.close()


def getClose(supList, patternList):
    closeDict = {}
    for i in range(0, len(patternList) - 1):
        flag = 0
        for j in range(i + 1, len(patternList)):
            if set(patternList[i]).issubset(set(patternList[j])) and supList[i] == supList[j]:
                break
            else:
                flag = j
        if flag == len(patternList) - 1:
            closeKey = patternList[i][0]
            for item in range(1, len(patternList[i])):
                closeKey += " " + patternList[i][item]
            closeDict[closeKey] = supList[i]
    return closeDict


def getMax(supList, patternList):
    maxDict = {}
    for i in range(0, len(patternList) - 1):
        flag = 0
        for j in range(i + 1, len(patternList)):
            if set(patternList[i]).issubset(set(patternList[j])):
                break
            else:
                flag = j
        if flag == len(patternList) - 1:
            maxKey = patternList[i][0]
            for item in range(1, len(patternList[i])):
                maxKey += " " + patternList[i][item]
            maxDict[maxKey] = supList[i]
    return maxDict


if __name__ == '__main__':
    for i in range(0, 5):
        supList, patternList = readData(i)
        closeDict = getClose(supList, patternList)
        writeFile(i, closeDict, "closed")
        maxDict = getMax(supList, patternList)
        writeFile(i, maxDict, "max")

