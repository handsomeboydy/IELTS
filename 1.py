from sympy import *
l1 = float(input('电感L1的值（H）为：'))
l2 = float(input('电感L2的值（H）为：'))
l3 = float(input('电感L3的值（H）为：'))
l4 = float(input('电感L4的值（H）为：'))
l5 = float(input('电感L5的值（H）为：'))

c1 = float(input('电感L1的值（F）为：'))
c2 = float(input('电容C2的值（F）为：'))
c3 = float(input('电容C3的值（F）为：'))
c4 = float(input('电容C4的值（F）为：'))
c5 = float(input('电容C5的值（F）为：'))

s = Symbol('s')
z1 = Symbol('Z1')
z2 = Symbol('Z2')
z3 = Symbol('Z3')
z23 = Symbol('Z23')
G = Symbol('G')

z1 = l1*s
z2 = 0.5*(l2*s+1/(c2*s)+1/(1/(l3*s)+c3*s)+1/(1/(l4*s)+c4*s))
z3 = 2+l5*s+1/(c5*s)
z23 = 1/((1/z2)+(1/z3))
G = z23/(z23+z1)
print('传递函数G(s)=',G)
