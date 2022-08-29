# 13
def cube(s) :
    print('모서리의 길이가 {}인 정육면체 : {}'.format(s, s ** 2))
    
def rectangular_parallelepiped(w, h, l) : 
    print('가로({}), 세로({}), 길이({}) 직육면체 : {}'.format(w, h, l, (w*h*l)))

def cone(r, h) :
    print('반지름({}), 높이({}) 원뿔(π) : {}'.format(r, h, (r ** 2) + (h ** 2)))

def sphere(r) :
    print('반지름({}) 구(π) : {}'.format(r, (4 * (2 ** 3))))

def cylinder(r, h) :
    print('반지름({}), 높이({}) 원기둥(π) : {}'.format(r, h, (r ** 2) * h))


cube(12)
cube(20)
rectangular_parallelepiped(3, 5, 6)
cone(20, 10)
sphere(15)
cylinder(20, 10)
