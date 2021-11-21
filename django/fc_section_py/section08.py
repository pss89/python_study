# section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대경로
# .. : 싱대경로
# . : 현재경로

#사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ",Fibonacci.fib2(400))
print("ex2 : ",Fibonacci().title)

# 사용2(권장하지는 않음) - 전부 가져오면 불필요한 리소스를 가져오기 때문에 권장 X
# import 시 , 단위로 가져올 수 있음
from pkg.fibonacci import *

Fibonacci.fib(300)

print("ex2 : ",Fibonacci.fib2(400))
print("ex2 : ",Fibonacci().title)

#사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(300)

print("ex3 : ",fb.fib2(400))
print("ex3 : ",fb().title)

#사용4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10,100))
print("ex4 : ", c.mul(10,100))

#사용5(함수)
from pkg.calculations import div as d
print("ex5 : ", int(d(100,10)))

#사용6(함수)
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))