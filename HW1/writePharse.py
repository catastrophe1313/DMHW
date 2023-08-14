import re


def readVoc():
    vocDict = {}
    f = open("vocab.txt")
    line = f.readline()
    count = 0
    while line:
        sp = line.split()
        vocDict[count] = sp[0]
        count += 1
        line = f.readline()
    f.close()
    return vocDict


def idToTerm(vocDict, file, type, num):
    supList = []
    patternList = []
    path = file + "/" + type + "-" + str(num) + ".txt"
    f = open(path)
    line = f.readline()
    while line:
        patternSplit = line.split(" ", 1)
        supList.append(patternSplit[0])
        vocList = re.findall(r"\d+", patternSplit[1])
        vocList = [vocDict[int(i)] for i in vocList]
        patternList.append(vocList)
        line = f.readline()
    f = open(path + ".pharse", "w")
    for i in range(0, len(supList)):
        key = patternList[i][0]
        for j in range(1, len(patternList[i])):
            key += " " + patternList[i][j]
        f.write(str(supList[i]) + " [" + str(key) + "]\n")
    f.close()


if __name__ == '__main__':
    vocDict = readVoc()
    for i in range(0, 5):
        idToTerm(vocDict, 'patterns', "pattern", i)
        idToTerm(vocDict, 'closed', "closed", i)
        idToTerm(vocDict, 'max', "max", i)
        idToTerm(vocDict, 'purity', "purity", i)