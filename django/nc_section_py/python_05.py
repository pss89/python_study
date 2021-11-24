# 랜덤 함수

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의값 생성
print(int(random()*10)) # 정수형으로 노출되도록
print(int(random()*10)+1) # 1~10 이하의 임의의값 생성

print("\n-------------------------------------\n")
#로또
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print("\n-------------------------------------\n")
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print("\n-------------------------------------\n")
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))

print("\n-------------------------------------\n")
# 퀴즈
off_word_date=randint(4,28)

print('오프라인 스터디 모임 날짜는 매월 '+str(off_word_date)+' 일로 선정되었습니다.')