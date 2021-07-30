import numpy as np
import pandas as pd
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen



def hani_pol_crawling():

    hani_site = 'https://www.hani.co.kr'
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(6):
        link = 'https://www.hani.co.kr/arti/politics/list{}.html'.format(i+1)
    
        for j in range(15):
            pol_hani = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = hani_site + pol_hani.select('h4.article-title > a')[j]['href']    # 기사 링크 
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')      # 기사 링크 html
        
            try :
                body = html.select('div.text')[0]                # 기사 본문 html
                url.append(link_1)                              # 페이지 모든 링크
                headline.append(html.select('span.title')[0].text)      # headline
            
                try:
                    while True :
                        body.div.decompose()
                except :
                    pass
            
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))   #  본문
            except :
                pass
            count += 1
            print(count)
        time.sleep(0.5)             

    hani_pol = pd.DataFrame()
    hani_pol['headline'] = headline
    hani_pol['contents'] = contents
    hani_pol['url'] = url
    hani_pol['category'] = '정치'
    hani_pol['name'] = '한겨레'

    return hani_pol




def hani_eco_crawling():
    
    hani_site = 'https://www.hani.co.kr'
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(6):
        link = 'https://www.hani.co.kr/arti/economy/list{}.html'.format(i+1)
    
        for j in range(15):
            eco_hani = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = hani_site + eco_hani.select('h4.article-title > a')[j]['href']    # 기사 링크 
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')      # 기사 링크 html
        
            try :
                body = html.select('div.text')[0]                # 기사 본문 html
                url.append(link_1)                              # 페이지 모든 링크
                headline.append(html.select('span.title')[0].text)      # headline
            
                try:
                    while True :
                        body.div.decompose()
                except :
                    pass
            
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))   #  본문
            except :
                pass
            count += 1
            print(count)
        time.sleep(0.5)             

    hani_eco = pd.DataFrame()
    hani_eco['headline'] = headline
    hani_eco['contents'] = contents
    hani_eco['url'] = url
    hani_eco['category'] = '경제'
    hani_eco['name'] = '한겨레'

    return hani_eco




def hani_soc_crawling():
    
    hani_site = 'https://www.hani.co.kr'
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(6):
        link = 'https://www.hani.co.kr/arti/society/list{}.html'.format(i+1)
    
        for j in range(15):
            soc_hani = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = hani_site + soc_hani.select('h4.article-title > a')[j]['href']    # 기사 링크 
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')      # 기사 링크 html
        
            try :
                body = html.select('div.text')[0]                # 기사 본문 html
                url.append(link_1)                              # 페이지 모든 링크
                headline.append(html.select('span.title')[0].text)      # headline
            
                try:
                    while True :
                        body.div.decompose()
                except :
                    pass
            
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))   #  본문
            except :
                pass
            count += 1
            print(count)
        time.sleep(0.5)             

    hani_soc = pd.DataFrame()
    hani_soc['headline'] = headline
    hani_soc['contents'] = contents
    hani_soc['url'] = url
    hani_soc['category'] = '사회'
    hani_soc['name'] = '한겨레'

    return hani_soc




def hani_wor_crawling():
    
    hani_site = 'https://www.hani.co.kr'
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(6):
        link = 'https://www.hani.co.kr/arti/international/list{}.html'.format(i+1)
    
        for j in range(15):
            wor_hani = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = hani_site + wor_hani.select('h4.article-title > a')[j]['href']    # 기사 링크 
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')      # 기사 링크 html
        
            try :
                body = html.select('div.text')[0]                # 기사 본문 html
                url.append(link_1)                              # 페이지 모든 링크
                headline.append(html.select('span.title')[0].text)      # headline
            
                try:
                    while True :
                        body.div.decompose()
                except :
                    pass
            
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))   #  본문
            except :
                pass
            count += 1
            print(count)
        time.sleep(0.5)             

    hani_wor = pd.DataFrame()
    hani_wor['headline'] = headline
    hani_wor['contents'] = contents
    hani_wor['url'] = url
    hani_wor['category'] = '국제'
    hani_wor['name'] = '한겨레'

    return hani_wor




def hani_spo_crawling():
    
    hani_site = 'https://www.hani.co.kr'
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(6):
        link = 'https://www.hani.co.kr/arti/sports/list{}.html'.format(i+1)
    
        for j in range(15):
            spo_hani = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = hani_site + spo_hani.select('h4.article-title > a')[j]['href']    # 기사 링크 
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')      # 기사 링크 html
        
            try :
                body = html.select('div.text')[0]                # 기사 본문 html
                url.append(link_1)                              # 페이지 모든 링크
                headline.append(html.select('span.title')[0].text)      # headline
            
                try:
                    while True :
                        body.div.decompose()
                except :
                    pass
            
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))   #  본문
            except :
                pass
            count += 1
            print(count)
        time.sleep(0.5)             

    hani_spo = pd.DataFrame()
    hani_spo['headline'] = headline
    hani_spo['contents'] = contents
    hani_spo['url'] = url
    hani_spo['category'] = '스포츠'
    hani_spo['name'] = '한겨레'

    return hani_spo


def hani_merge(hani_pol, hani_eco, hani_soc, hani_wor, hani_spo):
    hani = pd.concat([hani_pol, hani_eco, hani_soc, hani_wor, hani_spo]).reset_index().drop('index', axis = 1)
    hani.to_csv('hani.csv', index = False)
    return hani