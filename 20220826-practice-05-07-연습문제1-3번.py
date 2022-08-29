# 1번과 2번은 X
# 3번
list = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for i in list:
    for j in list2:
        print('{} * {} = {}'.format(i, j, i * j))
