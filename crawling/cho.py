import numpy as np
import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re



def cho_pol_crawling():
    chrome_loc = 'C:/chrome/chromedriver.exe'
    driver = webdriver.Chrome(chrome_loc)
    url = 'https://www.chosun.com/politics/'
    driver.get(url)

    fake_url = []
    real_url = []
    headline = []
    contents = []
    count = 0
    cho_site = 'https://www.chosun.com'

    for i in range(10):
        driver.find_element_by_xpath("//*[@id='load-more-stories']").click()                   # 기사 더보기
        time.sleep(1)
    pol_cho_html = driver.page_source
    pol_cho = BeautifulSoup(pol_cho_html, 'html.parser')                                       # 펼쳐진 페이지 크롤링

    for i in range(len(pol_cho.select('a.story-card__headline')[:-10])):
        link_fake = cho_site + pol_cho.select('a.story-card__headline')[:-10][i]['href']       # 기사 fake링크 0변경필요   -10인 이유 오른쪽 10순위 제거위함 
        html = BeautifulSoup(urlopen(link_fake), 'html.parser')                                # 기사 fake 링크 html
        fake_url.append(link_fake)
    
        link_real = html.select('head > link')[1]['href']                                      # 진짜 링크 뽑기
        real_url.append(link_real)
    
        html_real = BeautifulSoup(urlopen(link_real), 'html.parser')                           # 진짜 링크 html
    
        time.sleep(0.3)
    
        headline.append(html_real.select('h1.article-header__headline')[0].text)               # headline
    
        contents_real = html_real.select('p')                                                  # 기사 본문 크롤링
        contents_str = ''
        for i in range(len(contents_real)):
            contents_str += contents_real[i].text                                              # 크롤링한 본문 이어 붙이기
    
        contents.append(contents_str)
    
        count+=1
        print(count)

    cho_pol = pd.DataFrame()
    cho_pol['headline'] = headline
    cho_pol['contents'] = contents
    cho_pol['url'] = real_url
    cho_pol['category'] = '정치'
    cho_pol['name'] = '조선'

    return cho_pol



def cho_eco_crawling():
    chrome_loc = 'C:/chrome/chromedriver.exe'
    driver = webdriver.Chrome(chrome_loc)
    url = 'https://www.chosun.com/economy/'
    driver.get(url)

    fake_url = []
    real_url = []
    headline = []
    contents = []
    count = 0
    cho_site = 'https://www.chosun.com'

    for i in range(10):
        driver.find_element_by_xpath("//*[@id='load-more-stories']").click()                   # 기사 더보기
        time.sleep(1)
    eco_cho_html = driver.page_source
    eco_cho = BeautifulSoup(eco_cho_html, 'html.parser')                                       # 펼쳐진 페이지 크롤링

    for i in range(len(eco_cho.select('a.story-card__headline')[:-10])):
        link_fake = cho_site + eco_cho.select('a.story-card__headline')[:-10][i]['href']       # 기사 fake링크 0변경필요   -10인 이유 오른쪽 10순위 제거위함 
        html = BeautifulSoup(urlopen(link_fake), 'html.parser')                                # 기사 fake 링크 html
        fake_url.append(link_fake)
    
        link_real = html.select('head > link')[1]['href']                                      # 진짜 링크 뽑기
        real_url.append(link_real)
    
        html_real = BeautifulSoup(urlopen(link_real), 'html.parser')                           # 진짜 링크 html
    
        time.sleep(0.3)
    
        headline.append(html_real.select('h1.article-header__headline')[0].text)               # headline
    
        contents_real = html_real.select('p')                                                  # 기사 본문 크롤링
        contents_str = ''
        for i in range(len(contents_real)):
            contents_str += contents_real[i].text                                              # 크롤링한 본문 이어 붙이기
    
        contents.append(contents_str)
    
        count+=1
        print(count)

    cho_eco = pd.DataFrame()
    cho_eco['headline'] = headline
    cho_eco['contents'] = contents
    cho_eco['url'] = real_url
    cho_eco['category'] = '경제'
    cho_eco['name'] = '조선'

    return cho_eco



def cho_soc_crawling():
    chrome_loc = 'C:/chrome/chromedriver.exe'
    driver = webdriver.Chrome(chrome_loc)
    url = 'https://www.chosun.com/national/'
    driver.get(url)

    fake_url = []
    real_url = []
    headline = []
    contents = []
    count = 0
    cho_site = 'https://www.chosun.com'

    for i in range(10):
        driver.find_element_by_xpath("//*[@id='load-more-stories']").click()                   # 기사 더보기
        time.sleep(1)
    soc_cho_html = driver.page_source
    soc_cho = BeautifulSoup(soc_cho_html, 'html.parser')                                       # 펼쳐진 페이지 크롤링

    for i in range(len(soc_cho.select('a.story-card__headline')[:-10])):
        link_fake = cho_site + soc_cho.select('a.story-card__headline')[:-10][i]['href']       # 기사 fake링크 0변경필요   -10인 이유 오른쪽 10순위 제거위함 
        html = BeautifulSoup(urlopen(link_fake), 'html.parser')                                # 기사 fake 링크 html
        fake_url.append(link_fake)
    
        link_real = html.select('head > link')[1]['href']                                      # 진짜 링크 뽑기
        real_url.append(link_real)
    
        html_real = BeautifulSoup(urlopen(link_real), 'html.parser')                           # 진짜 링크 html
    
        time.sleep(0.3)
    
        headline.append(html_real.select('h1.article-header__headline')[0].text)               # headline
    
        contents_real = html_real.select('p')                                                  # 기사 본문 크롤링
        contents_str = ''
        for i in range(len(contents_real)):
            contents_str += contents_real[i].text                                              # 크롤링한 본문 이어 붙이기
    
        contents.append(contents_str)
    
        count+=1
        print(count)

    cho_soc = pd.DataFrame()
    cho_soc['headline'] = headline
    cho_soc['contents'] = contents
    cho_soc['url'] = real_url
    cho_soc['category'] = '사회'
    cho_soc['name'] = '조선'

    return cho_soc



def cho_wor_crawling():
    chrome_loc = 'C:/chrome/chromedriver.exe'
    driver = webdriver.Chrome(chrome_loc)
    url = 'https://www.chosun.com/international/'
    driver.get(url)

    fake_url = []
    real_url = []
    headline = []
    contents = []
    count = 0
    cho_site = 'https://www.chosun.com'

    for i in range(10):
        driver.find_element_by_xpath("//*[@id='load-more-stories']").click()                   # 기사 더보기
        time.sleep(1)
    wor_cho_html = driver.page_source
    wor_cho = BeautifulSoup(wor_cho_html, 'html.parser')                                       # 펼쳐진 페이지 크롤링

    for i in range(len(wor_cho.select('a.story-card__headline')[:-10])):
        link_fake = cho_site + wor_cho.select('a.story-card__headline')[:-10][i]['href']       # 기사 fake링크 0변경필요   -10인 이유 오른쪽 10순위 제거위함 
        html = BeautifulSoup(urlopen(link_fake), 'html.parser')                                # 기사 fake 링크 html
        fake_url.append(link_fake)
    
        link_real = html.select('head > link')[1]['href']                                      # 진짜 링크 뽑기
        real_url.append(link_real)
    
        html_real = BeautifulSoup(urlopen(link_real), 'html.parser')                           # 진짜 링크 html
    
        time.sleep(0.3)
    
        headline.append(html_real.select('h1.article-header__headline')[0].text)               # headline
    
        contents_real = html_real.select('p')                                                  # 기사 본문 크롤링
        contents_str = ''
        for i in range(len(contents_real)):
            contents_str += contents_real[i].text                                              # 크롤링한 본문 이어 붙이기
    
        contents.append(contents_str)
    
        count+=1
        print(count)

    cho_wor = pd.DataFrame()
    cho_wor['headline'] = headline
    cho_wor['contents'] = contents
    cho_wor['url'] = real_url
    cho_wor['category'] = '국제'
    cho_wor['name'] = '조선'

    return cho_wor



def cho_spo_crawling():
    chrome_loc = 'C:/chrome/chromedriver.exe'
    driver = webdriver.Chrome(chrome_loc)
    url = 'https://www.chosun.com/sports/'
    driver.get(url)

    fake_url = []
    real_url = []
    headline = []
    contents = []
    count = 0
    cho_site = 'https://www.chosun.com'

    for i in range(10):
        driver.find_element_by_xpath("//*[@id='load-more-stories']").click()                   # 기사 더보기
        time.sleep(1)
    spo_cho_html = driver.page_source
    spo_cho = BeautifulSoup(spo_cho_html, 'html.parser')                                       # 펼쳐진 페이지 크롤링

    for i in range(len(spo_cho.select('a.story-card__headline')[:-10])):
        link_fake = cho_site + spo_cho.select('a.story-card__headline')[:-10][i]['href']       # 기사 fake링크 0변경필요   -10인 이유 오른쪽 10순위 제거위함 
        html = BeautifulSoup(urlopen(link_fake), 'html.parser')                                # 기사 fake 링크 html
        fake_url.append(link_fake)
    
        link_real = html.select('head > link')[1]['href']                                      # 진짜 링크 뽑기
        real_url.append(link_real)
    
        html_real = BeautifulSoup(urlopen(link_real), 'html.parser')                           # 진짜 링크 html
    
        time.sleep(0.3)
    
        headline.append(html_real.select('h1.article-header__headline')[0].text)               # headline
    
        contents_real = html_real.select('p')                                                  # 기사 본문 크롤링
        contents_str = ''
        for i in range(len(contents_real)):
            contents_str += contents_real[i].text                                              # 크롤링한 본문 이어 붙이기
    
        contents.append(contents_str)
    
        count+=1
        print(count)

    cho_spo = pd.DataFrame()
    cho_spo['headline'] = headline
    cho_spo['contents'] = contents
    cho_spo['url'] = real_url
    cho_spo['category'] = '스포츠'
    cho_spo['name'] = '조선'

    return cho_spo


def cho_merge(cho_pol, cho_eco, cho_soc, cho_wor, cho_spo):
    cho = pd.concat([cho_pol, cho_eco, cho_soc, cho_wor, cho_spo]).reset_index().drop('index', axis = 1)
    cho.to_csv('cho.csv', index = False)
    return cho
