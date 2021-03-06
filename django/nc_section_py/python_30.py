# 메소드, 상속, 다중상속, 연산자 오버로딩

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
# 유닛 클래스 상속받아 사용하기
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

#벌쳐
vulture = AttackUnit("벌쳐",80,10,20)
#배틀크루져
battlecruiser = FlyableAttackUnit("배틀크루져",500,25,3)

vulture.move("11시") # 상속받은 Unit 의 move 함수
# battlecruiser.fly("배틀크루져","9시")
battlecruiser.move("9시") # FlyableAttackUnit 클래스의 move 함수
print("\n----------------------\n")
# 발키리
valkyrie = FlyableAttackUnit("발키리",200,6,5) 
valkyrie.fly(valkyrie.name,"3시") # 상속받은 Flyable 클래스의 fly 함수
print("\n----------------------\n")
# 파이어뱃
firebat1 = AttackUnit("firebat",50,16,25) # AttackUnit 클래스의 함수들을 사용
firebat1.attack("5시")
# 두번 공격 받음
firebat1.damaged(25)
firebat1.damaged(25)