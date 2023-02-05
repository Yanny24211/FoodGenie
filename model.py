import os
import cv2  
import numpy as np
from numpy import save

classNames = ["banana", "apple", "pear", "grapes", "orange", "kiwi", "watermelon",
             "pomegranate", "pineapple", "mango", "cucumber", "carrot", "capsicum", "onion", "potato", "lemon", "tomato", "raddish", 
             "beetroot", "cabbage", "lettuce", "spinach", "soy bean", "cauliflower", "bell pepper","chilli pepper", 
             "turnip", "corn", "sweetcorn", "sweet potato", "paprika", "jalepeño", "ginger", "garlic", "peas", "eggplant"]

trainDataArray = []

trainFeaturesArray = []

print("loading the train data")

imgDir = "C:/Users/pra_d/OneDrive/Desktop/Anmol/Projects/WebDev/repos/OpticGenie/archive/train"

for subDirectory, directory, files in os.walk(imgDir):

    for theFile in files:
        theImg = cv2.imread(os.path.join(subDirectory, theFile))

        if(theImg is None):
            print("invalid image")
        else:
            print(subDirectory, theFile)

            resizedImage = cv2.resize(theImg,(28,28), interpolation=cv2.INTER_AREA)
            checkTheSize = resizedImage.shape[0]

            if(checkTheSize==28):
                trainDataArray.append(resizedImage)
                theIndex = classNames.index(os.path.basename(subDirectory))
                trainFeaturesArray.append(theIndex)

trainData = np.array(trainDataArray)
trainFeatures = np.array(trainFeaturesArray)

print("Finished gay.")
print("Number of training records: ", trainData.shape[0])

print(trainData.shape)
print(trainFeatures.shape)


testImage = trainData[4]
cv2.imshow("Test image", testImage)
theIndex2 = trainFeatures[4]
print(classNames[theIndex2])

testImage2 = trainData[5]
cv2.imshow("Test image", testImage2)
theIndex3 = trainFeatures[5]
print(classNames[theIndex3])

cv2.waitKey(0)




















































