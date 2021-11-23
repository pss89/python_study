# 스타크래프트 프로젝트 전반전
from random import *

# 일반유닛
class Unit: # 부모클래스
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self,location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".\
            format(self.name,location,self.speed))
        
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        
# 공격유닛
# 유닛 클래스 상속받아 사용하기
class AttackUnit(Unit): # 자식클래스
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed) # 상속받은 클래스의 생성자를 상속받아 사용, 기존과 동일하게 self 를 사용할 수 있음
        self.damage = damage
        
    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
        
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    seize_developed = False # 시즈모드 개발 여부
    
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return 
        
        # 시즈모드 아닐 때 > 하면 됨
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환됩니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else: # 시즈모드 일 때 > 풀면 됨
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

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
        self.fly(self.name,location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked = False # 클로킹모드 (해제상태)
        
    def clocking(self):
        if self.clocked == True: # 클로킹모드 일 때 > 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else: # 클로킹모드 해제 > 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True
            
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")
    
# 실제 게임
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리
attacks_units = []
attacks_units.append(m1)
attacks_units.append(m2)
attacks_units.append(m3)
attacks_units.append(t1)
attacks_units.append(t2)
attacks_units.append(w1)
print("\n----------------------\n")

# 전군 이동
for unit in attacks_units:
    unit.move("1시")
    
print("\n----------------------\n")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비 (탱크 시즈모드, 레이스 클로킹, 마린 스팀팩)
for unit in attacks_units:
    if isinstance(unit,Marine): # 어떤 객체의 instance인지 확인
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

# 전군 피해
for unit in attacks_units:
    unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음 (5 ~ 20)
    
game_over()