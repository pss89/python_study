#section04-4
#파이썬 데이터 타입(자료형)
#딕셔너리, 집합 자료형

#딕셔너리(Dictionary) : 순서 X, 중복 X, 수정 O, 삭제 O
#key,value ( json 형식과 비슷 ) -> MongoDB와 비슷

#선언
a = {'name':'Park','Phone':'010-8653-5941','birth':890925}
b = {0:'Hello Python',1:'Hello Coding'}
c = {'arr':[1,2,3,4,5]}

#print(type(a))

#출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

#딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1,2,3,4]
a['rank2'] = (1,2,3,4)
print(a)

#keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(2 in b)
print('name2' not in a)

#집합 (Sets) (순서 X, 중복 X)
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a))
print(c)

t = tuple(b)
print(t)

l = list(b)
print(l)

print()
print()

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합
print(s1.intersection(s2))
print(s1 & s2)

#합집합
print(s1 | s2)
print(s1.union(s2))

#차집합
print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7,8,10,15])

s3.add(18)
#s3.add(7)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))