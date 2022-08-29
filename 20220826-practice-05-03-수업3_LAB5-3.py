# LAB 5-3
# 1번과 2번 문제 
print(' --- 1번과 2번 문제 --- ')
prime_list = [2, 3, 5, 7]
print('소수 목록 :', prime_list)

print()

# 1번
print(' --- 1번 --- ')
prime_list.append(11)
print('추가 후 소수 목록 :', prime_list)

# 2번
print(' --- 2번 --- ')
if 3 in prime_list:
    prime_list.remove(3)
print('추가 후 소수 목록 :', prime_list)

print()
print()

# 3번과 4번 문제 
print(' --- 3번과 4번 문제 --- ')
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가 목록 :', prime_list)

print()

# 3번
print(' --- 3번 --- ')
nations.append('Nepal')
print('추가 후 국가 목록 :', prime_list)

# 4번
print(' --- 4번 --- ')
def isnation(nation):
    isnationyn = True
    if nation not in nations:
        isnationyn = False

    print('{}는(은) 국가 목록에 {}'.format(nation, ('있습니다.' if isnationyn else '없습니다.')))        

isnation('Japan')
isnation('Russia')
