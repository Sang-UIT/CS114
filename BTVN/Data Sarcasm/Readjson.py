import json
import pandas as pd
import urllib.request
import requests
import urllib
from urllib.request import urlopen
import urllib3
import os
f = open("Link_json.txt", "r")
f1 = open("is.txt", "w",encoding="utf-8")
f2 = open("hl.txt", "w",encoding="utf-8")
f3 = open("al.txt", "w",encoding="utf-8")
for x in f:
    url = x
    try:
        for line in urllib.request.urlopen(url):
            s=line.decode('utf-8')
            s=s.replace('{', '')
            s=s.replace('}', '')
            s=s.replace('"', '')
            s=s.replace('[','')
            s=s.replace(']','')
            s=s+", "
            a0=s.find("is_sarcastic:")
            a1=s.find(",",s.find("is_sarcastic:"))
            f1.write(s[a0:a1].replace('is_sarcastic:','').replace(' ','')+"\n")
            
            a0=s.find("headline:")
            a1=s.find(",",s.find("headline:"))
            f2.write(s[a0:a1].replace('headline:','')+"\n")
            
            a0=s.find("article_link:")
            a1=s.find(",",s.find("article_link:"))
            f3.write(s[a0:a1].replace('article_link:','').replace('\n','')+"\n")
    except:
        print("Json eror")
f1.close()
f2.close()
f3.close()
with open("is.txt", 'r',encoding="utf-8") as r, open('nis.txt', 'w',encoding="utf-8") as o:
    o.write('is_sarcastic\n')
    for line in r:
        #strip() function
        if line.strip():
            o.write(line)
with open("hl.txt", 'r',encoding="utf-8") as r, open('nhl.txt', 'w',encoding="utf-8") as o:
    o.write('headline\n')
    for line in r:
        #strip() function
        if line.strip():
            o.write(line)  
with open("al.txt", 'r',encoding="utf-8") as r, open('nal.txt', 'w',encoding="utf-8") as o:
    o.write('article_link\n')
    for line in r:
        #strip() function
        if line.strip():
            o.write(line)      
with open('nis.txt', 'r', encoding="utf-8") as r1, open('nhl.txt', 'r', encoding="utf-8") as r2, open('nal.txt','r', encoding="utf-8") as r3, open('data.csv','w',encoding="utf-8") as o:
    while True:
        s1= r1.readline()
        s2= r2.readline()
        s3= r3.readline()
        if not (s2.strip()):
            break
        o.write(s1.replace('\n','')+","+s2.replace('\n','')+","+s3.replace('\n','')+"\n")
os.remove("al.txt")
os.remove("hl.txt")
os.remove("is.txt")
os.remove("nis.txt")
os.remove("nal.txt")
os.remove("nhl.txt")

