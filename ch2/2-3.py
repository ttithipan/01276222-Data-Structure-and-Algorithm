def RANGE(*args):
    iterator = 0.0
    result = []
    if len(args) == 1:
        while 0 + iterator < args[0]:
            result.append(round(iterator, 3))
            iterator += 1
        return f'{tuple(result)}'
    elif len(args) == 2:
        while args[0] + iterator < args[1]:
            result.append(round(args[0] + iterator, 3))
            iterator += 1
        return f'{tuple(result)}'
    elif len(args) == 3:
        while args[0] + iterator * args[2] < args[1]:
            result.append(round(args[0] + iterator * args[2], 3))
            iterator += 1
        return f'{tuple(result)}'
    else:
        return 'Invalid number of arguments'

print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    k = RANGE(n[0])
    print(RANGE(n[0]))
elif len(n) == 2:
    print(RANGE(n[0], n[1]))
elif len(n) == 3:
    print(RANGE(n[0], n[1], n[2]))