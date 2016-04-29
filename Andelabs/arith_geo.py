def arith_geo(arr):
    i = 0
    x = []
    y = []

    while i < len(arr) - 1:
        if arr[i + 1] == 0 or arr[i] == 0:
            y.append(0)
        else:
            y.append(arr[i + 1] / float(arr[i]))
        x.append(arr[i + 1] - arr[i])
        i += 1

    y, x = set(y), set(x)

    if arr == []:
        return 0
    if len(x) == 1:
        return 'Arithmetic'
    elif len(y) == 1:
        return 'Geometric'
    else:
        return -1