# pass

# 일반유닛
class Unit: # 부모클래스
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".\
            format(self.name,location,self.speed))
        # self.damage = damage
        # print("{0} 유닛이 생성되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))
        
# 공격유닛
class AttackUnit(Unit): # 자식클래스
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed) # 상속받은 클래스의 생성자를 상속받아 사용, 기존과 동일하게 self 를 사용할 수 있음
        self.damage = damage
        
    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))
        
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed # 멤버변수
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flying_speed))

# 클래스 다중상속
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_spped):
        # 멤버변수 초기화
        AttackUnit.__init__(self,name,hp,0,damage) #지상 speed 0
        Flyable.__init__(self,flying_spped)
    
    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

# 건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        pass # 통과시킨다 반복문의 continue 같은 느낌..
    
# 서플
supply_depot = BuildingUnit("서플라이 디폿",500,"7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    pass

game_start()
game_over()
