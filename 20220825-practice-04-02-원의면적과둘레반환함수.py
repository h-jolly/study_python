# LAB 4-7 : 원의 면적과 둘레를 반환하는 함
def circle_area_circum(radius) :
    area = radius * 2 * 3.14
    circum = (radius ** 2) * 3.14
    
    return area, circum

radius = 10
area, circum = circle_area_circum(radius)

print('반지름 {}인 원의 면적은 {}, 원의 둘레는 {}'.format(radius, circum, area))
