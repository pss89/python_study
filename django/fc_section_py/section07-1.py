#section07-1
#파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수

#클래스, 인스턴스 차이 중요
#네임스페이스 : 객세를 인스턴스화 할 때 저장된 공간
#클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성 (전체 공유)
#인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용 (인스턴스 변수를 찾을 경우 없으면 클래스의 변수를 찾는다, 그래도 없으면 오류)

#선언

# class 클래스명:
#     함수
#     함수
#     함수


#예제 1
class UserInfo:
    #속성, 메서드
    # pass
    
    def __init__(self,name):
        # print("초기화",name)
        self.name = name

    def user_info_p(self):
        print("Name : ",self.name)

#네임스페이스
user1 = UserInfo('Park')
print(user1.name)
user1.user_info_p()
user2 = UserInfo('Kim')
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))
#네임스페이스 확인하기
print(user1.__dict__)
print(user2.__dict__)

print()

#예제2
#selft의 이해
class SelfTest:
    #클래스 함수
    def function1():
        print("function1 called!")
    #인스턴스 함수
    def function2(self):
        print(id(self))
        print("function2 called!")

#인스턴스화
self_test = SelfTest()
#selft_test.function1()
#클래스 함수
SelfTest.function1()
#인스턴스 함수
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)

#예제3
#클래스 변수, 인스턴스 변수

class WareHouse:
    #클래스 변수
    stock_num = 0
    def __init__(self,name):
        self.name = name
        WareHouse.stock_num +=1
    def __del__(self):
        WareHouse.stock_num -=1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) #클래스 네임스페이지, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

#자기 네임스페이스에 없으면 클래스의 네임스페이스에서 찾는다, 그래도 없으면 오류
print(user1.stock_num)

del user1

print(user2.stock_num)
print(user3.stock_num)