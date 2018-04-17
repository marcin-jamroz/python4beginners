result = None

result = list(range(1000))
for x in result:
    if x % 5 == 0 and x % 3 ==0:
        result[x] = "trzypięć"
    elif x % 5 == 0:
        result[x] = "pięć"
    elif x % 3 == 0:
        result[x] = "trzy"

assert result[15] == "trzypięć"