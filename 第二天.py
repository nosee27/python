class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name}在叫")

class dog(Animal):
    def speak(self):
        super().speak()
        print(f"{self.name}汪汪汪")

class cat(Animal):
    def speak(self):
        super().speak()
        print(f"{self.name}喵喵喵")
dog=dog("喜喜")
cat=cat("积极")
dog.speak()
cat.speak()
