import nltk
from textblob.classifiers import NaiveBayesClassifier

#Utf 8 support
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#Create our features and lables
#1 for meme, 0 for not meme
features = []

#Read in our meme training data
memeTrainList = [];
with open('trainingDataMeme', 'r') as f:
    for line in f:
        memeTrainList.append([line.split('\n')[0], 'meme'])

#Add the memes to the features
features.extend(memeTrainList)

#Read in our non-meme training data
noMemeTrainList = [];
with open('trainingDataNoMeme', 'r') as f:
    for line in f:
        noMemeTrainList.append([line.split('\n')[0], 'nomeme'])

#Add the nomemes to the features
features.extend(noMemeTrainList)

#Using a naive bayes Classifier
bClassifier = NaiveBayesClassifier(features)

#Read in our testing
testingList = [];
with open('testingData', 'r') as f:
    for line in f:
        testingList.append(line.split('%')[0])

#Print our testing data
for i in range(0, len(testingList)):
    print testingList[i] + "- this haz " + bClassifier.classify(testingList[i])

#Find our accuracy
testingAccuracy = [];
with open('testingData', 'r') as f:
    for line in f:
        testingList.append([line.split('%')[0], line.split('%')[1]])
print("Accuracy: " + str(bClassifier.accuracy(testingAccuracy)) + "%")

#Show our most informative features
bClassifier.show_informative_features(5)
