# -*- coding: utf-8 -*-
"""
Created on Tue May 05 15:17:36 2015

@author: Tracy 

This script is for parsing the JSON results MonkeyLearn spits back. 
Fill a csv file with posts to be labeled, one post per row. You will get a 
new file in the same folder that has the original post, MonkeyLearn's label & 
probability that they think their label is correct. 

"""

import requests
import json
import csv
import yaml

original_post_list = []
classified_label_list = []
classified_probability_list = []

# Change to the name of your csv that has the posts to be labeled / scored
f = open('testfile2.csv')
csv_f = csv.reader(f)

# Reads through your csv and aggregates the posts into a giant list
for line in csv_f:
    original_line = line   
    # Each line of the csv shows up as a list, so converting to a string here
    string_line = ''.join(map(str, original_line))    
    original_post_list.append(string_line)        

data = {'text_list': original_post_list}

# Update the project ID & Authorization token below. Info on how to get the
# ID & token are on the site.
response = requests.post(
    "https://api.monkeylearn.com/v2/classifiers/cl_Tnwez9CH/classify/",
    data=json.dumps(data),
    headers={'Authorization': 'Token 79c3017dfabfec4836a4c84ec12e4adf3c92ae50',
            'Content-Type': 'application/json'})

parsed_json = yaml.safe_load(response.text)
list_of_judgements = parsed_json['result']

for item in list_of_judgements:
    post_result = item
    #Dictionary within a list in a list, just gotta clean it up to access
    #the label & probability scores
    post_result_cleaned = post_result[0]
    post_label = post_result_cleaned['label']
    post_label_probability = post_result_cleaned['probability']
    classified_label_list.append(post_label)
    classified_probability_list.append(post_label_probability)
         
 
zipped = zip(original_post_list, classified_label_list, classified_probability_list)

f.close()

#Update the name of the resulting file
with open('newtestfile2.csv', 'wb') as newfile:
    writer = csv.writer(newfile)
    writer.writerows(zipped)

newfile.close() 

print("All done! Check it out!")
