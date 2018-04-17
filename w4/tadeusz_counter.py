from collections import Counter

with open("pan_tadeusz.txt") as file:
    counter = Counter()
    for line in file:
        words = line.split()
        words = [w for w in words if len(w) > 3]
        counter.update(words)

print(counter.most_common(10))