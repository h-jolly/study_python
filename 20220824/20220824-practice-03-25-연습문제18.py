# 연습문제 22
for i in range(2, 13) :
    nflag = True
    for j in range(2, i) :
        if i%j == 0 :
            nflag = False
            break
    if nflag :
        print(i, ': 소수')
    elif nflag :
        print(i, ': 합소수')
