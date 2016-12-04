#!/usr/bin/python

from __future__ import division
from collections import Counter, defaultdict
from math import log,isinf
import csv
import codecs
import re
import random
import json

# Import our library functions from lib.py
# Feel free to take a look at these if you're feeling adventurous!
from lib import *

# -----------------------------------------------------------------------------
# BEGIN NAIVE BAYES CODE
# -----------------------------------------------------------------------------

def featurize(datum):
    """
    Featurize a particular example.
    @param datum: This is a single datum that we are featurizing
    @return A set of features for that datum. For example, unigram and bigram features.
    For the input 'Gabor is awesome', the output would be, set('Gabor',
    '^_Gabor', 'is', 'Gabor_is', 'awesome', 'is_awesome').
    """
    features = []
    last_word = '^'
    for word in lower(datum):
        features.append(word)
        features.append(last_word + "_" + word)
        last_word = word
    return set(features)


def train_classifier(data, class_of_interest):
  """
  Train a Naive Bayes classifier from a given dataset.
  @param data:Datum[] The dataset to train from, as a list of Datum objects.
                      see load_data_from_csv, which returns a triple of such lists.
  @param class_of_interest:String The class we are classifying into (e.g., 'Food')
  @return A classifier object. This is just a triple of the tables for p(c) and
                                p(f | c_true) and p(f | c_false).
  """

  # 1. Collect count(c)
  # The total number of times we see each label.
  # This should have counts for 'True' (needs food), and 'False' (doesn't need food)
  total_counts = Counter()
  for datum in data:
    if datum.answer() == class_of_interest:
      total_counts[True] += 1
    else:
      total_counts[False] += 1

  # 2. Compute p(c)
  # The probability of each label. This should mirror total_counts.
  total_probs = Counter()
  total_probs[True] = total_counts[True] / (total_counts[True] + total_counts[False])
  total_probs[False] = total_counts[False] / (total_counts[True] + total_counts[False])

  # 3. Collect count(f | c)
  true_counts = Counter()
  false_counts = Counter()
  # For each tweet in our dataset...
  for datum in data:
    features = featurize(datum)
    for feature in features:
      if datum.answer() == class_of_interest:
        true_counts[feature] += 1
      else:
       false_counts[feature] += 1
  # Add an UNK count
  true_counts['__UNK__'] = 10.0
  false_counts['__UNK__'] = 10.0
  # Smooth the counts (add 0.1 fake counts to each feature)
  features = set(true_counts + false_counts)
  for feature in features:
      true_counts[feature] += 1.0
      false_counts[feature] += 1.0

  # 4. Compute p(f | c)
  true_probs = Counter()
  false_probs = Counter()
  # p(f | c) = count(f, c) / count(c)
  for feature in true_counts:
      true_probs[feature] = true_counts[feature] / total_counts[True];
  for feature in false_counts:
      false_probs[feature] = false_counts[feature] / total_counts[False];

  # 5. Return the model
  return [total_probs, true_probs, false_probs]


def classify(model, datum):
  """
  Predict the label for a datum. This function should take a datum (without a known label!), and
  output True if the datum is about food, and false otherwise.
  @param model The triple that contains the Naive Bayes counts. This is the output
               of the function train_classifier().
  @param datum A datum that we should classify into the 'Food' versus 'Not Food' category.
  @return True if the datum is about food, and false otherwise.
  """

  # Unpack the model
  [total_probs, true_probs, false_probs] = model
  # Start the log scores at 0.0
  true_score = 0.0
  false_score = 0.0

  # Featurize the input
  features = featurize(datum)

  # Multiply in p(c)
  true_score += log(total_probs[True])
  false_score += log(total_probs[False])

  # Multiply in p(f | c) for each f
  for feature in features:
    if feature in true_probs:
      true_score += log(true_probs[feature])
    else:
      true_score += log(true_probs['__UNK__'])
    if feature in false_probs:
      false_score += log(false_probs[feature])
    else:
      false_score += log(false_probs['__UNK__'])

  # Some error checking
  if isinf(true_score) or isinf(false_score):
    print "WARNING: either true_score or false_score is infinite"

  # Return the most likely class.
  return true_score > false_score


if __name__ == "__main__":
  """
    The entry point of your code.
  """
  # The free variables to set
  filename = 'datasets/data.csv'
  target_class = '1'

  # Load the data
  [dev_data, train_data, test_data] = load_data_from_csv(filename)

  # Train the classifier
  classifier = train_classifier(train_data, target_class)

  # Evaluate the classifier
  in_class = []
  not_in_class = []
  for datum in dev_data:
    if classify(classifier, datum):
      in_class.append(datum)
    else:
      not_in_class.append(datum)
  evaluate(target_class, in_class, not_in_class)

  # Start a web server for the live demo
#  start_server(lambda x: classify(classifier, x), 4242)
