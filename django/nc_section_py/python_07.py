#문자열 함수
python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper()) # boolean 값으로 리턴
print(len(python))
print(python.replace("Python","Java")) # 특정문자 변경
print("\n-------------------------------------\n")
index = python.index("n") # 해당글자가 몇번째에 있는지
print(index)
index = python.index("n",index+1) # 해당문자의 index 중 2번째 값
print(index)
print(python.find("Java")) # -1 반환
# print(python.index("Java")) # 오류
print(python.count("n")) # 해당 문자 갯수 확인
print("\n-------------------------------------\n")
# 문자열 포맷
print("나는 %d살입니다" % 20) # 숫자
print("나는 %s를 좋아해요." % "파이썬") #문자열
print("Apple 은 %c로 시작해요" % "A") #문자
# %s로 하면 포맷 상관없이 가능
print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간")) # 순서대로 포맷에 맞게 정의 됨
print("\n-------------------------------------\n")
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))
print("\n-------------------------------------\n")
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20,color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간",age=20))
print("\n-------------------------------------\n")
# python 3.6 이상부터 가능
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")