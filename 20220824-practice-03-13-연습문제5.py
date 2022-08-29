# 연습문제 5와 6
tmp = input('두 정수 및 세 정수를 입력해주세요. ').split(' ')
tmp_num = 0
for i in tmp :
    if tmp_num < i :
        tmp_num = i
    print('-- end ', i)
