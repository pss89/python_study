#section07-2
#파이썬 클래스 상세 이해
#상속, 다중상속

#예제1
#상속 기본
#슈퍼클래슼(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

#라면 -> 속성(종류, 회사, 맛, 면종류, 이름) : 부모

class Car:
    """ Parent Class """
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'


class BmwCar(Car):
    """ Sub Class """
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """ Sub Class """
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

#일반 사용
model1 = BmwCar('520d', 'sedan', 'red')
print(model1.color)
print(model1.type)
print(model1.car_name)
print(model1.show())
print(model1.show_model())
print(model1.__dict__)

#Method Overriding(오버라이딩) - 코드 재정의
model2 = BenzCar("220d","suv","black")
#부모클래스에 show 메서드가 있지만 model2 인스턴스화 시킨 클래스 BenzCar 클래스의 show 메서드를 실행시킨다
print(model2.show())

#Parent Method Call
model3 = BenzCar("350s","sedan","silver")
print(model3.show())
print(model3.show())

# Inheritance Info(인스턴스 정보)
print(BmwCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(B,A,Z):
    pass

print(M.mro())
print(A.mro())