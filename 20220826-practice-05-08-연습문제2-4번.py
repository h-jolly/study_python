# 4번
a = [2, 3, 4, 5, 6]
rew_a = []
for i in range(len(a), -1, -1):
    rew_a.append(a[i-1])

print(rew_a)
