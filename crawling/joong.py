import numpy as np
import pandas as pd
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

def joong_pol_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for page in range(1, 6):
        link = 'https://news.joins.com/politics?page={}'.format(page)
        for i in range(15):
            pol_joong = BeautifulSoup(urlopen(link), 'html.parser') # html
    
            link_1 = pol_joong.select('h2 > a')[i]['href']
        
            time.sleep(0.2)
    
            html = BeautifulSoup(urlopen(link_1), 'html.parser')    # 기사 링크 html
    
            try :
                body = html.select('div.article_body')[0]              # 기사 본문
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # 헤드라인
                try :
                    while True:
                        body.div.decompose()                            # 주석, 기자이름 제거
                except :
                    pass                                  
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))      
            except :
                pass  
            count += 1
            print(count / 75 * 100)
        time.sleep(0.5) 

    joong_pol = pd.DataFrame()
    joong_pol['headline'] = headline
    joong_pol['contents'] = contents
    joong_pol['url'] = url
    joong_pol['category'] = '정치'
    joong_pol['name'] = '중앙'
    return joong_pol


def joong_eco_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for page in range(1, 6):
        link = 'https://news.joins.com/money?page={}'.format(page)
        for i in range(15):
            eco_joong = BeautifulSoup(urlopen(link), 'html.parser') # html
    
            link_1 = eco_joong.select('h2 > a')[i]['href']
        
            time.sleep(0.2)
    
            html = BeautifulSoup(urlopen(link_1), 'html.parser')    # 기사 링크 html
    
            try :
                body = html.select('div.article_body')[0]              # 기사 본문
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # 헤드라인
                try :
                    while True:
                        body.div.decompose()                            # 주석, 기자이름 제거
                except :
                    pass                                  
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))      
            except :
                pass  
            count += 1
            print(count / 75 * 100)
        time.sleep(0.5) 

    joong_eco = pd.DataFrame()
    joong_eco['headline'] = headline
    joong_eco['contents'] = contents
    joong_eco['url'] = url
    joong_eco['category'] = '경제'
    joong_eco['name'] = '중앙'
    return joong_eco


def joong_soc_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for page in range(1, 6):
        link = 'https://news.joins.com/society?page={}'.format(page)
        for i in range(15):
            soc_joong = BeautifulSoup(urlopen(link), 'html.parser') # html
    
            link_1 = soc_joong.select('h2 > a')[i]['href']
        
            time.sleep(0.2)
    
            html = BeautifulSoup(urlopen(link_1), 'html.parser')    # 기사 링크 html
    
            try :
                body = html.select('div.article_body')[0]              # 기사 본문
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # 헤드라인
                try :
                    while True:
                        body.div.decompose()                            # 주석, 기자이름 제거
                except :
                    pass                                  
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))      
            except :
                pass  
            count += 1
            print(count / 75 * 100)
        time.sleep(0.5) 

    joong_soc = pd.DataFrame()
    joong_soc['headline'] = headline
    joong_soc['contents'] = contents
    joong_soc['url'] = url
    joong_soc['category'] = '사회'
    joong_soc['name'] = '중앙'
    return joong_soc


def joong_wor_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for page in range(1, 6):
        link = 'https://news.joins.com/world?page={}'.format(page)
        for i in range(15):
            wor_joong = BeautifulSoup(urlopen(link), 'html.parser') # html
    
            link_1 = wor_joong.select('h2 > a')[i]['href']
        
            time.sleep(0.2)
    
            html = BeautifulSoup(urlopen(link_1), 'html.parser')    # 기사 링크 html
    
            try :
                body = html.select('div.article_body')[0]              # 기사 본문
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # 헤드라인
                try :
                    while True:
                        body.div.decompose()                            # 주석, 기자이름 제거
                except :
                    pass                                  
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))      
            except :
                pass  
            count += 1
            print(count / 75 * 100)
        time.sleep(0.5) 

    joong_wor = pd.DataFrame()
    joong_wor['headline'] = headline
    joong_wor['contents'] = contents
    joong_wor['url'] = url
    joong_wor['category'] = '국제'
    joong_wor['name'] = '중앙'
    return joong_wor


def joong_spo_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for page in range(1, 6):
        link = 'https://news.joins.com/sports?page={}'.format(page)
        for i in range(15):
            spo_joong = BeautifulSoup(urlopen(link), 'html.parser') # html
    
            link_1 = spo_joong.select('h2 > a')[i]['href']
        
            time.sleep(0.2)
    
            html = BeautifulSoup(urlopen(link_1), 'html.parser')    # 기사 링크 html
    
            try :
                body = html.select('div.article_body')[0]              # 기사 본문
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # 헤드라인
                try :
                    while True:
                        body.div.decompose()                            # 주석, 기자이름 제거
                except :
                    pass                                  
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))      
            except :
                pass  
            count += 1
            print(count / 75 * 100)
        time.sleep(0.5) 

    joong_spo = pd.DataFrame()
    joong_spo['headline'] = headline
    joong_spo['contents'] = contents
    joong_spo['url'] = url
    joong_spo['category'] = '스포츠'
    joong_spo['name'] = '중앙'
    return joong_spo

def joong_merge(joong_pol, joong_eco, joong_soc, joong_wor, joong_spo):
    joong = pd.concat([joong_pol, joong_eco, joong_soc, joong_wor, joong_spo]).reset_index().drop('index', axis = 1)
    joong.to_csv('joong.csv', index = False)
    return joong

