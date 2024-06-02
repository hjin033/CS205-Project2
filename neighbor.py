import math

def nearest(data, features):
    correct = 0
    closestDist = 10
    guess = 1
    distance = 10
    
    for i in range(len(data)):
        testData  = data[i].split()
        for j in range(len(data)):
            currentData = data[j].split()
            if testData == currentData:
                continue
            distance = 0
            for f in features:
                distance += (float(testData[f]) - float(currentData[f])) ** 2
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
    featureNum = len(data[0].split()) - 1
    features = []
    bestFeatures = []
    bestAcc = 0
    
    for i in range(0, featureNum):
        currBest = 0
        for j in range(i, featureNum):
            currBest = max(nearest(data, features), currBest)
            
            
    
    file.close()

def main():
    '''
    print("Nearest Neighbor Classifier")
    fileName = input("Enter the name of the data file: ")
    
    print("Which method of feature selection?")
    print("1. Forward Selection")
    print("2. Backward Elimination")
    method = input("")
    '''
    
    '''
    file = open("CS205_large_Data__6.txt", "r")
    data = file.readlines()
    features = [29, 4, 1]
    #print(data[0].split())
    
    acc = nearest(data, features)
    print(acc)
    '''
    
    
if __name__ == "__main__":
    main()