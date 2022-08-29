# 10
x1 = int(input('x1 좌표를 입력해주세요 : '))
y1 = int(input('y1 좌표를 입력해주세요 : '))
x2 = int(input('x2 좌표를 입력해주세요 : '))
y2 = int(input('y2 좌표를 입력해주세요 : '))

def distance(x1, y1, x2, y2) :
    d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    print('두 점의 거리 :', d)

distance(x1, y1, x2, y2)

print()

# 11


print()

# 12
def cal_area(width, height):
    return 0.5 * width * height

width = int(input('밑변 : '))
height = int(input('높이 : '))

area = cal_area(width, height)
print('삼각형의 면적 :', area)
