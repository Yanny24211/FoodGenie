import os
import cv2  
import numpy as np
from numpy import load
import tensorflow as tf 
from tensorflow import keras

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2" 

classNames = ["banana", "apple", "pear", "grapes", "orange", "kiwi", "watermelon",
             "pomegranate", "pineapple", "mango", "cucumber", "carrot", "capsicum", "onion", "potato", "lemon", "tomato", "raddish", 
             "beetroot", "cabbage", "lettuce", "spinach", "soy beans", "cauliflower", "bell pepper","chilli pepper", 
             "turnip", "corn", "sweetcorn", "sweetpotato", "paprika", "jalepeno", "ginger", "garlic", "peas", "eggplant"]

trainData = load('c:/tempFolder/trainData.npy')
trainFeatures = load('c:/tempFolder/trainFeatures.npy')
testData = load('c:/tempFolder/testData.npy')
largeTestData = load('c:/tempFolder/largeTestData.npy')
testFeatures = load('c:/tempFolder/testFeatures.npy')

print("Finished loading all the data.")

# testingImage = trainData[1]
# cv2.imshow('testingImage', testingImage)
# thisIndex = trainFeatures[1]
# print(classNames[thisIndex])
# cv2.waitKey(0)

print("Train shape: ", trainData.shape)
print("Features shape: ", trainFeatures.shape)
print("Test data shape: ", testData)
print("Test features shape: ", testFeatures)



trainData = trainData/255.0
testData = testData/255.0

model = keras.Sequential([

    keras.layers.Flatten(input_shape=(28,28,3)),

    keras.layers.Dense(512, activation="relu"),

    keras.layers.Dense(36, activation="softmax")
])

print("Finished building the skeleton of the neural network")

model.compile(

    optimizer=tf.optimizers.Adam(), 
    loss = 'sparse_categorical_crossentropy',
    metrics=['accuracy']

)

print("Finished compiling the model.")


loadedModelDir = "c:/tempFolder/model.h5"

if os.path.exists(loadedModelDir):
    model = keras.models.load_model(loadedModelDir)
    print("Loaded the pre-trained model")
else:
    model.fit(trainData, trainFeatures, epoch=100)
    model.save(loadedModelDir)
    print("Trained then saved the model.")


lossValues, accValues = model.evaluate(testData, testFeatures, verbose=1)
print("############# Testing Accuracy: ", accValues)


predictionVal = model.predict(testData)


for predicting, testFeature in zip(predictionVal, testFeatures):
    fruitVegIndex = np.argmax(predicting)
    fruitVegPredicted = classNames[fruitVegIndex]

    fruitVegCorrect = classNames[testFeature]

    print("Predicted class: ", fruitVegPredicted, "  Actual class: ", fruitVegCorrect)




















