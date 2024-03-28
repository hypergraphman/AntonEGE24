def f(n):
    d1, d2, d3 = map(int, str(n))
    a = [d1 * 10 + d2, d1 * 10 + d3,
         d2 * 10 + d1, d2 * 10 + d3,
         d3 * 10 + d2, d3 * 10 + d1,]
    nums = []
    for x in a:
        if x > 9:
            nums.append(x)
    return max(nums) - min(nums)


print(f(131))