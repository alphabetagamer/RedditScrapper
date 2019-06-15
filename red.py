# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:29:43 2018

@author: lokin
"""

import praw
import random
import urllib.request

reddit = praw.Reddit(client_id='******',
                     client_secret='***',
                     password='**',
                     user_agent='Data Scraping',
                     username='****3')
#for submission in reddit.subreddit('gentlemanboners').hot(limit=20) :
for submission in reddit.redditor('dendritesofdendrites').submissions.top('all') :
    if not submission.stickied:
        img_name = random.randrange(0, 8989) 
        a=submission.url.split('.')
       
        if a[0]!='https://gfycat':
            if submission.url[-4:]!='.png' and submission.url[-4:]!='.jpg':
                submission.url=submission.url+'.png'
            else:
                pass
            print(submission.url)
            full_name = str(img_name) + '.png'
            urllib.request.urlretrieve(submission.url,full_name)

      

