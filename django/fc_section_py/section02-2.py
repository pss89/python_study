# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this """파이썬의 장점들 설명글"""
import sys

# 파이썬 기본 인코딩 - 파이썬 2.x : 유니코드, 파이썬 3.x : UTF-8
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is pss')

# 변수 선언
myName = 'pss'

# 조건문
if myName == 'pss':
    print('Ok')

# 반복문 (구구단)
for i in range(1, 10):
    for j in range(1,10):
        print('%d * %d = ' % (i,j), i*j)

# 변수 선언(한글)
이름 = "좋은사람"

# 출력
print(이름)

# 함수 선언(한글)
def 인사():
    print('안녕하세요')
    
인사()

# 함수 선언(영어)
def greeting():
    print('Hello!')

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))