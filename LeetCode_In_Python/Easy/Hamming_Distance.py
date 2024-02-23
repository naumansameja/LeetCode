def hammingbird(x,y):
    different = 0
    while x > 0 or y > 0:
        x , cf1 = x>>1, x&1
        y, cf2 = y>>1, y&1
        if cf1 != cf2:
            different += 1
    return different 


x = 1
y = 4
print(hammingbird(x,y))