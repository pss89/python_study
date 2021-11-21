# 한줄 for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)
print("\n-------------------------------------\n")
students = ["Iron Man","Thor","Hulk"]
students = [len(i) for i in students] # 리스트의 값에 대한 길이 반환
print(students)
print("\n-------------------------------------\n")
students = ["Iron Man","Thor","Hulk"]
students = [i.upper() for i in students]
print(students)
print("\n-------------------------------------\n")
# 퀴즈

from random import *
cnt = 0
for customer in range(1,51):
    # time = randint(5,50)
    time = randrange(5,51)

    # if time >= 5 and time <= 15:
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 :{1}분)".format(customer,time))
        cnt += 1
    else:
        print("[X] {0}번째 손님 (소요시간 :{1}분)".format(customer,time))

print("총 탑승 승객 : {0} 분".format(cnt))