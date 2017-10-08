# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:55:36 2017

@author: Pavan
"""


 
import pprint
import urllib3, certifi
#import simplejson
import sys
import subprocess
import json
import re
import os
from bs4 import BeautifulSoup as Soup
from datetime import datetime
import requests
from lxml import html

 

url = 'http://www.datacamp.com/login/'
login_data = dict(login='pavanteja.m@outlook.com', password='mach2012')
session = requests.session()

r = session.post(url, data=login_data)
#print(r.text)
r2 = session.get('https://campus.datacamp.com/courses/natural-language-processing-fundamentals-in-python/building-a-fake-news-classifier?ex=1')
print(r2.content)