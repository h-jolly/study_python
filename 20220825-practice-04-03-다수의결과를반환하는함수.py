# LAB 4-8
def muliples(a, b) :
    result_tmp = []
    for i in range(1, b+1) :
        result_tmp.append(a * i)

    return result_tmp

print(muliples(2, 5))
