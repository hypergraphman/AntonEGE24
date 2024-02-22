from itertools import product

print('x y z w f')
for x, y, z, w in product((0, 1), repeat=4):
    f = int(((w <= (not x)) == (z <= y)) and ((not y) <= w))
    print(x, y, z, w, f)
