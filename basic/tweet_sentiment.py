import sys
import json

# Create dictionary of AFINN - a list of English words rated for valence with an integer between minus five (negative) and plus five (positive)
def affinDictionary(sys):
    affinfile = open(sys)
    scores = {}
    for line in affinfile:
      term, score = line.split("\t")
      scores[term] = int(score)
    return scores

def sentiment(sys, sys2):
    #Build AFINN dictionary
    dic = affinDictionary(sys)

    tweets = open(sys2)
    for line in tweets:
      if len(line) > 10:
        if 'text' in json.loads(line):
          words = json.loads(line)['text'].split()
          sentiment_score = 0

          for word in words:
            word = word.encode('utf-8')

            #need to improve on cleaning up words and emojis
            word = str(word).translate(None, '!@#.$%&*!?:,\'_-+={}[]\\|;<>/~`()"').lower()
            if word in dic.keys():
              sentiment_score = sentiment_score + dic[word]

          print "Tweet: " + json.loads(line)['text']
          print "Tweet sentiment: " + str(sentiment_score)
          print

def main():
    sentiment(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
