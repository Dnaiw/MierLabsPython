from math import sqrt

z1 = complex(10, -31.85)
z2 = complex(2, 4.99)
z3 = complex(10, -15.92)
z23 = z2*z3/(z2+z3)
u = complex(150*sqrt(2), 0)

xc1 = complex(0, -31.85)
xl2 = complex(0, 4.99)
xc3 = complex(0, -15.92)

i1 = u/(z1 + z23)
i2 = i1*z3/(z2+z3)
i3 = i1*z2/(z2+z3)

print(abs(i1)**2*z1 + abs(i2)**2*z2 + abs(i3)**2*z3)

ur1 = i1*10
uc1 = i1*xc1
ur2 = i2*2
ul2 = i2*xl2
ur3 = i3*10
uc3 = i3*xc3

print("i1 - ", i1)
print("i2 - ", i2)
print("i3 - ", i3)
print("ur1 - ", ur1)
print("uc1 - ", uc1)
print("ur2 - ", ur2)
print("ul2 - ", ul2)
print("ur3 - ", ur3)
print("uc3 - ", uc3)
