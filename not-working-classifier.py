import pandas

data = pandas.read_csv("datasets/data.csv", names = ["label_bullying", "text_message"]).values  # assumes train.csv is in the same folder as this notebook

import sklearn
from sklearn.cross_validation import train_test_split
y1 = data[1:,0]
X1 = data[1:,1]
X, X_dev, y, y_dev = train_test_split(X1, y1, test_size=0.2, random_state=42)

tweets = X;
#tweet = "hello I like pie"


#probs of label bully
bully_prob = 0;
non_bully_prob = 0;
for i in range(len(tweets)):
    if (y[i] == "1"):
        bully_prob += 1;
#print bully_prob
bully_prob /= 1.0 * len(tweets);
non_bully_prob = 1 - bully_prob;
#print len(tweets)
#print bully_prob

#feat count of in label
bully_count = {};
non_bully_count = {};
total_count = {};
for i in range(len(tweets)): #list of tweets
    t = tweets[i];
    for word in t.split(" "):
        if (word in total_count.keys()):
            total_count[word] += 1;
        else:
            total_count[word] = 1;

        if (word not in bully_count.keys()):
            bully_count[word] = 0;
        if (word not in non_bully_count.keys()):
            non_bully_count[word] = 0;

        if (y[i] == "1"):
            bully_count[word] += 1;

        else:
            non_bully_count[word] += 1;

#prob that word is in a class
feat_bully_prob = {};
feat_non_bully_prob = {};
for t in tweets:
    for word in t.split(" "):
        feat_bully_prob[word] = 1.0 * bully_count[word] / total_count[word];
        feat_non_bully_prob[word] = 1.0 * non_bully_count[word] / total_count[word];
        # print(word, feat_bully_prob[word], feat_non_bully_prob[word]);
#prob that tweet is bully or not


predictions = []
for tweet in X_dev:
    for word in tweet:
        in_bully_prob = 1;
        not_in_bully_prob = 1;
        if (word not in feat_bully_prob.keys()):
            feat_bully_prob[word] = 0.5;
            feat_non_bully_prob[word] = 0.5;
        in_bully_prob *= (feat_bully_prob[word] + 0.5) * (bully_prob + 1);
        not_in_bully_prob *= (feat_non_bully_prob[word] + 0.5) * (non_bully_prob + 1);
        # print(in_bully_prob, not_in_bully_prob);

    if (in_bully_prob > not_in_bully_prob):
        predictions.append("0")
    else:
        predictions.append("1")

from sklearn.metrics import accuracy_score
print accuracy_score(y_dev, predictions)
print ("dev",y_dev)
print ("predictions: ", predictions)
