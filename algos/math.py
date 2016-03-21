def pow(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y == 2:
        return x * x
    elif y % 2 == 0:
        return pow(x * x, y/2)
    else:
        return pow(x * x, y/2) * x
