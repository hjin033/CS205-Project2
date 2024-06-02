import math
import copy

def nearest(data, features):
    correct = 0
    closestDist = 10
    guess = 1
    distance = 10
    
    #Nested for loop to test each data against the entire dataset
    for i in range(len(data)):
        testData  = data[i].split()
        for j in range(len(data)):
            currentData = data[j].split()
            if testData == currentData:
                continue #skip on the data left out for testing
            distance = 0
            for f in features:
                distance += (float(testData[f]) - float(currentData[f])) ** 2 #Euclidean distance
            distance = math.sqrt(distance)
            if distance < closestDist:
                closestDist = distance
                guess = int(float(currentData[0]))
        closestDist = 10
        if guess == int(float(testData[0])):
            correct += 1
             
    return correct / len(data)

def forward(fileName):
    file = open(fileName, "r")
    data = file.readlines()
    featureNum = len(data[0].split())
    features = []
    bestFeatures = []
    bestAcc = 0
    acc = 0
    
    print("The dataset has %d features and %d instances." % (featureNum - 1, len(data)))
    print("")
    
    #Nested for loop that expand(add feature) upon the (local)best feature set
    for i in range(1, featureNum):
        currBest = 0
        currFeat = 0
        for j in range(1, featureNum):
            if j in features:
                continue
            acc = nearest(data, features + [j])
            print("Feature(s) %s, the accuracy is %.2f%%" % (str(features + [j]), acc * 100))
            if acc > currBest:
                currBest = acc
                currFeat = j
        features.append(currFeat)
        print("")
        print("Feature set %s is the best with an accuracy of %.2f%%" % (str(features), currBest * 100))
        if currBest > bestAcc:
            bestAcc = currBest
            bestFeatures = copy.deepcopy(features)
        else:
            print("!!!Accuracy is decreasing!!!")
        print("")        
            
    file.close()
    print("Finished! The best feature set is %s with an accuracy of %.2f%%" % (str(bestFeatures), bestAcc * 100))
    
def backward(fileName):
    file = open(fileName, "r")
    data = file.readlines()
    featureNum = len(data[0].split())
    features = list(range(1, featureNum))
    bestFeatures = []
    bestAcc = 0
    acc = 0

    print("The dataset has %d features and %d instances." % (featureNum - 1, len(data)))
    print("")
    
    acc = nearest(data, features)
    print("Feature(s) %s, the accuracy is %.2f%%" % (str(features), acc * 100))
    print("")
    print("Feature set %s is the best with an accuracy of %.2f%%" % (str(features), acc * 100))
    print("")
    
    #Nested for loop that expand(delete feature) upon the (local)best feature set
    for i in range(1, featureNum - 1):
        currBest = 0
        currFeat = 0
        for j in range(1, featureNum):
            if j not in features:
                continue
            temp = copy.deepcopy(features)
            temp.remove(j)
            acc = nearest(data, temp)
            print("Feature(s) %s, the accuracy is %.2f%%" % (str(temp), acc * 100))
            if acc > currBest:
                currBest = acc
                currFeat = j
        features.remove(currFeat)
        print("")
        print("Feature set %s is the best with an accuracy of %.2f%%" % (str(features), currBest * 100))
        if currBest > bestAcc:
            bestAcc = currBest
            bestFeatures = copy.deepcopy(features)
        else:
            print("!!!Accuracy is decreasing!!!")
        print("")        
            
    file.close()
    print("Finished! The best feature set is %s with an accuracy of %.2f%%" % (str(bestFeatures), bestAcc * 100))

def main():
    
    print("Nearest Neighbor Classifier")
    fileName = input("Enter the name of the data file: ")
    
    print("Which method of feature selection?")
    print("1. Forward Selection")
    print("2. Backward Elimination")
    method = input("")
    
    if method == '1':
        forward(fileName)
    else:
        backward(fileName)
    
if __name__ == "__main__":
    main()