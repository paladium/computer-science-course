e = 43
f=1276
for d in range(1,10000):
    result = (d * e - 1) % f
    if result == 0:
        print(d)

d = 1187