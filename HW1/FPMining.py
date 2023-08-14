import itertools


def readData(num):
    dataset = []
    f = open("topic-"+str(num)+".txt")
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
    f = open("patterns/pattern-" + str(num) + ".txt", "w")
    for item in resDict:
        f.write(str(item[1]) + " [" + str(item[0]) + "]\n")
    f.close()


def initItem(dataset, minSup):
    initDict = {}
    for i in dataset:
        for j in i:
            if j in initDict:
                initDict[j] += 1
            else:
                initDict[j] = 1
    resDict = {k: v for k, v in initDict.items() if v >= minSup}
    initSet = set(resDict)
    return resDict, initSet


def apriori(lastList, length, minSup):
    candList = list(itertools.combinations(lastList, 2))
    candDict = {}
    freqList = []
    for i in candList:
        if length == 2:
            candKey = i[0] + " " + i[1]
            for j in dataset:
                interSet = set(i).intersection(set(j))
                if len(interSet) == length:
                    if candKey in candDict:
                        candDict[candKey] += 1
                    else:
                        candDict[candKey] = 1
        else:
            res = set(list(i[0])+list(i[1]))
            if len(res) == length:
                candKey = ""
                count = 1
                for item in res:
                    if count == length:
                        candKey += item
                    else:
                        candKey += item + " "
                    count += 1
                for j in dataset:
                    interSet = set(res).intersection(set(j))
                    if len(interSet) == length:
                        if candKey in candDict:
                            candDict[candKey] += 1
                        else:
                            candDict[candKey] = 1
    freqDict = {k: v for k, v in candDict.items() if v >= minSup}
    for i in set(freqDict):
        temp = []
        for j in i.split():
            temp.append(j)
        freqList.append(temp)
    return freqDict, freqList


if __name__ == '__main__':
    percent = 0.01
    for i in range(0, 5):
        resDict = {}
        dataset = readData(i)
        minSup = int(len(dataset) * percent)
        freqDict = {0:0, 1:1, 2:2}
        resDict, initSet = initItem(dataset, minSup)
        count = 2
        freqList = list(initSet)
        while len(freqDict) > 1:
            freqDict, freqList = apriori(freqList, count, minSup)
            if len(freqDict) > 0:
                resDict.update(freqDict)
            count += 1
        resDict = sorted(resDict.items(), key=lambda x: x[1], reverse=True)
        writeFile(i, resDict)
