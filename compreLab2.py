def mydict(**p):
    d = {}
    if p:
        d = {'my' + str(i): p[i] for i in p}
    return d
print(mydict(a=1, b=2, c=3))
print(mydict())
print(mydict(교육='멀티캠퍼스', 현재='파이썬'))