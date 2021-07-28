import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pymysql
import random

def Tostr(name, category, s):
    value=ast.literal_eval(s)
    a=" ".join(value)
    a+=" "+name
    a+=" "+category
    return a

# 뉴스추천 (5개의 뉴스 추천내역 가져와서 총 5개 추출)
def find_sim_news(df,sorted_ind, news_id, top_n=5):
    ans=[]
    for i in news_id:
    #  해당 영화 cosine 유사도가 높은 순로 top_n개 반환
        similar_indexes= sorted_ind[i, :(top_n)]

    # 추출된 top_n개의 index 출력 (2차원 data)
    # DF에서 index로 사용하기 위해 1차원 arr로 변경
        similar_indexes= similar_indexes.reshape(-1)
        ans.append(similar_indexes[1])
    return ans


data=pd.read_csv('C:/Users/kimjh/d/final.csv')
news=data[['headline', 'url', 'category', 'name', 'hot_word']]


###### 추천 알고리즘 적용하기 위해 만든 소스 ###################################
# CountVectorizer 를 적용하기 위해 공백문자로 word 단위가 구분되는 문자열로 변환
news['hot_news']=news.apply(lambda x:Tostr(x['name'], x['category'], x['hot_word']), axis=1)

count_vect=CountVectorizer(min_df=0, ngram_range=(1,2))
genre_mat= count_vect.fit_transform(news['hot_news'])

genre_sim=cosine_similarity(genre_mat, genre_mat)
genre_sim_sorted_ind=genre_sim.argsort()[:,::-1]


######  DB 접속 #############################################
con=pymysql.connect(host='final-chatbot.c7dwoilcj9uq.ap-northeast-2.rds.amazonaws.com',user='yejin',password='1313', db='CHAT_BOT_DB', charset='utf8')
cur=con.cursor()

# User Table에서 User정보 싹다 뽑아오기 
extract_ID="SELECT * FROM Users"
cur.execute(extract_ID)
user=cur.fetchall()
userinfo=pd.DataFrame(user,columns=['user_id','preference1','preference2'])

# Userlog에서 로그들 다 추출하기
extract_log="SELECT * FROM User_log WHERE News_like=1"
cur.execute(extract_log)
log=cur.fetchall()
loginfo=pd.DataFrame(log,columns=['user_id','news_id','news_like'])


category=['정치', '경제','사회','국제','스포츠']
# 한번에 업데이트 할 것 
# 모든 유저에 대해 접근
for i in range(len(userinfo)):
    # user별 추천 idx
    reco_idx=[]
    # 각 user의 정보 추출
    # user 1명에 대한 id, 카테고리 2개, 좋아요 한 log 빼오기
    userid, cate1, cate2=userinfo['user_id'][i], userinfo['preference1'][i], userinfo['preference2'][i]
    user_log= loginfo[loginfo['user_id']==userid]
    # userlog에 대해 해당하는 애가 없는 경우 
    if len(user_log)==0:
        reco_idx.extend(random.sample(news[news['category']==category[cate1]].index.tolist(),2))
        reco_idx.extend(random.sample(news[news['category']==category[cate2]].index.tolist(),3))
    # userlog에 해당하는 애가 있는 경우
    else:
        temp=[]
        #  추천 알고리즘 수행해서 3개 data 추출하기
        # userlog의 news index모두 추출
        nidx=user_log['news_id']
        similar_news_list=find_sim_news(news,genre_sim_sorted_ind, nidx ,3)
        temp.extend(similar_news_list)
        ### Ramdom 추출
        temp.extend(random.sample(news[news['category']==category[cate1]].index.tolist(),2))
        temp.extend(random.sample(news[news['category']==category[cate2]].index.tolist(),2))
        reco_idx=random.sample(temp,5)
    
    # user_id, reconewslist db에 전송하기
    link1,link2, link3, link4, link5 =news['url'][reco_idx[0]],news['url'][reco_idx[1]], news['url'][reco_idx[2]], news['url'][reco_idx[3]], news['url'][reco_idx[4]]
    
    update_sql="UPDATE Daily_Reco set News_link1=%s, News_link2=%s, News_link3=%s, News_link4=%s, News_link5=%s, News_id1=%s, News_id2=%s, News_id3=%s, News_id4=%s,News_id5=%s WHERE User_id=%s"
    cur.execute(update_sql, (link1,link2, link3,link4, link5,reco_idx[0], reco_idx[1], reco_idx[2], reco_idx[3], reco_idx[4] ,userid)) 
    con.commit()
    
    print(userid,"의 유저가 선호하는 뉴스는 ", news['headline'][reco_idx[0]])

print("complete")
