# 라즈베리파이 ip주소로 변경

import pymysql

# MySQL Connection 연결
def get_db():
    conn = pymysql.connect(host='localhost', user='root', password='1358',
                       db='myproject', charset='utf8', autocommit=False)

    return conn
