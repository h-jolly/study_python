# 중첩 loop


print('--- double_for_pattern')
n = 7
for i in range(n) :
    st = ''
    for j in range(i) :
        st += ' '
    print(st + '#')

print()
print('--- for_pattern')

n = 7
for i in range(n) :
    print(' ' * i + '#')

print()
print('--- for_pattern, 반')

n = 7
for i in range(n-1, 0, -1) :
    print(' ' * i + '#')

