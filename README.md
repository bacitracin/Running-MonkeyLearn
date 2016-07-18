# Running-MonkeyLearn
Files for working with MonkeyLearn.com's sentiment scoring / machine learning

This script is for parsing the JSON results MonkeyLearn spits back. 
Fill a csv file with posts to be labeled for sentiment, one post per row. You will get a 
new file in the same folder that has the original post, MonkeyLearn's label & 
probability that they think their label is correct. 

Imported Libraries: requests, json, csv, yaml
