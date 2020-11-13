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
        sql = f"SELECT * FROM people_counting where datetime='{cur_time}';"
                
        cur.execute(sql)
        result = cur.fetchall()
		

    except:
        print('예외가 발생했습니다.')

    finally:
        con.close()
	
    return result # 나중에 오류가 난다면 여기를 의심해볼 것
