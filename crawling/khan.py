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


def khan_pol_crawling(): 
    chrome_loc = 'C:/chrome/chromedriver.exe'
    driver = webdriver.Chrome(chrome_loc)
    url = 'https://www.khan.co.kr/politics'
    driver.get(url)

    khan_politics_head=[]
    khan_politics_url=[]
    khan_politics_contents=[]
    kkk=[]

    for i in range(1,11):
        try :
            html = driver.page_source
            bs =BeautifulSoup(html, 'lxml') #lxml
            politics = bs.select('ul.df-list > li > div.txt > h2.tit > a')
            for k in politics:
                khan_politics_head.append(k.attrs['title'])
                khan_politics_url.append(k.attrs['href'])

                khan_p_url = k.attrs['href']
                res = requests.get(khan_p_url, headers={"User-Agent": "Mozilla/5.0"})
                bs =BeautifulSoup(res.text, 'lxml') #lxml
                ttp = bs.select('div.art_body > p') #('div#articleBody')도 같은결과?
                for j in ttp:
                    kkk.append(j.text)
                khan_politics_contents.append(' '.join(kkk))
                kkk=[]
                sleep(0.03)
            if i%5==0:
                next_5_btn = driver.find_element_by_css_selector('#paging > a.btn-paging.next > span').click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
            elif i<=4:
                next_page = driver.find_element_by_css_selector('#paging > a:nth-child({})'.format((i%5)+1)).click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
            else:
                next_page = driver.find_element_by_css_selector('#paging > a:nth-child({})'.format((i%5)+2)).click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
        except:
            pass

    khan_p1= pd.DataFrame(khan_politics_head, columns= ['headline'])
    khan_p3= pd.DataFrame(khan_politics_url, columns= ['url'])
    khan_p2= pd.DataFrame(khan_politics_contents, columns= ['contents'])
    khan_p=pd.concat([(pd.concat([khan_p1,khan_p2],axis=1)),khan_p3],axis=1)
    khan_p['category'] = '정치'
    khan_p['name'] = '경향'

    return khan_p



def khan_eco_crawling():

    khan_economy_head=[]
    khan_economy_url=[]
    khan_economy_contents=[]
    kkk=[]

    for i in range(1,8):
        try :
            site= 'http://biz.khan.co.kr/khan_art_list.html?page={}'.format(i)
            res = requests.get(site, headers={"User-Agent": "Mozilla/5.0"})
            bs =BeautifulSoup(res.text, 'lxml') #lxml
            economy = bs.select('li > div.text_area > strong.hd_title > a')
            for k in economy:
                khan_economy_head.append(k.text)
                khan_economy_url.append('http:'+k.attrs['href'])
            
                khan_e_url = 'http:'+k.attrs['href']
                res2 = requests.get(khan_e_url, headers={"User-Agent": "Mozilla/5.0"})
                bs2 =BeautifulSoup(res2.text, 'lxml') #lxml
                ttp = bs2.select('div.art_body > p') #('div#articleBody')도 같은결과?
                for j in ttp:
                    kkk.append(j.text)
                khan_economy_contents.append(' '.join(kkk))
                kkk=[]
                sleep(0.03)
        except:
            pass

    khan_e1= pd.DataFrame(khan_economy_head, columns= ['headline'])
    khan_e3= pd.DataFrame(khan_economy_url, columns= ['url'])
    khan_e2= pd.DataFrame(khan_economy_contents, columns= ['contents'])
    khan_e=pd.concat([(pd.concat([khan_e1,khan_e2],axis=1)),khan_e3],axis=1)
    khan_e['category'] = '경제'
    khan_e['name'] = '경향'

    return khan_e



def khan_soc_crawling():

    chrome_loc = 'C:/chrome/chromedriver.exe'
    driver = webdriver.Chrome(chrome_loc)
    url = 'https://www.khan.co.kr/national'
    driver.get(url)

    khan_society_head=[]
    khan_society_url=[]
    khan_society_contents=[]
    kkk=[]

    for i in range(1,11):
        try :
            html = driver.page_source
            bs =BeautifulSoup(html, 'lxml') #lxml
            society = bs.select('ul.df-list > li > div.txt > h2.tit > a')
            for k in society:
                khan_society_head.append(k.attrs['title'])
                khan_society_url.append(k.attrs['href'])

                khan_s_url = k.attrs['href']
                res = requests.get(khan_s_url, headers={"User-Agent": "Mozilla/5.0"})
                bs =BeautifulSoup(res.text, 'lxml') #lxml
                ttp = bs.select('div.art_body > p') #('div#articleBody')도 같은결과?
                for j in ttp:
                    kkk.append(j.text)
                khan_society_contents.append(' '.join(kkk))
                kkk=[]
                sleep(0.03)
            if i%5==0:
                next_5_btn = driver.find_element_by_css_selector('#paging > a.btn-paging.next > span').click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
            elif i<=4:
                next_page = driver.find_element_by_css_selector('#paging > a:nth-child({})'.format((i%5)+1)).click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
            else:
                next_page = driver.find_element_by_css_selector('#paging > a:nth-child({})'.format((i%5)+2)).click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
        except:
            pass

    khan_s1= pd.DataFrame(khan_society_head, columns= ['headline'])
    khan_s3= pd.DataFrame(khan_society_url, columns= ['url'])
    khan_s2= pd.DataFrame(khan_society_contents, columns= ['contents'])
    khan_s=pd.concat([(pd.concat([khan_s1,khan_s2],axis=1)),khan_s3],axis=1)
    khan_s['category'] = '사회'
    khan_s['name'] = '경향'

    return khan_s



def khan_wor_crawling():

    chrome_loc = 'C:/chrome/chromedriver.exe'
    driver = webdriver.Chrome(chrome_loc)
    url = 'https://www.khan.co.kr/world'
    driver.get(url)

    khan_world_head=[]
    khan_world_url=[]
    khan_world_contents=[]
    kkk=[]

    for i in range(1,11):
        try :
            html = driver.page_source
            bs =BeautifulSoup(html, 'lxml') #lxml
            world = bs.select('ul.df-list > li > div.txt > h2.tit > a')
            for k in world:
                khan_world_head.append(k.attrs['title'])
                khan_world_url.append(k.attrs['href'])

                khan_w_url = k.attrs['href']
                res = requests.get(khan_w_url, headers={"User-Agent": "Mozilla/5.0"})
                bs =BeautifulSoup(res.text, 'lxml') #lxml
                ttp = bs.select('div.art_body > p') #('div#articleBody')도 같은결과?
                for j in ttp:
                    kkk.append(j.text)
                khan_world_contents.append(' '.join(kkk))
                kkk=[]
                sleep(0.03)
            if i%5==0:
                next_5_btn = driver.find_element_by_css_selector('#paging > a.btn-paging.next > span').click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
            elif i<=4:
                next_page = driver.find_element_by_css_selector('#paging > a:nth-child({})'.format((i%5)+1)).click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
            else:
                next_page = driver.find_element_by_css_selector('#paging > a:nth-child({})'.format((i%5)+2)).click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
        except:
            pass

    khan_w1= pd.DataFrame(khan_world_head, columns= ['headline'])
    khan_w3= pd.DataFrame(khan_world_url, columns= ['url'])
    khan_w2= pd.DataFrame(khan_world_contents, columns= ['contents'])
    khan_w=pd.concat([(pd.concat([khan_w1,khan_w2],axis=1)),khan_w3],axis=1)
    khan_w['category'] = '국제'
    khan_w['name'] = '경향'

    return khan_w



def khan_spo_crawling():

    chrome_loc = 'C:/chrome/chromedriver.exe'
    driver = webdriver.Chrome(chrome_loc)
    url = 'https://www.khan.co.kr/sports'
    driver.get(url)

    khan_sports_head=[]
    khan_sports_url=[]
    khan_sports_contents=[]
    kkk=[]

    for i in range(1,11):
        try :
            html = driver.page_source
            bs =BeautifulSoup(html, 'lxml') #lxml
            sports = bs.select('ul.df-list > li > div.txt > h2.tit > a')
            for k in sports:
                khan_sports_head.append(k.attrs['title'])
                khan_sports_url.append(k.attrs['href'])

                khan_sp_url = k.attrs['href']
                res = requests.get(khan_sp_url, headers={"User-Agent": "Mozilla/5.0"})
                bs =BeautifulSoup(res.text, 'lxml') #lxml
                ttp = bs.select('div.art_body > p') #('div#articleBody')도 같은결과?
                for j in ttp:
                    kkk.append(j.text)
                khan_sports_contents.append(' '.join(kkk))
                kkk=[]
                sleep(0.03)
            if i%5==0:
                next_5_btn = driver.find_element_by_css_selector('#paging > a.btn-paging.next > span').click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
            elif i<=4:
                next_page = driver.find_element_by_css_selector('#paging > a:nth-child({})'.format((i%5)+1)).click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
            else:
                next_page = driver.find_element_by_css_selector('#paging > a:nth-child({})'.format((i%5)+2)).click()
                print('{}페이지 작업 끝'.format(i))
                sleep(0.01)
        except:
            pass

    khan_sp1= pd.DataFrame(khan_sports_head, columns= ['headline'])
    khan_sp3= pd.DataFrame(khan_sports_url, columns= ['url'])
    khan_sp2= pd.DataFrame(khan_sports_contents, columns= ['contents'])
    khan_sp=pd.concat([(pd.concat([khan_sp1,khan_sp2],axis=1)),khan_sp3],axis=1)
    khan_sp['category'] = '스포츠'
    khan_sp['name'] = '경향'

    return khan_sp

def khan_merge(khan_pol, khan_eco, khan_soc, khan_wor, khan_spo):
    khan = pd.concat([khan_pol, khan_eco, khan_soc, khan_wor, khan_spo], axis = 0)
    khan = khan.reset_index().drop(columns = 'index')
    khan.to_csv('khan.csv', index = False)
    return khan
