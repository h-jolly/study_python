def cel2fah(cel) :
    for i in range(10, cel + 1, 10) :
        fahrenheit = (9/5) * i + 32
        print('섭씨 {}도 = 화씨 {}도'.format(cel, fahrenheit))

cel2fah(50)
