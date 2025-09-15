def staircase(n, i=1):
    if n == 0:
        return "Not Draw!"
    elif n > 0:
        if i > n:
            return ""
        line = "_" * (n - i) + "#" * i
        rest = staircase(n, i + 1)
        return line + "\n" + rest if rest else line
    else:  # n < 0
        m = abs(n)
        if i > m:
            return ""
        line = "_" * (i - 1) + "#" * (m - i + 1)
        rest = staircase(n, i + 1)
        return line + "\n" + rest if rest else line


print(" *** Stair case ***")
print(staircase(int(input("Enter Input : "))))
print("===== End of program =====")
