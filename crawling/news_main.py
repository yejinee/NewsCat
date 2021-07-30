from joong import joong_pol_crawling
from joong import joong_eco_crawling
from joong import joong_soc_crawling
from joong import joong_wor_crawling
from joong import joong_spo_crawling
from joong import joong_merge

from dong import dong_pol_crawling
from dong import dong_eco_crawling
from dong import dong_soc_crawling
from dong import dong_wor_crawling
from dong import dong_spo_crawling
from dong import dong_merge

from hani import hani_pol_crawling
from hani import hani_eco_crawling
from hani import hani_soc_crawling
from hani import hani_wor_crawling
from hani import hani_spo_crawling
from hani import hani_merge

from cho import cho_pol_crawling
from cho import cho_eco_crawling
from cho import cho_soc_crawling
from cho import cho_wor_crawling
from cho import cho_spo_crawling
from cho import cho_merge

from hankyung import hank_pol_crawling
from hankyung import hank_eco_crawling
from hankyung import hank_soc_crawling
from hankyung import hank_wor_crawling
from hankyung import hank_spo_crawling
from hankyung import hank_merge

from khan import khan_pol_crawling
from khan import khan_eco_crawling
from khan import khan_soc_crawling
from khan import khan_wor_crawling
from khan import khan_spo_crawling
from khan import khan_merge

import pandas as pd

#j_pol = joong_pol_crawling()
print('joong_pol 생성 완료')
#j_eco = joong_eco_crawling()
print('joong_eco 생성 완료')
#j_soc = joong_soc_crawling()
print('joong_soc 생성 완료')
#j_wor = joong_wor_crawling()
print('joong_wor 생성 완료')
#j_spo = joong_spo_crawling()
print('joong_spo 생성 완료')
#joong_news = joong_merge(j_pol, j_eco, j_soc, j_wor, j_spo)

#d_pol = dong_pol_crawling()
print('dong_pol 생성 완료')
#d_eco = dong_eco_crawling()
print('dong_eco 생성 완료')
#d_soc = dong_soc_crawling()
print('dong_soc 생성 완료')
#d_wor = dong_wor_crawling()
print('dong_wor 생성 완료')
#d_spo = dong_spo_crawling()
print('dong_spo 생성 완료')
#dong_news = dong_merge(d_pol, d_eco, d_soc, d_wor, d_spo)

#hani_pol = hani_pol_crawling()
print('hani_pol 생성 완료')
#hani_eco = hani_eco_crawling()
print('hani_eco 생성 완료')
#hani_soc = hani_soc_crawling()
print('hani_soc 생성 완료')
#hani_wor = hani_wor_crawling()
print('hani_wor 생성 완료')
#hani_spo = hani_spo_crawling()
print('hani_spo 생성 완료')
#hani_news = hani_merge(hani_pol, hani_eco, hani_soc, hani_wor, hani_spo)

#cho_pol = cho_pol_crawling()
print('cho_pol 생성 완료')
#cho_eco = cho_eco_crawling()
print('cho_eco 생성 완료')
#cho_soc = cho_soc_crawling()
print('cho_soc 생성 완료')
#cho_wor = cho_wor_crawling()
print('cho_wor 생성 완료')
#cho_spo = cho_spo_crawling()
print('cho_spo 생성 완료')
#cho_news = cho_merge(cho_pol, cho_eco, cho_soc, cho_wor, cho_spo)

#hank_pol = hank_pol_crawling()
print('hank_pol 생성 완료')
#hank_eco = hank_eco_crawling()
print('hank_eco 생성 완료')
#hank_soc = hank_soc_crawling()
print('hank_soc 생성 완료')
#hank_wor = hank_wor_crawling()
print('hank_wor 생성 완료')
#hank_spo = hank_spo_crawling()
print('hank_spo 생성 완료')
#hank_news = hank_merge(hank_pol, hank_eco, hank_soc, hank_wor, hank_spo)

#khan_pol = khan_pol_crawling()
print('khan_pol 생성 완료')
#khan_eco = khan_eco_crawling()
print('khan_eco 생성 완료')
#khan_soc = khan_soc_crawling()
print('khan_soc 생성 완료')
#khan_wor = khan_wor_crawling()
print('khan_wor 생성 완료')
#khan_spo = khan_spo_crawling()
print('khan_spo 생성 완료')
#khan_news = khan_merge(khan_pol, khan_eco, khan_soc, khan_wor, khan_spo)

import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns


dong = pd.read_csv('dong.csv')
hani = pd.read_csv('hani.csv')
joong = pd.read_csv('joong.csv')
khan = pd.read_csv('khan.csv')
hankyung = pd.read_csv('hankyung.csv')
cho = pd.read_csv('cho.csv')

data = pd.concat([dong, hani, joong, khan, hankyung, cho])   # 병합
data = data.drop_duplicates(['headline'])               # 기사 제목 중복 제거
data = data.reset_index().drop(['index'], axis = 1)     # index reset
data = data.dropna(axis = 0)                            # NA 제거
data = data.reset_index().drop('index', axis = 1) 

print('data 로딩 완료')
##############################  contents 전처리 특수문자 제거
import re 
import string
to_replace_by_space = re.compile('[/(){}\[|]|@,;')
punctuation = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')

def text_prepare(text):
    text = re.sub(punctuation, '', text)
    text = re.sub(to_replace_by_space, " ", text)
    return text

data['contents'] = data['contents'].apply(text_prepare) 

print('contents 특수문자 제거 완료')
############################  형태소분석

from konlpy.tag import Okt
import re
okt = Okt()
sep = []

for word in data['contents'] : 
    sep.append(okt.pos(word))

print('형태소 분석 완료')
############################# keyword 

keyword = []
blank = []
for word in sep:
    for each in word:
        if each[1] == 'Noun':
            blank.append(each[0])
        else:
            pass
    keyword.append(blank)
    blank = []
    
keyword2 = []                      ### 두글자 이상만 뽑기
balck = []
for word in keyword:
    for each in word:
        if len(each) >= 2 :
            blank.append(each)
    keyword2.append(blank)
    blank = []

data['keyword2'] = keyword2

print('keyword2 생성 완료')
####################################### TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from operator import itemgetter

tf_word = []                                                    ## 모든 keyword2 이어 붙이기
for i in range(len(data['keyword2'])):
    tf_word.append(' '.join(t for t in data['keyword2'][i]))


tfidf = TfidfVectorizer()
sp_matrix = tfidf.fit_transform(tf_word)

word2id = defaultdict(lambda : 0)
for idx, feature in enumerate(tfidf.get_feature_names()):
    word2id[feature] = idx

word = []
for i, sent in enumerate(tf_word):
    word.append([ [token, sp_matrix[i, word2id[token]]] for token in sent.split()])

for i in range(len(word)):
    word[i].sort(key = itemgetter(1), reverse = True)      # 중요도 순으로 정렬

print('tf-idf 계산 완료')
##########################               한 기사에 여러 단어가 들어가 있으므로 중복 제거
new_word = []
blank = []

for i in range(len(word)):
    
    for j in range(len(word[i])):
        if word[i][j] not in blank :
            blank.append(word[i][j])
        else :
            pass
    new_word.append(blank)  
    blank = []


################################              상위 5개 뽑기
hot_word = []
blank = []
for i in range(len(new_word)):
    for j in range(len(new_word[i])):
        blank.append(new_word[i][j][0])
    hot_word.append(blank[:5])
    blank = []


print('hot_word 생성 완료')
data['hot_word'] = hot_word
data = data.drop('keyword2', axis = 1)
data.to_csv('final.csv')
print('크롤링 데이터 저장 완료')