def tree(height, sign="*"):
    sCount = 0
    for i in range(height):
        sCount += (2*i+1)
        print((height-i-1)*" " + (2*i+1)*sign)
    return sCount

sCount = tree(3)
print(sCount)