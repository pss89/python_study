# 튜플
# key or value 값을 수정할 순 없지만 속도는 빠름
menu = ("돈끼스","치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선끼스") # 오류
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국",20,"게임")
print(name, age, hobby)