# 23
def area_and_circumference():
    while(True):
        r = int(input('반지름을 입력해주세요. : '))
        if(r < 0):
            break
        a = r * 2 * 3.14
        b = r * r * 3.14
        print('넓이 : {:7.3f}, 둘레 : {:7.3f}'.format(a, b))

    print('프로그램을 종료합니다.')

area_and_circumference()
