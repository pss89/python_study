# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for a1 in q1.keys():
    if(a1 == '가을'):
        print(q1[a1])
        break
print()

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for a2_key, a2_val in q2.items():
    if(a2_key == '사과' or a2_val == '사과'):
        print(a2_val)
        break
print()

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score1 = 100

if(score1 >= 81 and score1 <= 100):
    print('A학점')
elif(score1 >= 61 and score1 <= 80):
    print('B학점')
elif(score1 >= 41 and score1 <= 60):
    print('C학점')
elif(score1 >= 21 and score1 <= 40):
    print('D학점')
else:
    print('E학점')
print()

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
# a = 12
# b = 6
# c = 18
a, b, c = 12, 6, 18

best = a
if best > a:
    best = b
if c > b:
    best = c

print(best)
print()

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '890925-1178013'

if int(s[7]) & 2 == 0:
    print('여자')
else:
    print('남자')
print()

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
# for a in q3:
#     if a != '정':
#         print(a)

for a in q3:
    if a == '정':
         continue
    else:
         print(a)
print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for a in range(1,101):
    if a % 2 != 0:
        print(a, end=",")
print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for a in q4 :
    if len(a) >= 5:
        print(a)
print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for a in q5 :
    if a.islower():
        print(a,end=',')
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for a in q5 :
    if a.islower():
        print(a.upper(),end=',')
    elif a.isupper():
        print(a.lower(),end=',')

print()

#리스트 컴프레션(리스트 코딩 축약)
numbers = []

for n in range(1,101):
    numbers.append(n)

print(numbers)

numbers2 = [x for x in range(1,101)]
print(numbers2)