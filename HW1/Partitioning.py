def reorganizeTerm():
    f = open("result/word-assignments.dat")
    line = f.readline()
    orgMap = {0: [], 1: [], 2: [], 3: [], 4: []}
    count = 0
    while line:
        orgSplit = line.split()
        for value in orgMap.values():
            temp = []
            value.append(temp)
        for i in range(1, len(orgSplit)):
            term = orgSplit[i].split(":")[0]
            topic = int(orgSplit[i].split(":")[1])
            orgMap[topic][count].append(term)
        line = f.readline()
        count += 1
    for key, value in orgMap.items():
        f = open("topic-" + str(key) + ".txt", "w")
        for i in value:
            if len(i) != 0:
                for j in i:
                    f.write(j + " ")
                f.write("\n")
        f.close()


if __name__ == '__main__':
    reorganizeTerm()