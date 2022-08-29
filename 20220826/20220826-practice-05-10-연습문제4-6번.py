# 6번
list1 = [2, 3, 4, 1, 32]

print('max :', max(list1)) # 32
print('sum :', sum(list1)) # 42
list1.remove(32)
print('max :', list1) # [2, 3, 4, 1]
list1.reverse()
print('max :', list1) # [1, 4, 3, 2]
list1.sort()
print('max :', list1) # [1, 2, 3, 4]
