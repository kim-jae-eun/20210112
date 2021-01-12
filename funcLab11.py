def mydict(**p):
    d = {}
    if len(p) > 0: # if p 라고만 해도 됨. p가 빈 집합이면 False라서
        for i in p:
            d['my ' + i] = p[i]
    return d

print(mydict(a=1, b=2, c=3))
print(mydict())
print(mydict(교육='멀티캠퍼스',현재='파이썬'))