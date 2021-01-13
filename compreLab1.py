def createList(*p, type=1):
    if len(p) == 0:
        p = [i for i in range(1, 31)]
    if type == 1:
        return list(p)
    if type == 2:
        return [i for i in p if i % 2 == 0]
    if type == 3:
        return [i for i in p if i % 2 == 1]
    if type == 4:
        return [i for i in p if i > 10]

print(createList())
print(createList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
print(createList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, type=2))
print(createList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, type=3))
print(createList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, type=4))