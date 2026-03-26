#单继承
#class 类名（父）:
class Phone:
    imei=None
    producer=None
    def call_by_4g(self):
        print("4g通话")
class Phone2022(Phone):
    face_id=True
    def call_by_5g(self):
        print("5g通话")
phone=Phone2022()
phone.call_by_5g()
phone.call_by_4g()
print(f"{phone.imei}")
#多继承
#class 类名（父类1，父类2.。。。）：
#pass 输出同名属性，越先越优先
class xiaomi:
    id=1011
    producer="xiaomi"
    def kaiji(self):
        print("成功开机")
class zhaoxiang:
    zx="laiya"
    def photo(self):
        print("拍照")
class myphone(xiaomi,zhaoxiang):
    pass
phone=myphone()
phone.photo()