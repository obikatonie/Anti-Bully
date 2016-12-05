import string

badwords = []
for line in open("badwords.txt"):
    for word in line.split( ):
        badwords.append(word)

import pandas

data = pandas.read_csv("datasets/data.csv", names = ["label_bullying", "text_message"]).values  # assumes train.csv is in the same folder as this notebook

import sklearn
y = data[1:,0]
X = data[1:,1]

predictions = []
for tweet in X:
    # get rid of punctuation
    tweet = "".join(l for l in tweet if l not in string.punctuation)
    tweet = tweet.lower()
    bullying = False
    for word in tweet.split(" "):
        if word in badwords:
            bullying = True
            predictions.append("1")
            break
    if bullying == False:
        predictions.append("0")


from sklearn.metrics import accuracy_score
print accuracy_score(y, predictions)
