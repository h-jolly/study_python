# LAB 5-4
# 1번 문제
print(' --- 1번 --- ')

a = [1, 2, 3]
b = [10, 20, 30]
a.append(b)
print('append 테스트 :', a)

a = [1, 2, 3]
b = [10, 20, 30]
a.extend(b)
print('extend 테스트 :', a)

print()

# 2번, 3번, 4번, 5번 문제
print(' --- 2번, 3번, 4번, 5번 문제 --- ')
print()

# 2번 문제
nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('2번 - 초기 값 :', nlist)

# 3번 문제
nlist.insert(0, 0)
print('3번 - ',nlist)

# 4번 문제
nlist.reverse()
print('4번 - ', nlist)

# 5번 문제
nlist.pop(-1)
print('5번 - ', nlist)
