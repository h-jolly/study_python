# 14번
spell = ['h', 'a', 'p', 'p', 'y', ' ', 'b', 'i', 'r', 't', 'h', 'd', 'a', 'y']

print('14-1)', spell[1:5]) # ['a', 'p', 'p', 'y']
print('14-2)', spell[:]) # ['h', 'a', 'p', 'p', 'y', ' ', 'b', 'i', 'r', 't', 'h', 'd', 'a', 'y']
print('14-3)', spell[:5]) # ['h', 'a', 'p', 'p', 'y']
print('14-4)', spell[6:]) # ['b', 'i', 'r', 't', 'h', 'd', 'a', 'y']

print()

# 15번
greet = 'Have a beautiful day.'
print('15-1)', greet[:4])
print('15-2)', greet[7:17])
print('15-3)', greet[-4:-1])

print()

# 16번
s = 'Birthday'
print('16-1)', s[:5]) # Birth
print('16-2)', s[5:]) # day
print('16-3)', s[1:-1]) # irthda
print('16-4)', s[::-1]) # yadhtriB
print('16-5)', 'day' in s) # True
print('16-6)', 'birth' in s) # False
print('16-7)', 'Birth' in s) # True
print('16-8)', 'Birth' not in s) # False
