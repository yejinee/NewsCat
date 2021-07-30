import numpy as np
import pandas as pd
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen



def dong_pol_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(5):
        if i == 0:
            link = 'https://www.donga.com/news/List/Politics?p=1&prod=news&ymd=&m='
        else :
            link = 'https://www.donga.com/news/List/Politics?p={}1&prod=news&ymd=&m='.format(i*2)
    
        for i in range(20):
            pol_dong = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = pol_dong.select('div.rightList > a')[i]['href']       # 기사 링크  
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')     # 기사 링크 html
        
            try :
                body = html.select('div.article_txt')[0]                 # 기사 본문 html
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # headline
            
                try :
                    while True :
                        body.div.decompose()
                except:
                    pass
                try :
                    while True :
                        body.script.decompose()
                except :
                    pass
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))
            except :
                pass
        
            count += 1
            print(count)
        time.sleep(0.5)

    dong_pol = pd.DataFrame()
    dong_pol['headline'] = headline
    dong_pol['contents'] = contents
    dong_pol['url'] = url
    dong_pol['category'] = '정치'
    dong_pol['name'] = '동아'

    return dong_pol



def dong_eco_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(5):
        if i == 0:
            link = 'https://www.donga.com/news/List/Economy?p=1&prod=news&ymd=&m='
        else :
            link = 'https://www.donga.com/news/List/Economy?p={}1&prod=news&ymd=&m='.format(i*2)
    
        for i in range(20):
            eco_dong = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = eco_dong.select('div.rightList > a')[i]['href']       # 기사 링크  
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')     # 기사 링크 html
        
            try :
                body = html.select('div.article_txt')[0]                 # 기사 본문 html
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # headline
            
                try :
                    while True :
                        body.div.decompose()
                except:
                    pass
                try :
                    while True :
                        body.script.decompose()
                except :
                    pass
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))
            except :
                pass
        
            count += 1
            print(count)
        time.sleep(0.5)

    dong_eco = pd.DataFrame()
    dong_eco['headline'] = headline
    dong_eco['contents'] = contents
    dong_eco['url'] = url
    dong_eco['category'] = '경제'
    dong_eco['name'] = '동아'

    return dong_eco



def dong_soc_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(5):
        if i == 0:
            link = 'https://www.donga.com/news/List/Society?p=1&prod=news&ymd=&m='
        else :
            link = 'https://www.donga.com/news/List/Society?p={}1&prod=news&ymd=&m='.format(i*2)
    
        for i in range(20):
            soc_dong = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = soc_dong.select('div.rightList > a')[i]['href']       # 기사 링크  
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')     # 기사 링크 html
        
            try :
                body = html.select('div.article_txt')[0]                 # 기사 본문 html
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # headline
            
                try :
                    while True :
                        body.div.decompose()
                except:
                    pass
                try :
                    while True :
                        body.script.decompose()
                except :
                    pass
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))
            except :
                pass
        
            count += 1
            print(count)
        time.sleep(0.5)

    dong_soc = pd.DataFrame()
    dong_soc['headline'] = headline
    dong_soc['contents'] = contents
    dong_soc['url'] = url
    dong_soc['category'] = '사회'
    dong_soc['name'] = '동아'

    return dong_soc


def dong_wor_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(5):
        if i == 0:
            link = 'https://www.donga.com/news/List/Inter?p=1&prod=news&ymd=&m='
        else :
            link = 'https://www.donga.com/news/List/Inter?p={}1&prod=news&ymd=&m='.format(i*2)
    
        for i in range(20):
            wor_dong = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = wor_dong.select('div.rightList > a')[i]['href']       # 기사 링크  
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')     # 기사 링크 html
        
            try :
                body = html.select('div.article_txt')[0]                 # 기사 본문 html
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # headline
            
                try :
                    while True :
                        body.div.decompose()
                except:
                    pass
                try :
                    while True :
                        body.script.decompose()
                except :
                    pass
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))
            except :
                pass
        
            count += 1
            print(count)
        time.sleep(0.5)

    dong_wor = pd.DataFrame()
    dong_wor['headline'] = headline
    dong_wor['contents'] = contents
    dong_wor['url'] = url
    dong_wor['category'] = '국제'
    dong_wor['name'] = '동아'

    return dong_wor



def dong_spo_crawling():
    url = []
    headline = []
    contents = []
    count = 0

    for i in range(5):
        if i == 0:
            link = 'https://www.donga.com/news/List/Sports?p=1&prod=news&ymd=&m='
        else :
            link = 'https://www.donga.com/news/List/Sports?p={}1&prod=news&ymd=&m='.format(i*2)
    
        for i in range(20):
            spo_dong = BeautifulSoup(urlopen(link), 'html.parser')
            link_1 = spo_dong.select('div.rightList > a')[i]['href']       # 기사 링크  
        
            time.sleep(0.2)
        
            html = BeautifulSoup(urlopen(link_1), 'html.parser')     # 기사 링크 html
        
            try :
                body = html.select('div.article_txt')[0]                 # 기사 본문 html
                url.append(link_1)                                      # 첫페이지 모든링크
                headline.append(html.select('h1')[0].text)              # headline
            
                try :
                    while True :
                        body.div.decompose()
                except:
                    pass
                try :
                    while True :
                        body.script.decompose()
                except :
                    pass
                contents.append(body.text.replace('\n', '').replace('\xa0','').replace('  ','').replace('\r','').replace('\'',''))
            except :
                pass
        
            count += 1
            print(count)
        time.sleep(0.5)

    dong_spo = pd.DataFrame()
    dong_spo['headline'] = headline
    dong_spo['contents'] = contents
    dong_spo['url'] = url
    dong_spo['category'] = '스포츠'
    dong_spo['name'] = '동아'

    return dong_spo


def dong_merge(dong_pol, dong_eco, dong_soc, dong_wor, dong_spo):
    dong = pd.concat([dong_pol, dong_eco, dong_soc, dong_wor, dong_spo]).reset_index().drop('index', axis = 1)
    dong.to_csv('dong.csv', index = False)
    return dong