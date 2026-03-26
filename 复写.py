#调用父类成员
#父类名.成员变量
#父类名.成员方法（self）
#super().成员变量
#super().成员方法()
#father
class phone():
    id=1011
    def wifi(self):
        print("使用4g")
class myphone(phone):
    id=110 #复写
    def wifi(self):
        #方式一
        #print(f"父类的id是{phone.id}")
        #phone.wifi(self)
        #方式二
        print(f"父类的id是{super().id}")
        super().wifi()
        print("使用5g") #复写方法
p=myphone()
p.wifi()
