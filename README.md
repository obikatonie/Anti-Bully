# Anti-Bully
Hack Harassment EV Hacks II  
Best Application award winner at EV Hacks II (uses machine learning to detect cyberbullying and automatically warn the user)  
Devpost Submission: https://devpost.com/software/anti-bully

##Inspiration
Cyberbullying is an extremely prevalent issue in the modern digital world. Yet many social media platforms such as Twitter don’t have intelligent cyberbullying detection systems so they don’t effectively address this issue. Because of this, we wanted to create a classifier using artificial intelligence to determine whether a tweet is cyberbullying or not.

##What it does
Our project is a twitter bot that uses a machine learning classifier to detect cyberbullying and automatically reply to the tweet to warn the user not to bully. We chose Twitter for this project because it was simple to search through tweets and reply with a bot, but in the future, we could expand this project for other social media platforms.

##How we built it
We used Python for the entire project, utilizing the Twitter API for searching for tweets and replying automatically. We used a Naive Bayes machine learning classifier (uses conditional probability concepts) to calculate the probability that a given tweet is harassment or not.

##Challenges we ran into
The first main challenge we ran into was finding a good dataset. Not many well labeled cyberbullying datasets exist, and we spent many hours trying to find a good dataset. We also had difficulty getting the classifier to work (tokenizing the input tweets) and dealing with unknown (previously unencountered words). Furthermore, since we were using a free version of the twitter API, there was a hard limit on the number of API requests we could make, causing many delays in testing.

##Accomplishments that we're proud of
We achieved a very high accuracy of 93%, which is much better than most existing models which only achieve 50-70%. This accuracy could be improved even further if we had a better labeled dataset (the one we used had many mislabeled tweets which threw off the classifier).

##What we learned
We learned how to use the Twitter API from scratch, as well as how to code an effective naive bayes classifier. We also realized that finding good data was necessary for an accurate algorithm.

##What's next for Anti Bully
In the future, we plan on expanding the model to other social media platforms besides just Twitter (such as facebook, reddit, and instagram). We also hope to find a better dataset and achieve even higher accuracy.
