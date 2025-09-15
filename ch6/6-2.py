def length(txt):
    def recurse(s, i=0, decorated=''):
        if s == '':
            print(decorated, end= '')
            print(f"\nlength of '{txt}' is {i}",end = '')
        else:
            recurse(
            s[1:],
            i + 1,
            decorated + s[0] + ('*' if i % 2 == 0 else '~')
        )
    recurse(txt)
    return ''

print(" *** Length of string (Recursion) ***",end = '')
print("\n",length(input("\nEnter Input : ")),sep="")
