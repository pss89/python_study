# 가변인자 이용한 함수
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") # end = " " 줄바꿈이 아닌 계속 출력
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name,age,*language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") # end = " " 줄바꿈이 아닌 계속 출력
    for lang in language:
        print(lang, end=" ")
    print()
    
profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")
profile("김태호",25,"Kotlin","Swift")

# 전역변수
gun = 10
def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용 (전역변수는 권장하지 않음)
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    
print("전체 총 : {0}".format(gun))
checkpoint(5)
print("남은 총 : {0}".format(gun))

# 지역변수
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))