import random
n = [random.randint(0, 100) for i in range(10)]
print(n)
d = {i + 1: 'pass' if n[i] >= 60 else 'nopass' for i in range(10)}
print(d)