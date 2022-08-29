# 18# 18
def findleast(a, b):
    bNotFnd = True
    i=1
    while bNotFnd:
        i += 1
        c = b * i
        for x in range(a, b):
            if c % x is not 0: break
            if x is b - 1: return c

start = int(input('범위의 시작 정수 : '))
end = int(input('범위의 마지막 정수 : '))

print('{0:}에서 {1:}까지의 정수들의 최소 공배수 : {2:}'.format(start, end, findleast(start, end)))
