result = None

result = [list(range(1,101)) for x in range(100)]

for x in range(100):
    result[x].append(sum(result[x][:x+1]))

assert result[-1][-1] == 5050