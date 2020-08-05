#coding=utf-8
a = 10
print(a*2)
print(a*3)
print(abs(1-100)-100)
print(max(1,2,3,4,5,6,7,120))
print(float('23456'))
print(str(123))
print(bool(-1))
print(bool(''))
print(bool(0))

#hex 转换
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

#定义绝对值函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-3.78))
#print(my_abs(str(12345)))

#定义空函数
def nop():
    pass

#解一元二次方程
import math
def quadratic(a,b,c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/2
    x2 = (-b-math.sqrt(b*b-4*a*c))/2
    return x1,x2
print(quadratic(2,3,1))

