# 常量
注意：python语法中是没有常量的概念，但是在程序的开发中会涉及到常量的概念

```python
#小写字母全为大写代表常量，这只是一种约定，规范
$AGE_OF_WZF = 73 
```
# 修改
无

# 数据类型
整数型：int
```python
>>>作用：记录年龄，身份证等没有小数点的数字
>>>定义：
age = 18                   #定义年龄
print(type(age))           #输出年龄

```
浮点类型：float
```python
>>>作用：记录薪资，身高，等带小数点的数字
>>>定义：
height = 168          #定义身高值
print（height）       #输出身高
```
数字类型其他使用
```python
level = 1           #level值等于1
level = level + 1   #level值上层已经赋予了1，所以是1+1，现在的level是等于3
print(level)        #输出2
print(level*3)      #输出6 
print(10 + 1.3)     #输出11.3(备注整数类型是可以和浮点数相加的)
```
字符串类型：
```python
>>>作用：记录描述性质的状态，名字，一段话
>>>定义：用引号（'',"",''' ''',""  ""）包含的字符串
ccvfx = "请问你今天吃了饭没有？"
print（ccvfx）
#'name' = "egon" 这个是错误的语法，左边是变量名
#字符串的嵌套，注意：外层用单引号，内存应该用双引号，反之
print("my name is \'666\'")
print('you name is "4444"')
#字符串直接也是可以相加的
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("my name is" + "666")  
 或者 
a = "my name is"
name="ccvfx"
print(a + name)
#字符串可以相乘
print（a*10）
```

列类型：
```python
>>>
>>>
info = ["wuzhifeng",18,"我是谁？"]
print(info[0])
>>>输出结果为：wuzhifrng
wangxiao_info = [["吴志峰",19,"你是谁?"],["王建夫",18,"我是你爸爸?"]]
print(wangxiao_info[0][0],wangxiao_info[1][0])
>>>输出结果为【吴志峰 王建夫】
```
布尔类型：z

```python
>>>作用：
>>>定义：
```
