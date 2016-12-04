import string
tweets = ["i love!!!,>Myself", "you suck", "kill yourself"]

badwords = []
for line in open("badwords.txt"):
    for word in line.split( ):
        badwords.append(word)

for tweet in tweets:
    # get rid of punctuation
    tweet = "".join(l for l in tweet if l not in string.punctuation)
    tweet = tweet.lower()
    bullying = False
    for word in tweet.split(" "):
        if word in badwords:
            print "bullying"
            bullying = True
            break
    if bullying == False:
        print "not bullying"
