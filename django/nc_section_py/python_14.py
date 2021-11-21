# if
# weather = "맑음"
weather = input("오늘 날씨는 어때요? ") # prompot
if weather == "비" or weather == "눈":
    print("우산 쓰자")
elif weather == '미세먼지':
    print('마스크 챙기기')
else:
    print("그냥 나가자")

# 학점
grade = input("너의 수학 등급은?")
grade = int(grade)
if grade >= 90 :
    print("A")
elif grade < 90 and grade >= 70:
    print("B")
elif grade < 70 and grade >= 50:
    print("C")
elif grade < 50 and grade >= 30:
    print("D")
else:
    print("F")