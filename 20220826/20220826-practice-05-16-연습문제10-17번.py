# 17번
animals = ['dog', 'cat', 'tiger', 'lion']

print('animals =', animals)
print('animals =', (animals[1:]+animals[:1]))
for i in range(len(animals)):
    print('I love {}'.format(animals[i]))

