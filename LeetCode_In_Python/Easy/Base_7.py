def base7(num):
    if num == 0:
        return str(0)
    new = abs(num)
    representation = ''
    while new:
        representation = str(new%7) + representation 
        new //= 7
    if num < 0:
        return '-' + representation
    return representation

print(base7(-7))
    
