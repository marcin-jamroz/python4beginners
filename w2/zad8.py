def tree(height, sign="*"):
    
    """
    Ta funkcja przyjmuje fajne argumenty
    """
    sCount = 0
    for i in range(height):
        sCount += (2*i+1)
        print((height-i-1)*" " + (2*i+1)*sign)
    return sCount

mtree = tree
mtree.a = 1

sCount = mtree(3)
print(mtree.a)
print(mtree.__doc__)