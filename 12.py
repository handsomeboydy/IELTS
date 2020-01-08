import nath
from decimal import *

s =Decimal(0)

class Boundary():
# 定义线路边界的第一段阻抗
    def type1(l1):
        z1 = l1*s
# 定义线路边界的第二段阻抗
    def type2(l21,l22,l23,c21,c22,c23):
        z2 = 0.5*((1/(l21)))
# 定义线路边界的第三段阻抗
    def type3():
        z3 = 
# 定义一个求边界传递函数的方法
    def tf(z1,z2,z3):
        return ((z1*z2)/(z1+z2))/(((z1*z2)/(z1+z2))+z1)
