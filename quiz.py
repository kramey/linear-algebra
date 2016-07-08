from vector import *

# Problem 1
v1 = Vector([8.218,-9.341])
v2 = Vector([-1.129,2.111])
print v1, '+', v2, '=', v1.add(v2)

# Problem 2
v3 = Vector([7.119,8.215])
v4 = Vector([-8.223,0.878])
print v3, '-', v4, '=', v3.subtract(v4)

# Problem 3
scalar = 7.41
v5 = Vector([1.671,-1.012,-0.318])
print scalar, 'X', v5, '=', v5.scale(scalar)
