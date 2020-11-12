import pymysql
import datetime

def lookup_database():
    # 데이터베이스 조회
    con = pymysql.connect(host="localhost", user="root", password="1358",
            db="people", charset="utf8")
    now = datetime.datetime.now()
    
    cur_time = str(now.strftime('%Y-%m-%d %H:%M:%S'))
		
    try:
	
        cur = con.cursor()
        print("일단 연결은 됨")
        sql = f"SELECT * FROM people_counting where datetime='{cur_time}';"
                
        cur.execute(sql)
        result = cur.fetchall()
		
        print(result[-1])

    except:
        print('예외가 발생했습니다.')

    finally:
        con.close()

lookup_database()


