#section04-3
#파이썬 데이터 타입(자료형)
#리스트, 튜플

#리스트(순서 O, 중복 O, 수정 O, 삭제 O)
#선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen','Banana','Orange']
e = [10, 100, ['Pen','Banana','Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

#연산
print(c+d)
print(c*3)
print(c[0]+111)
print(str(c[0])+'hi')

#리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a','b','c']
print(c)

#원하는 index값을 찾아서 삭제
del c[1]
print(c)
del c[-1]
print(c)

print()
print()

#리스트 함수
y = [5,2,3,1,4]
print(y)
y.append(6) #끝에 추가
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7) #원하는 위치에 추가
print(y)
y.remove(2) #원하는 값을 찾아서 삭제
y.remove(7)
print(y)
y.pop() #마지막 값을 삭제(stack 구조 : lifo)
print(y)
ex = [88,77]
y.append(ex) #원소 그래도 추가(리스트 형태면 그대로 리스트 형태로 추가)
print(y)
del y[4]
y.extend(ex) #원소를 배열에 맞게 추가
print(y)

#삭제 : del, remove, pop

#튜플 (순서 O, 중복허용 O, 수정 X, 삭제 X)
a = ()
b = (1,)
c = (1,2,3,4)
d = (10,100,('a','b','c'))

print(c[2])
print(c[3])
print(d[2][1])
print(d[2:])
print(d[2][0:2])

#튜플 연산
print(c+d)
print(c*3)

print()
print()

#튜플 함수
z = (5,2,1,3,4)
print(z)
print(3 in z)
print(z.index(5))
print(z.count(1)) #해당 값이 몇개 있는지 체크