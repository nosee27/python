import os
from shlex import join

result_list=[]
i=0
for file_name in os.listdir("."):
    #只处理.txt文件
    if file_name.endswith(".txt"):
        try:
            f=open(file_name,"r",encoding="utf-8")
            line=f.readlines()
            line_count=len(line)

            i=f"{file_name}有{line_count}行"
            print(i)
            result_list.append(i)
        except Exception as e:
            print(f"出现了{e}错误")
            print(i)
            result_list.append(i)
#输出
f=open("result.txt","w",encoding="utf-8")
f.write("\n".join(result_list))


