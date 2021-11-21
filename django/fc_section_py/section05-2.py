#section05-2
#파이썬 흐름제어 반복문
#반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is : ",v1)
    v1 += 1

print()

for v2 in range(10):
    print("v2 is : ",v2)

print()

for v3 in range(1,10):
    print("v3 is : ",v3)

print()

#1~100합

sum1=0
cnt1=1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1~100: ', sum1)
print('1~100: ', sum(range(1,101)))
print('1~100: ', sum(range(1,101,2))) #두개 단위로 1~101전까지 계산해라
print()
# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 류플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ['Kim','Park','Cho','Choi','Yoo']

for name in names:
    print('You ar : ',name)

word = "dreams"

for s in word:
    print('word : ',s)

my_info = {"name":"Kim","age":33,"city":"seoul"}

#기본값은 키
for key in my_info:
    print("my_info",key)

#값
for key in my_info.values():
    print("my_info",key)

#키
for key in my_info.keys():
    print("my_info",key)

#키 and 값
for k,v in my_info.items():
    print("my_info",k,v)

name = "KennRY"
for n in name:
    if n.isupper():
        print(n.lower())
    else :
        print(n.upper())

# break
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]
for n in numbers:
    if n == 33:
        print('found:33!')
        break
    else:
        print('not found:33!')

#for-else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for n in numbers:
    if n == 33:
        print('found:33!')
        break
    else:
        print('not found:33!')
else:
    print("not founct 33.....")

# continue

lt = ["1",2,5,True,4.3,complex(4)]

for n in lt:
    if type(n) is float:
        continue
    else:
        print(type(n))

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))