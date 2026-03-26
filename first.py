#同一行为，使用不同对象，获得不同状态
#声明父类，子类工作
class Animal:
    def speak(self):
        pass
class dag(Animal):
    def speak(self):
        print("汪汪汪")
class cat(Animal):
    def speak(self):
        print("喵喵喵")
def make_noise(Animal):
    Animal.speak()

dog=dag()
cat=cat()
make_noise(dog)
make_noise(cat)

#抽象类
#没有具体的实现方法（pass）
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing(self):
        pass
class meidi(AC):
    def cool_wind(self):
        print("美的吹冷风")
    def hot_wind(self):
        print("美的吹热风")
    def swing(self):
        print("美的吹摇摆风")
class gree(AC):
    def cool_wind(self):
        print("格力吹冷风")
    def hot_wind(self):
        print("格力吹热风")
    def swing(self):
        print("格力吹摇摆风")
def make_cool(AC):
    AC.cool_wind()
meidi_ac=meidi()
gree_ac=gree()

make_cool(meidi_ac)
make_cool(gree_ac)