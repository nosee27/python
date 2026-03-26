from logging import exception


def chufa(a,b):
    try:
        return a/b
    except exception as e:
        print(f"出现了错误{e}")
    finally:
        print("除法运行结束")
print(chufa(3,0))