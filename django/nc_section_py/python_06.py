# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3="""
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
print("\n-------------------------------------\n")
# 슬라이싱
jumin = "890925-1234567"
print("성별 : "+jumin[7])
print("연 : " +jumin[0:2]) # 몇번째부터 몇번째를 가져올지
print("월 : "+jumin[2:4]) 
print("일 : "+jumin[4:6])
print("생년월일 : "+jumin[:6])
print("뒤 7자리 : "+jumin[7:])
print("뒤 7자리 (뒤에서부터) : "+jumin[-7:])
print("\n-------------------------------------\n")