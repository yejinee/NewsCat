import requests
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen
import matplotlib.pyplot as plt
from konlpy.tag import Okt
import re
import sys
from wordcloud import WordCloud
from selenium import webdriver
from time import sleep
import numpy as np
import pandas as pd


def hank_pol_crawling():

    hankyung_politics_head=[]
    hankyung_politics_url=[]
    hankyung_politics_contents=[]
    kkk=[]

    for i in range(1,6):
        try :
            site = "https://www.hankyung.com/politics?page={}".format(i)
            res = requests.get(site, headers={"User-Agent": "Mozilla/5.0"})
            bs =BeautifulSoup(res.text, 'lxml') #lxml
            politics = bs.select('ul.list_basic > li > div.article > h3.tit > a')
        
            for k in politics:
                hankyung_politics_head.append(k.text)
                hankyung_politics_url.append(k.attrs['href'])
            
                hankyung_p_url = k.attrs['href']
                res2 = requests.get(hankyung_p_url, headers={"User-Agent": "Mozilla/5.0"})
                bs2 =BeautifulSoup(res2.text, 'lxml') #lxml
                ttp = bs2.find('div',{'id':'articletxt'}).find_all(text=True)
                for j in ttp:
                    kkk.append(j.replace("\n","").replace("\t",""))
                hankyung_politics_contents.append(' '.join(kkk))
                kkk=[]
                time.sleep(0.03)
        except:
            pass
    hankyung_p1= pd.DataFrame(hankyung_politics_head, columns= ['headline'])
    hankyung_p3= pd.DataFrame(hankyung_politics_url, columns= ['url'])
    hankyung_p2= pd.DataFrame(hankyung_politics_contents, columns= ['contents'])
    hankyung_p=pd.concat([(pd.concat([hankyung_p1,hankyung_p2],axis=1)),hankyung_p3],axis=1)
    hankyung_p['category'] = '정치'
    hankyung_p['name'] = '한국경제'

    return hankyung_p



def hank_eco_crawling():
    
    hankyung_economy_head=[]
    hankyung_economy_url=[]
    hankyung_economy_contents=[]
    kkk=[]

    for i in range(1,6):
        try :
            site = "https://www.hankyung.com/economy?page={}".format(i)
            res = requests.get(site, headers={"User-Agent": "Mozilla/5.0"})
            bs =BeautifulSoup(res.text, 'lxml') #lxml
            economy = bs.select('ul.list_basic > li > div.article > h3.tit > a')
        
            for k in economy:
                hankyung_economy_head.append(k.text)
                hankyung_economy_url.append(k.attrs['href'])
            
                hankyung_e_url = k.attrs['href']
                res2 = requests.get(hankyung_e_url, headers={"User-Agent": "Mozilla/5.0"})
                bs2 =BeautifulSoup(res2.text, 'lxml') #lxml
                ttp = bs2.find('div',{'id':'articletxt'}).find_all(text=True)
                for j in ttp:
                    kkk.append(j.replace("\n","").replace("\t",""))
                hankyung_economy_contents.append(' '.join(kkk))
                kkk=[]
                sleep(0.03)
        except:
            pass
    hankyung_e1= pd.DataFrame(hankyung_economy_head, columns= ['headline'])
    hankyung_e3= pd.DataFrame(hankyung_economy_url, columns= ['url'])
    hankyung_e2= pd.DataFrame(hankyung_economy_contents, columns= ['contents'])
    hankyung_e=pd.concat([(pd.concat([hankyung_e1,hankyung_e2],axis=1)),hankyung_e3],axis=1)
    hankyung_e['category'] = '경제'
    hankyung_e['name'] = '한국경제'

    return hankyung_e



def hank_soc_crawling():
    
    hankyung_society_head=[]
    hankyung_society_url=[]
    hankyung_society_contents=[]
    kkk=[]

    for i in range(1,6):
        try :
            site = "https://www.hankyung.com/society?page={}".format(i)
            res = requests.get(site, headers={"User-Agent": "Mozilla/5.0"})
            bs =BeautifulSoup(res.text, 'lxml') #lxml
            society = bs.select('ul.list_basic > li > div.article > h3.tit > a')
        
            for k in society:
                hankyung_society_head.append(k.text)
                hankyung_society_url.append(k.attrs['href'])
            
                hankyung_s_url = k.attrs['href']
                res2 = requests.get(hankyung_s_url, headers={"User-Agent": "Mozilla/5.0"})
                bs2 =BeautifulSoup(res2.text, 'lxml') #lxml
                ttp = bs2.find('div',{'id':'articletxt'}).find_all(text=True)
                for j in ttp:
                    kkk.append(j.replace("\n","").replace("\t",""))
                hankyung_society_contents.append(' '.join(kkk))
                kkk=[]
                sleep(0.03)
        except:
            pass
    hankyung_s1= pd.DataFrame(hankyung_society_head, columns= ['headline'])
    hankyung_s3= pd.DataFrame(hankyung_society_url, columns= ['url'])
    hankyung_s2= pd.DataFrame(hankyung_society_contents, columns= ['contents'])
    hankyung_s=pd.concat([(pd.concat([hankyung_s1,hankyung_s2],axis=1)),hankyung_s3],axis=1)
    hankyung_s['category'] = '사회'
    hankyung_s['name'] = '한국경제'

    return hankyung_s



def hank_wor_crawling():

    hankyung_world_head=[]
    hankyung_world_url=[]
    hankyung_world_contents=[]
    kkk=[]

    for i in range(1,6):
        try :
            site = "https://www.hankyung.com/international?page={}".format(i)
            res = requests.get(site, headers={"User-Agent": "Mozilla/5.0"})
            bs =BeautifulSoup(res.text, 'lxml') #lxml
            world = bs.select('ul.list_basic > li > div.article > h3.tit > a')
        
            for k in world:
                hankyung_world_head.append(k.text)
                hankyung_world_url.append(k.attrs['href'])
            
                hankyung_w_url = k.attrs['href']
                res2 = requests.get(hankyung_w_url, headers={"User-Agent": "Mozilla/5.0"})
                bs2 =BeautifulSoup(res2.text, 'lxml') #lxml
                ttp = bs2.find('div',{'id':'articletxt'}).find_all(text=True)
                for j in ttp:
                    kkk.append(j.replace("\n","").replace("\t",""))
                hankyung_world_contents.append(' '.join(kkk))
                kkk=[]
                sleep(0.03)
        except:
            pass

    hankyung_w1= pd.DataFrame(hankyung_world_head, columns= ['headline'])
    hankyung_w3= pd.DataFrame(hankyung_world_url, columns= ['url'])
    hankyung_w2= pd.DataFrame(hankyung_world_contents, columns= ['contents'])
    hankyung_w=pd.concat([(pd.concat([hankyung_w1,hankyung_w2],axis=1)),hankyung_w3],axis=1)
    hankyung_w['category'] = '국제'
    hankyung_w['name'] = '한국경제'

    return hankyung_w



def hank_spo_crawling():

    hankyung_sports_head=[]
    hankyung_sports_url=[]
    hankyung_sports_contents=[]
    kkk=[]

    for i in range(1,6):
        try :
            site = "https://www.hankyung.com/sports?page={}".format(i)
            res = requests.get(site, headers={"User-Agent": "Mozilla/5.0"})
            bs =BeautifulSoup(res.text, 'lxml') #lxml
            sports = bs.select('ul.list_basic > li > div.article > h3.tit > a')
        
            for k in sports:
                hankyung_sports_head.append(k.text)
                hankyung_sports_url.append(k.attrs['href'])

                hankyung_sp_url = k.attrs['href']
                res2 = requests.get(hankyung_sp_url, headers={"User-Agent": "Mozilla/5.0"})
                bs2 =BeautifulSoup(res2.text, 'lxml') #lxml
                ttp = bs2.find('div',{'id':'articletxt'}).find_all(text=True)
                for j in ttp:
                    kkk.append(j.replace("\n","").replace("\t",""))
                hankyung_sports_contents.append(' '.join(kkk))
                kkk=[]
                sleep(0.03)
        except:
            pass

    hankyung_sp1= pd.DataFrame(hankyung_sports_head, columns= ['headline'])
    hankyung_sp3= pd.DataFrame(hankyung_sports_url, columns= ['url'])
    hankyung_sp2= pd.DataFrame(hankyung_sports_contents, columns= ['contents'])
    hankyung_sp=pd.concat([(pd.concat([hankyung_sp1,hankyung_sp2],axis=1)),hankyung_sp3],axis=1)
    hankyung_sp['category'] = '스포츠'
    hankyung_sp['name'] = '한국경제'

    return hankyung_sp


def hank_merge(hank_pol, hank_eco, hank_soc, hank_wor, hank_spo):
    hank = pd.concat([hank_pol, hank_eco, hank_soc, hank_wor, hank_spo]).reset_index().drop('index', axis = 1)
    hank.to_csv('hankyung.csv', index = False) #index=False
    return hank