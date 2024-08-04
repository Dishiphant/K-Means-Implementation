import re
import K_Means

placesFile = 'Input Text File.txt'

#takes filepath of text file and returns it as line by line list
def fileScan(filePath):
    lineList = []
    with open(filePath, 'r') as file:
        for line in file:
            lineList.append(line.strip())
    return lineList

lineList = fileScan(placesFile)

# ========================================
# Splits each line into a list of words
# ========================================

#takes line and splits it according the rule into a list of segments
def wordSplit(line, splitRule):
    lineWords = re.split(splitRule, line)
    return lineWords

splitRule = r'[,]+'

lineList2 = []
for line in lineList:
    lineList2.append(wordSplit(line, splitRule))

lineList = lineList2

for i in range(len(lineList)):
    for j in range(len(lineList[i])):
        lineList[i][j] = float(lineList[i][j])

print(len(lineList))

clusterList = K_Means.kMeans(dataPoints = lineList, k = 3)

for cluster in clusterList:
    print("CLUSTER ")
    print(len(cluster.clusterPoints))
    print(cluster.centroid)
    print(cluster.clusterPoints)
    print("------------------")







# Open the file in write mode ('w')
with open('clusters.txt', 'w') as file:
    for i in range(len(lineList)):
        for j in range(len(clusterList)):
            if lineList[i] in clusterList[j].clusterPoints:
                writeStr = str(i) + " " + str(j) + "\n"
                file.write(writeStr)
                # file.write(f"{[key]}:{key}\n")



