# 변수
animal = "강아지"
name = "해피"
age = 4
hobby = "산책"
is_adult = age >= 3

# , 처리하면 자동으로 띄어쓰기 처리 되어 부자연스러움
# print("우리집",animal,"의 이름은 연탄이에요")
# print(name,"는 ",age,"살이며, ",hobby,"을 아주 좋아해요")
# print(name,"는 어른일까요? ",is_adult)

print("우리집 "+animal+"의 이름은 "+name+"이에요")
hobby = "공놀이"
print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
print(name+"는 어른일까요? "+str(is_adult))

# 주석
''' 
여러줄을 주석
처리할 수
있습니다
'''

print("\n-------------------------------------\n")

# 퀴즈
station = ['사당','신도림','인천공항']

for v in station:
    print(v + '행 열차가 들어오고 있습니다')