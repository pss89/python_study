# super

class Unit:
    def __init__(self):
        print("Unit 생성자")
        
class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # 두개 이상의 상속을 받을 경우 첫 인자의 상속자만 인식한다
        Unit.__init__(self)
        Flyable.__init__(self)
        
dropship = FlyableUnit()