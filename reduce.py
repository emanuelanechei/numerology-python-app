def get_input(var):
    print("Enter " + var)
    x = input()
    return x

def numerologize(num, masters):
    if masters is not False:
        masters = [11,22,33]

    lis = list(str(num))
    y = 0

    for l in lis:
        y += int(l)

    if y < 10 or masters.__contains__(y):
        return y
    else:
        return numerologize(str(y), masters)