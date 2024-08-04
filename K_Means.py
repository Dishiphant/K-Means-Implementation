import random
import math

#K-Means Algorithm:

#takes input: List of List representing each data point

#intialize: select k random points to act as centroids?
#create k clusters with centroids abvoe

#main loop:

#go through all data points, then go through all centroids
#assign data point to nearest ccluster 

#update centroid of cluster based on all points in clutser

#repeat

#stopping criteria:

#number of iterations, to be based on size of dataset and clutsers? maybe?
#or flat based on time it takes to run on my device

#if set of data points in cluster do not change after an iteration
#or only change a tiny bit



class Cluster:
    def __init__(self, centroid, clusterPoints):
        self.centroid = centroid
        self.clusterPoints = clusterPoints

def kMeans(dataPoints, k):
    clusterList = initializeClusters(dataPoints, k)
    kMeansLoop(dataPoints, k, clusterList)

    return clusterList


def initializeClusters(dataPoints, k):
    clusterList = []
    for i in range(k):
        randomIndex = random.randint(0, len(dataPoints)-1)
        clusterList.append(Cluster(centroid = dataPoints[randomIndex], clusterPoints = []))
    return clusterList

def kMeansLoop(dataPoints, k, clusterList):
    converge = False
    iters = 0
    while converge is False and iters < 2000000:
        for cluster in clusterList:
            cluster.clusterPoints = []
        for point in dataPoints:
            assignCluster(point, clusterList)
        oldCentroids = []
        for cluster in clusterList:
            oldCentroids.append(cluster.centroid)
            recalculateCentroid(cluster, len(dataPoints[0]), dataPoints)

        print(f"Iteration {iters}:")
        for i, cluster in enumerate(clusterList):
            print(f"Cluster {i} - Centroid: {cluster.centroid}, Number of Points: {len(cluster.clusterPoints)}")

        for i in range(len(oldCentroids)):
            converge = True
            for j in range(len(clusterList[i].centroid)):
                if math.isclose(oldCentroids[i][j], clusterList[i].centroid[j], rel_tol=1e-9):
                    None
                else:
                    converge = False
                    break
                    

            if(math.isclose(oldCentroids[i][j], clusterList[i].centroid[j], rel_tol=1e-9) for j in range(len(clusterList[i].centroid))):
                None
            else:
                converge = False
                break
        
        iters += 1
        
            


def assignCluster(point, clusterList):
    minDistCluster = 0
    minDist = float('inf')
    eucliDistance = 0
    for j in range(len(clusterList)):
        for i in range(len(point)):
            eucliDistance += (point[i] - clusterList[j].centroid[i]) ** 2
        eucliDistance = math.sqrt(eucliDistance)
        if eucliDistance < minDist:
            minDist = eucliDistance
            minDistCluster = j
    clusterList[minDistCluster].clusterPoints.append(point)

        
    
def recalculateCentroid(cluster, pointSize, dataPoints):
    meanVector = [0] * pointSize
    if (len(cluster.clusterPoints) > 0):
        for point in cluster.clusterPoints:
            for i in range(len(point)):
                meanVector[i] += point[i]
        for i in range(len(meanVector)):
            meanVector[i] = meanVector[i] / len(cluster.clusterPoints)
        cluster.centroid = meanVector
    else:
        randomIndex = random.randint(0, len(dataPoints)-1)
        cluster.centroid = dataPoints[randomIndex]

        
