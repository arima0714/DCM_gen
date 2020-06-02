#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import os
import time

from urllib import request
from bs4 import BeautifulSoup

import glob
import re
from gensim.models import word2vec


# In[2]:


def nocScraping(novelID, limit=0):
   
   #set UA
   header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"}
   
   #set cookie
   cookie = {"over18": "yes"}
   
   #親URLをセット
   chapterlistUrl = "https://novel18.syosetu.com/" + str(novelID) + "/"
   responseCL  = requests.get(url=chapterlistUrl, headers=header, cookies=cookie)
   chapterlistHtml = responseCL.content
   soupCL = BeautifulSoup(chapterlistHtml, "html.parser")
   sublist = soupCL.find_all("dl", attrs={"class","novel_sublist2"})
   #print(len(sublist))
   
   
   novelDirPass = "data/" + novelID
   count = 1
   
   if(limit == 0):
       countlimit = len(sublist) + 1
   else:
       countlimit = limit + 1
   
   while(count < countlimit):
       #set url
       url = "https://novel18.syosetu.com/" + str(novelID) + "/" + str(count) + "/"

       #get html
       response  = requests.get(url=url, headers=header, cookies=cookie)
       html = response.content

       #set BeautifulSoup
       soup = BeautifulSoup(html, "html.parser")

       #scraping
       mainText = soup.find("div", attrs={"id":"novel_honbun"})
       try:
           mainTextLines = mainText.find_all("p")
       except AttributeError:
           pass

       allText = ""

       for mainTextLine in mainTextLines:
           text = str(mainTextLine)
           text = re.sub("<p.*\">","",text)
           text = re.sub("</p>","",text)
           text = text.replace("<br/>","")
           if(text != ""):
               allText = allText + text + "\n"

       allText = re.sub("\n\n","\n",allText)
       allText = re.sub("　","",allText)
       #print(allText)
       
       os.makedirs(novelDirPass, exist_ok=True)
       newFilePass = novelDirPass + "/" + novelID + "_" + str(count) + ".txt"
       if not os.path.isfile(newFilePass):
           with open(newFilePass, mode="w", encoding="UTF-8") as f:
               f.write(allText)
       
       count = count +1
       
def getNcode(limit):
   response = requests.get("https://api.syosetu.com/novel18api/api",params={"out":"json","nocgenre":1,"sasie":0,"type":"re","ispickup":1,"lim":limit,"of":"n"})
   #print(response.json()[1]["ncode"])
   count = 1
   ncodelist=[]
   
   while(count < limit+1):
       ncodelist.append(response.json()[count]["ncode"])
       count = count + 1
   #print(ncodelist)
   return ncodelist
   

def getNovelText(number,limit=0):
   ncodelist = getNcode(number)
   count = 1
   while(count < number):
       nocScraping(ncodelist[count],limit)
       count = count + 1
       print("count = "+str(count)+" ("+str((count/number)*100)+"%)")
       time.sleep(1.5)


# In[3]:


getNcode(10) # 関数テスト


# In[4]:


getNovelText(10,10)


# In[5]:


word_list = []

from janome.tokenizer import Tokenizer
t = Tokenizer()
def extract_words(text):
  tokens = t.tokenize(text)
  return [token.base_form for token in tokens if token.part_of_speech.split(",")[0] in ["名詞", "動詞", "形容詞"]]


# In[6]:


for path in glob.glob("./data/*/*.txt"):
  with open(path , encoding="UTF-8") as f:
    try:
      for s_line in f:
        s_line = s_line.replace("<ruby><rb>","")
        s_line = s_line.replace("</rb><rp>(</rp><rt>","")
        s_line = s_line.replace("</rt><rp>(</rp></ruby>","")
        word_list.append(extract_words(s_line))
    except UnicodeDecodeError:
      pass

with open("./wordlist.txt", mode="w", encoding="UTF-8") as f:
  f.write(str(word_list))

model = word2vec.Word2Vec(word_list , size=100, min_count=5, window=5, iter=100)
model.save("dosukebe.model")


# In[7]:


model.most_similar("オチンチン")


# In[8]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'Untitled.ipynb'])


# In[ ]:




