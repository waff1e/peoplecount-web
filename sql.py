# 데이터베이스에 맞게 설정

import pymysql
import db
from datetime import datetime

def login(data):
    conn = db.get_db()
    sql = """
        select *
        FROM user_info
        WHERE id = %s
    """

    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            rs = cursor.execute(sql, data['id'])

            if rs == 0:
                return {'result': 'false', 'msg': '아이디 혹은 비밀번호가 다릅니다.'}

            item = cursor.fetchone()
            
            print(item['id'])
            print(item['pw'])
            
            if item['pw'] == data['pw']:
                return {'result': 'success', 'msg': '로그인 성공.', 'idx': item['idx']}
    finally:
        conn.close()


def get_data():
    conn = db.get_db()
    sql = """
           select *
           FROM trash
           order by idx DESC
       """
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            rs = cursor.execute(sql)

            if rs == 0:
                return {'result': 'success', 'data': {}}

            item = cursor.fetchall()
            lens = len(item)
            total = []
            month = [0 for i in range(12)]
            index = 1
            today = 0
            for obj in item:
                if datetime.today().strftime("%Y-%m-%d") == obj['time'].strftime('%Y-%m-%d'):
                    today += 1
                month[int(obj['time'].month)] += 1
                datas = {
                    "no": index,
                    "idx": obj['idx'],
                    "pos": obj['pos'],
                    "src": obj['img_src'],
                    "time": obj['time'].strftime('%Y-%m-%d-%H-%M')
                }
                total.append(datas)
                index += 1

            return {'result': 'success', 'data': total, "total": lens, "today": today, 'month': month}
    finally:
        conn.close()

