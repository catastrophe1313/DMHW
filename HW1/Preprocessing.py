def getVocabDict():
    f = open("paper.txt")
    line = f.readline()
    vocSet = set()
    vocStat = []
    vocCount = []
    while line:
        vocSplit = line.split()
        item = []
        for i in range(1, len(vocSplit)):
            vocSet.add(vocSplit[i])
            item.append(vocSplit[i])
        vocCount.append(len(set(item)))
        vocStat.append(item)
        line = f.readline()
    f.close()
    f = open("vocab.txt", "w")
    for i in vocSet:
        f.write(i)
        f.write("\n")
    f.close()
    return vocSet, vocStat, vocCount


def tokenizeTitle(vocSet, vocStat, vocCount):
    vocList = list(vocSet)
    f = open("title.txt", "w")
    for i in range(len(vocStat)):
        f.write(str(vocCount[i]) + " ")
        statDict = {}
        for j in vocStat[i]:
            ind = vocList.index(j)
            if ind in statDict:
                statDict[ind] += 1
            else:
                statDict[ind] = 1
        for k, v in statDict.items():
            f.write(str(k) + ":" + str(v) + " ")
        f.write("\n")
    f.close()


if __name__ == '__main__':
    vocSet, vocStat, vocCount = getVocabDict()
    tokenizeTitle(vocSet, vocStat, vocCount)