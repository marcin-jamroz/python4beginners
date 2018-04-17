A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

result = set()
result.add(frozenset())

for x in A:
    tmp = set()
    for i in result:
        tmp.add(i.union(frozenset((x,))))
    result.update(tmp)

    

assert frozenset((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) in result


print(len(result))

result = sorted(result)
print("Result")
for x in result:
    print(x)