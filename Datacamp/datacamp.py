# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 22:21:49 2017

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
 
pp = pprint.PrettyPrinter(indent=4)
 
http = urllib3.PoolManager()
r = http.request('GET','https://www.datacamp.com/courses/tech:sql')

soup = Soup(r.data,'html.parser')
courses=soup.find_all('div',class_='course-block')
print(courses)
for course in courses:
    course_link='https://www.datacamp.com'+course.a['href']
    course_title=course.h4.get_text()
    course_folder=os.path.join('C:\\Users\\IBM_ADMIN\\Desktop\\personal\\learning\\Data_Camp_sql'+course.a['href'])
    os.makedirs(course_folder)
    #print('course_link:', course_link)
    
    r = http.request('GET',course_link)
    soup = Soup(r.data,'html.parser')
    #print(soup)
    #print(soup.find_all('h4',class_='chapter__title'))
    slides_link=[]
    chapter_names=[]
    for exercise in  soup.find_all('a',class_='chapter__exercise-link'):
        if exercise['href'].endswith('ex=1'):
            chapter_name=str(exercise['href'])
            chapter_name=chapter_name.replace('campus','www')
            chapter_name=chapter_name.replace(course_link,'')
            chapter_name=re.sub(r'/(.*?)\?ex=1',r'\1',chapter_name)
            chapter_names.append(chapter_name)
            #print(soup.find_all('a',class_='chapter__exercise-link'))
        
            r2 = http.request('GET',exercise['href'])
            soup = Soup(r2.data,'html.parser')
            for script in soup.find_all('script'): 
                if script['data-reactid']=='35':
                    #print(script.get_text())
                    a=script.get_text()
                    slides_link.append(re.sub(r'(.*?)"slides_link":"(.*?.pdf)"(.*)',r'\2',a))
                    #print('\n\n\n\n')
    for i,chapter_link in enumerate(slides_link):
        #print(i)
        chapter_data=http.request('GET',chapter_link)
        chapter_pdf=open(os.path.join(str(course_folder+'\\chapter'+ str(i)+'_'+str(chapter_names[i]) +'.pdf')),'wb')
        chapter_pdf.write(chapter_data.data)
        chapter_pdf.close()
