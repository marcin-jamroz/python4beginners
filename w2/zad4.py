def tree(height, sign):
    for i in range(height):
        print((height-i-1)*" " + (2*i+1)*sign)

for x in range(2,4):
    tree(x, sign="#")