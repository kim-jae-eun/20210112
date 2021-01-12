def myprint(*p, **q):
    sep, deco = ',', '**'
    if len(p) != 0:
        if 'sep' in q: # q.get('sep',',') 이런 식으로 할 수도 있음
            sep = q['sep']
        if 'deco' in q:
            deco = q['deco']
        p = [str(i) for i in p]
        print(deco, sep.join(p), deco, sep='')
    else:
        print('Hello Python')

myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
myprint()