def tree(height):
    for i in range(height):
        print((height-i-1)*" " + (2*i+1)*"*")

for x in range(2,4):
    tree(x)

