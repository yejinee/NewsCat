
import pandas as pd 
import pymysql
from time import sleep

# 집어넣는 것들 되어있음 
class Userquery():
    ## 유저 선호도 기록
    def __init__(self, User_id, pref):
        self.userid = User_id
        self.pref = pref

    ###### 예진 추가 ) 이때 초기화 같이 진행
    def querrytords(self):
        conn = pymysql.connect(host='final-chatbot.c7dwoilcj9uq.ap-northeast-2.rds.amazonaws.com', user='yschoi', password='mm001138', db='CHAT_BOT_DB', charset='utf8') 
        cursor = conn.cursor() 
        sleep(1)
        cat_list = []
        for c in self.pref.split()[1:]:
            cat1 = 0
            if c == '정치':
                cat1 = 0
            elif c == '경제':
                cat1 = 1
            elif c == '사회':
                cat1 = 2
            elif c == '국제':
                cat1 = 3
            elif c == '스포츠':
                cat1 =4 
            cat_list.append(cat1)

        sql = "insert into Users(User_id,Preference_1,Preference_2) \
                values('{}','{}','{}');".format(self.userid,
                                                cat_list[0], cat_list[1] )
        cursor.execute(sql)
        conn.commit()

        #### 좋아하는 뉴스 Table ( Reco_News) 도 같이 초기화############
        reco_idx=['a','b','c','d','e']
        newsidx=[0,1,2,3,4]

        Reco_sql = "INSERT INTO Daily_Reco VALUES (%s, %s, %s, %s,%s,%s,%s,%s, %s, %s,%s);"
        cursor.execute(Reco_sql,(self.userid, reco_idx[0],reco_idx[1], reco_idx[2], reco_idx[3], reco_idx[4] , newsidx[0],newsidx[1],newsidx[2],newsidx[3],newsidx[4]) ) 
        conn.commit()
        print("Complete  Initializing Users & Daily_Reco Table")


    def send_reco(self):
        conn = pymysql.connect(host='final-chatbot.c7dwoilcj9uq.ap-northeast-2.rds.amazonaws.com',
                             user='yschoi', password='mm001138',
                              db='CHAT_BOT_DB', charset='utf8') 
        cursor = conn.cursor() 
        sleep(1)
        query_test = 'select * from Daily_Reco where User_id = {};'.format(self.userid)
        user_reco = pd.read_sql_query(query_test, conn)
        reco_list = [link for link in user_reco.iloc[0,1:6]]
        return reco_list
    
    def send_like(self):
        conn = pymysql.connect(host='final-chatbot.c7dwoilcj9uq.ap-northeast-2.rds.amazonaws.com',
                             user='yschoi', password='mm001138',
                              db='CHAT_BOT_DB', charset='utf8')
        cursor = conn.cursor()
        sleep(1)
        b = [i for i in self.pref.split()][1:]
        print(b)
        query_test = 'select * from Daily_Reco where User_id = {};'.format(self.userid)
        user_like = pd.read_sql_query(query_test, conn)
        for i in b:
            news = user_like.iloc[:,int(i)+5]
            sql = "insert into User_log(User_id, News_id, News_like) \
                values('{}','{}','{}');".format(self.userid,
                                                int(news),1)
            print(sql)
            cursor.execute(sql)
            conn.commit()


        #li = [0,0,0,0,0]
        #for i in b:
        #    li[int(i)] = 1

        


        






    
    