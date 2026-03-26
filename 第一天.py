class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"我的名字是{self.name},我今年{self.age}岁")
stu=student("乐乐",19)
print(stu.name)
print(stu.age)
stu.introduce()
