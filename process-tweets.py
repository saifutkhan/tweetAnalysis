# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:50:33 2018
Copy Right
@author: skhan
version 1: build dictionary cache, gather tweets
           create pie chart of simple sentiment analysis
           methods for building and checking words. Produce list of valid words
           build word vectors from bag of words

Acknowledgements:
    Asma Sultan for gathering bag of words and gold data
           
"""
import numpy as np
import json
from textblob import TextBlob
import tweepy
import sys, os
import matplotlib.pyplot as plt
import pandas as pd
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
import csv

bagofwords=['gold', 'stock', 'price', 'trade', 'down', 'gain', 'loss', 'high', 'low', 'spot']

# builde dictionary cache in memory from dictionary on disk
def openDictionary(lang):
    if (lang == 'en'):
        with open("C:\\Users\\skhan\\semesters\\201920\\capstone\\gold-prices\\Data\\wordsEn.txt") as words:
            DictCache = set(word.strip().lower() for word in words)
    return DictCache
            
# create a list of words to be used in analysis
def wordsCheck(words, Dict):

    validWords=[]
    
    for word in words:
        if (word.lower() in Dict) or (pos_tag(word_tokenize(word))[0][1] == 'NN' ):
            validWords.append(word)
    
    return removeStopwords(validWords)

def removeStopwords(wordlist):
    #saif: TODO add custom stopwords
    stopw=set(stopwords.words('english'))
    qwords=[w for w in wordlist if not w in stopw]
    return qwords

# change words into word vector
def wordVectors(words):
    vector={}
    for s in bagofwords:
        vector[s]=0
    for word in words:
        for bagword in bagofwords:
            if word.lower() == bagword.lower():
                vector[word.lower()]=vector[word.lower()]+1
    return vector

def vectorCSV(vector, file):
    with open(file, 'a') as f:
        writer=csv.writer(f)
        writer.writerow(vector.keys())
        writer.writerow(vector.values())
        

# top level data directory
topdatadir="C:\\Users\\skhan\\semesters\\201920\\capstone\\gold-prices\\Data"
# tweet data diretory
tweetdatadir="C:\\Users\\skhan\\semesters\\201920\\capstone\\gold-prices\\Data\\tweets"
# read the json file for specific dates
for dir in os.listdir(tweetdatadir):
    print(dir)
    datedir=os.path.join(tweetdatadir,dir)
    print(datedir)
    blobs=[]
    if os.path.isdir(datedir):
        for file in os.listdir(datedir):
            tfile=os.path.join(datedir,file)
            print(tfile)
            try:
                with open(tfile,'r') as f:
                    line=f.readline()
                    while len(line) > 0:
                        tweet=json.loads(line)
                        blob=TextBlob(tweet['full_text'])
                        blobs.append(blob.words)
                        line=f.readline()
            except Exception as err:
                    print(err)
        blobwords=[lstlst for sublist in blobs for lstlst in sublist]
        words=wordsCheck(blobwords, openDictionary('en'))
        vectors=wordVectors(words)
        vectors['date']=dir
        vectorCSV(vectors, topdatadir+"\\data.csv")

'''
                with open(tfile) as f:
#            jsondata=pd.read_json(file,chunksize=1,lines=True,encoding='utf-8')
#                jsondata=pd.read_json(file,encoding='utf-8')
                    data=json.load(f)
#                    for data in jsondata:
                    print(data['text'])
            except Exception as err:
                print(err)
                #pass
 #           print(date)
#           text=jsondata['text']
#            text=text + jsondata['extended_tweet'].get('full_text')
#
'''
    