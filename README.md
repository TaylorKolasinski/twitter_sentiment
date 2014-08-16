# Overview

This repo contains two basic approaches for getting the sentiment score of a tweet:

  * Only using the AFFIN library for calculating the score
  * Deriving a more robust score by extrapolating the sentiment of terms not in the AFFIN library

# Usage

To get started, first register an app with Twitter and place all the necessary tokens in the twitterstream.py file. Also in this file, is the url for which tweets to retrieve. Currently it's set to use the streaming api and tracking mentions of 'nyc'.

Next, populate the output.txt. To do this, run the following code in your terminal while in local directory:
```
python twitterstream.py >> libs/output.txt
```

This populates with the output.txt file with the incoming tweets. Stop whenever you feel you have enough tweets. These are the tweets that'll be used for the sentiment analysis.

Next, for the basic analysis, run the sentiment script:
````
python basic/tweet_sentiment.py libs/AFINN-111.txt libs/output.txt
````

tweet_sentiment.py takes two inputs, the AFFIN library and the tweets to be analyzed. The output of this will be printed to the terminal.

To run analysis that will produce a more robust score, you'll first estimate the sentiment score for all the words not in the AFFIN dictionary. The current score calculations are not perfect and rather naive. Will be working on improving them soon.

To get the term sentiments, run:
````
python terms/term_sentiment.py libs/AFINN-111.txt libs/output.txt
````

This creates a new library based on the non AFFIN terms in your tweets. To get the sentiment scores for these, run:

````
python terms/tweet_sentiment.py libs/AFINN-111.txt libs/output.txt libs/term_dictionary.txt
````

