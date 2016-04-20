import nltk
from textblob.classifiers import NaiveBayesClassifier

#Utf 8 support
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

print "Welcom 2 meme guesser!"

#Our testing data features
features = []

#Read in our meme training data
memeTrainList = [];
with open('trainingDataMeme', 'r') as f:
    for line in f:
        line = line.strip()
        memeTrainList.append([line, 'meme'])

#Add the memes to the features
features.extend(memeTrainList)

#Read in our non-meme training data
noMemeTrainList = [];
with open('trainingDataNoMeme', 'r') as f:
    for line in f:
        line = line.strip()
        noMemeTrainList.append([line, 'nomeme'])

#Add the nomemes to the features
features.extend(noMemeTrainList)

#Using a naive bayes Classifier
bClassifier = NaiveBayesClassifier(features)

#Read in our testing
testingList = [];
with open('testingData', 'r') as f:
    for line in f:
        line = line.strip()
        testingList.append(line.split('%')[0])

#Print our testing data
for i in range(0, len(testingList)):
    print testingList[i] + " - this haz " + bClassifier.classify(testingList[i])

#Find our accuracy
testingAccuracy = [];
with open('testingData', 'r') as f:
    for line in f:
        line = line.strip()
        testingAccuracy.append([line.split('%')[0], line.split('%')[1]])

#Times 100 for percent
print("Meme Accuracy: " + str(bClassifier.accuracy(testingAccuracy) * 100) + "%")

#Show our most informative features
bClassifier.show_informative_features(15)
