import nltk
from textblob.classifiers import NaiveBayesClassifier

#Utf 8 support
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

print "Welcom 2 meme guesser!"

print "Plz wait we is being loaded..."

#Our testing data features
memeFeatures = []
noMemeFeatures = []

#Read in our meme training data
memeTrainList = [];
with open('trainingDataMeme', 'r') as f:
    for line in f:
        line = line.strip().lower()
        memeTrainList.append([line, 'meme'])

#Add the memes to the features
memeFeatures.extend(memeTrainList)

#Read in our non-meme training data
noMemeTrainList = [];
with open('trainingDataNoMeme', 'r') as f:
    for line in f:
        line = line.strip().lower()
        noMemeTrainList.append([line, 'nomeme'])

#Add the nomemes to the features
noMemeFeatures.extend(noMemeTrainList)

#Create a mixed features array
classifierFeatures = [];
classifierFeatures.extend(memeFeatures)
classifierFeatures.extend(noMemeFeatures)


#Using a naive bayes Classifier
bClassifier = NaiveBayesClassifier(classifierFeatures)

#Read in our testing
testingList = [];
with open('testingData', 'r') as f:
    for line in f:
        line = line.strip().lower()
        testingList.append(line.split('%')[0])

#Print our testing data
for i in range(0, len(testingList)):
    print testingList[i] + " - this haz " + bClassifier.classify(testingList[i])

#Find our accuracy
testingAccuracy = [];
with open('testingData', 'r') as f:
    for line in f:
        line = line.strip().lower()
        testingAccuracy.append([line.split('%')[0], line.split('%')[1]])

#Times 100 for percent
print("Meme Accuracy: " + str(bClassifier.accuracy(testingAccuracy) * 100) + "%")

#Show our most informative features
bClassifier.show_informative_features(15)
