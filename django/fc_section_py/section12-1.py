#section12-1
#파이썬 데이터베이스 연동(SQLite)

import sqlite3
import datetime

#삽입날짜 생성
now = datetime.datetime.now()
#년월일시분초밀리초
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('now datetime : ',nowDatetime)

# sqlite3
print('sqlite3.version : ' ,sqlite3.version)
print('sqlite3.sqlite_version : ' ,sqlite3.sqlite_version)

# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('D:/svc/webapp/python_buchet/resource/database.db',isolation_level=None)

# Cursor(실행하기 위한 함수?)
c = conn.cursor()
#클래스 타입
print('cursor type:', type(c))

# 테이블 생성(Data Type : TEXT NUMERIC INTEGER REAL BLOB)
# 테이블이 있는지에 따라 생성 or 그대로 사용하겠다 선언
# \ 사용 이유는 줄바꿈시 에러구문 방지 (escape 처리)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# c.execute("INSERT INTO users VALUES(1,'Park','seongsigbag2@gmail.com','010-8653-5941','Park.com',?)",(nowDatetime,))

# 튜플행태로 inset
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)",(2,'Kim','Kim@naver.com','010-1111-1111','Kim.com',nowDatetime))

# Many 삽입 (튜플, 리스트)
userList = (
    (3, 'Lee','Lee@naver.com','010-2222-2222','Lee.com',nowDatetime)
    ,(4, 'Joe','Joe@naver.com','010-3333-3333','Joe.com',nowDatetime)
    ,(5, 'Kang','Kang@naver.com','010-4444-4444','Kang.com',nowDatetime)
)
# c.executemany("INSERT INTO users(id,username,email,phone,website,regdate) VALUES(?,?,?,?,?,?)",userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# print('users db deleted : ', conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영(오토 커밋)
# isolation_level = None 아닐 경우 conn.commit() 실행해야 함

# 롤백
# conn.rollback()

# 접속 해제(리소스 반환을 위해)
# conn.close()