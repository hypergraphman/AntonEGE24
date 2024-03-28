from time import time

cur = time()
for a in range(1, 100000):
    if all(((x % 45 == 0) or (x % 30 == 0)) <= (x % a == 0) for x in range(1, 100000)):
        print(a)
print(time() - cur)