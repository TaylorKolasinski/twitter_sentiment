# Overview

This repo contains two basic approaches for getting the sentiment score of a tweet:

  * Only using the AFFIN library for calculating the score
  * Deriving a more robust score by extrapolating the sentiment of terms not in the AFFIN library


# Usage

To get started, first register an app with Twitter and place all the necessary tokens in the twitterstream.py file. Also in this file, is the url for which tweets to retrieve. Currently it's set to use the streaming api and tracking mentions of 'nyc'.

Next, populate the output.txt. To do this, run the following code in your terminal while in local directory:
```
python twitterstream.py >> output.txt
```

This populates with the output.txt file with tweets being received. Stop whenever you feel you have enough tweets.

Next, run the sentiment script:
````
python tweet_sentiment.py AFINN-111.txt output.txt
````

tweet_sentiment.py takes two inputs, the AFFIN library and the tweets to be analyzed. The output of this will be printed to the terminal.