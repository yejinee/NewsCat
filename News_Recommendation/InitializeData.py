import pymysql

######  DB 접속 #############################################
con=pymysql.connect(host='final-chatbot.c7dwoilcj9uq.ap-northeast-2.rds.amazonaws.com',user='yejin',password='1313', db='CHAT_BOT_DB', charset='utf8')
cur=con.cursor()

extract_ID="SELECT User_id FROM Users"
cur.execute(extract_ID)
user=cur.fetchall()
#### user id만 저장 ########
userid_list=[]
for u in user:
    userid_list.append(u[0])

#### Initialize Daily Reco Table  ######
## 1. 데이터 전부 삭제 
removeall_sql="DELETE FROM Daily_Reco"
cur.execute(removeall_sql) 
con.commit()


#### 2. 초기화 시킬 value (str) 넣기
reco_idx=['a','b','c','d','e']
for id in userid_list:
    sql = '''INSERT INTO Daily_Reco VALUES ('{}', '{}', '{}', '{}','{}','{}');'''.format(id, reco_idx[0],reco_idx[1], reco_idx[2], reco_idx[3], reco_idx[4] )
    cur.execute(sql) 
    con.commit()

print('complete')