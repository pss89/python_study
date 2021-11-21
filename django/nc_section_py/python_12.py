# 세트 - 집합
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}
print("\n-------------------------------------\n")
java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

# 교집합 ( java, python 동시 만족 )
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 ( 둘중에 하나 만족)
print(java | python)
print(java.union(python))

# 차집합 ( 자바는 ok, 파이썬 x)
print(java - python) # {'김태호','양세형}
print(java.difference(python))

# python 추가
python.add("김태호")
print(python)

# java 제거
java.remove("김태호")
print(java)