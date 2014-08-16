import sys
import json
import string
import re
import math
from decimal import *

def dictionary(sys):
    affinfile = open(sys)
    scores = {}
    for line in affinfile:
      term, score = line.split("\t")
      scores[term] = int(score)
    return scores

def sentiment(sys, sys2):
    dic = dictionary(sys)
    tweets = open(sys2)
    additional_scores = {}
    new_score = {}
    for line in tweets:
      if len(line) > 10:
        if 'text' in json.loads(line):
          words = json.loads(line)['text'].split()
          tweet_information = get_known_score(line, words, dic)

          for word in tweet_information['tweet']:
            if word not in dic.keys():
              # create new entry for word, else add
              if word not in additional_scores:
                word = word.encode('utf-8')
                #need to improve on cleaning up words and emojis
                word = str(word).translate(None, '!@#.$%&*!?:,\'_-+={}[]\\|;<>/~`()"').lower()
                additional_scores[word] = {'pos_count': int(tweet_information['pos_count']), 'neg_count': int(tweet_information['neg_count'])}
              else:
                additional_scores[word] = {'pos_count': additional_scores[word]['pos_count'] + int(tweet_information['pos_count']), 'neg_count': additional_scores[word]['neg_count'] + int(tweet_information['neg_count'])}

          append_new_term_dictionary(additional_scores)

# Naively calculates the sentiment scores for terms not in AFFIN library and creates a 2nd library for them
def append_new_term_dictionary(additional_scores):
  # Need to find a better method for approximating and bounding scores
  # Proxy method for term scores
  with open('libs/term_dictionary.txt', 'w') as f:
    for word in additional_scores:
      if additional_scores[word]['neg_count'] != 0 and additional_scores[word]['pos_count'] != 0:
        r = Decimal( additional_scores[word]['pos_count'])/Decimal(additional_scores[word]['neg_count'])
        if r > 0:
          rlog = math.floor((math.log(r)*4))
        elif r < 0:
          rlog = math.ceil((math.log(r)*4))
        else:
          rlog = 0
      elif additional_scores[word]['neg_count'] != 0 and additional_scores[word]['pos_count'] == 0:
        r = -additional_scores[word]['neg_count']
        rlog = -additional_scores[word]['neg_count']
      elif additional_scores[word]['neg_count'] == 0 and additional_scores[word]['pos_count'] != 0:
        r = additional_scores[word]['pos_count']
        rlog = additional_scores[word]['pos_count']
      else:
        r = 0
        rlog = 0.0


      row = str(word) + "\t" + str(int(rlog))
      print row
      f.write("%s\n" % str(row))

#gets the tweet's sentiment score and counts of negative/positive known words in tweet
def get_known_score(line, words, dic):
    pos_count = 0
    neg_count = 0
    sentiment_score = 0

    for word in words:
      if word in dic.keys():
         sentiment_score = sentiment_score + dic[word]
         if dic[word] > 0:
          pos_count = pos_count + 1
         else:
          neg_count = neg_count + 1
    tweet_information = {"tweet": words, "sentiment_score": str(sentiment_score), "pos_count": str(pos_count), "neg_count": str(neg_count)}
    return tweet_information

def main():
    sentiment(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
