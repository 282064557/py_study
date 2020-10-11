print("hello,world!")

print("你是三哥") #打印

#缩进知识
if True:
    print("true")
else:
    print("false")

#多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
#total = item_one + \
  #      item_two + \
  #      item_three
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one','item_two','item_three'] 


#数字类型
# python中数字有四种类型：整数、布尔型、浮点数和复数。
#int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
#bool (布尔), 如 True。
#float (浮点数), 如 1.23、3E-2
#complex (复数), 如 1 + 2j、 1.1 + 2.2j

input("\n\n按下 enter 建后退出。")

input("")

import sys; x = 'runoob'; sys.stdout.write(x +'\n')
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

#多个语句构成代码组
'''
if Exception:
    suite
elif expression:
    suite
else:
    suite
'''  

#print输出
x = "a"
y = "b"
print(x)
print(y)
print("---------")
print(x,end=" ")
print(y,end=" ")
print()


import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv,path 
print("============cancai============")
print('path:',path)
print("请问一下你是谁!")
print("ni shi shiui ?")











