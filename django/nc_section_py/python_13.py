# 자료구조의 변경
menu = {"커피","우유","주수"} # set
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

print("\n-------------------------------------\n")

# 퀴즈
from random import *
def issued():
    users = range(1,21)
    users = list(users)
    # print(users,type(users))
    shuffle(users)

    winners = sample(users,4) # 4명중에서 1명은 치킨, 3명은 커피
    print("-- 당첨자 발표 --")
    print("치킨 당첨자 : {0}".format(winners[0]))
    print("커피 당첨자 : {0}".format(winners[1:4]))
    print("-- 축하합니다 --")
    # shuffle_list = sample(list,1)
    # coffe = shuffle(list)
    # print(shuffle_list)

issued()