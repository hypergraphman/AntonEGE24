from itertools import product

print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f = (w <= z) and (y <= w) or ((w or y) == x)
    if not f:
        print(x, y, z, w)