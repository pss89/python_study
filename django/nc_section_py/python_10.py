# 딕셔너리
cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]) 오류
# print(cabinet.get(5)) # None (오류 x)
print(cabinet.get(5,"사용가능")) # 기본값은 사용가능, 있으면 5의 값 출력
print("\n-------------------------------------\n")
print(3 in cabinet) # boolean 리턴 (true)
print(5 in cabinet) # false
print("\n-------------------------------------\n")
cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print("\n-------------------------------------\n")
cabinet["A-3"] = "김종국"
cabinet["C-30"] = "조세호"
print(cabinet)
print("\n-------------------------------------\n")
del cabinet["A-3"]
print(cabinet)
print("\n-------------------------------------\n")
print(cabinet.keys()) # key 출력
print(cabinet.values()) # value 출력
print(cabinet.items()) # key, value 동시 출력
print("\n-------------------------------------\n")
cabinet.clear()
print(cabinet)