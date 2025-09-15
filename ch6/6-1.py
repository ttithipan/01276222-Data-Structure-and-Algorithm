total = 0
out_str = ''
def natural_sum(n):
    global total
    global out_str
    if n == 0:
        return 0
    else:
        natural_sum(n-1)
        total += n
        out_str += f'{n} + '
    return f"{out_str[:-3]} = {total}"


print(" *** Natural sum ***")
num = int(input("Enter number : ")) 
print(f"{natural_sum(num)}")
print("===== End of program =====")
