def gcd(a, b):
    if a == 0 and b == 0:
        return "Error! must be not all zero."
    if b == 0:
        return abs(a)
    return gcd(b, a % b)
try:
    x, y = map(int, input("Enter Input : ").split())
    result = gcd(x, y)
    if isinstance(result, str):
        print(result)
    else:
        print("The gcd of {} and {} is : {}".format(max(x, y), min(x, y), result))
except:
    print("Invalid input.")
