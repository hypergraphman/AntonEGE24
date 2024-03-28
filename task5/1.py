def f(n):
    d1, d2, d3 = map(int, str(n))
    sum_1 = d1 + d2
    sum_2 = d2 + d3
    if sum_1 > sum_2:
        return str(sum_1) + str(sum_2)
    return str(sum_2) + str(sum_1)


for i in range(100, 1000):
    if f(i) == '145':
        print(i)
        break
