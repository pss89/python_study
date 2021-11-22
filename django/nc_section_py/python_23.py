# 표준 입출력
print("Python","Java",sep=",",end="?") # sep 구분자
print("무엇이 더 재미있을까요?")
# print("Python"+"Java")
print("\n-------------------------------------\n")
# 예제 2
import sys
print("Python","Java",file=sys.stdout) # 표준출력
print("Python","Java",file=sys.stderr) # 표준에러
print("\n-------------------------------------\n")
# 예제 3
scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items(): # key, value 동시 출력
    # print(subject, score)
    print(subject.ljust(8),str(score).rjust(4), sep=":") #ljust, rjust는 str에서만 먹힘
print("\n-------------------------------------\n")
# 예제 4
# 은행 대기 순번표
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
print("\n-------------------------------------\n")
# 예제 5
answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
print("입력하신 값은 " + answer + "입니다.")