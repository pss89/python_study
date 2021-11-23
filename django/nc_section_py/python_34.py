# 퀴즈 - 부동산 프로그램

class House:
    # 매물 초기화
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".\
        format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))
        pass
    
houses = []
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다".format(len(houses)))
for house in houses:
    house.show_detail()

# print("\n----------------------\n")

# list = [
# {'location':'강남','house_type':'아파트','deal_type':'매매','price':'10','completion_year':'2010'}
# ,{'location':'마포','house_type':'오피스텔','deal_type':'전세','price':'5','completion_year':'2007'}
# ,{'location':'송파','house_type':'빌라','deal_type':'월세','price':'500/50','completion_year':'2000'}
# ]

# for i in list:
#     for v in i.values():
#         print(i.find('location'))
#         # house_c = House()