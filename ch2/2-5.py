class funString():

    def __init__(self, string=""):
        self.s = string

    def __str__(self):
        return self.s

    def size(self):
        return len(self.s)

    def changeSize(self):
        result = ""
        for ch in self.s:
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            elif 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch
        return result

    def reverse(self):
        result = ""
        for i in range(len(self.s) - 1, -1, -1):
            result += self.s[i]
        return result

    def deleteSame(self):
        seen = set()
        result = ""
        for ch in self.s:
            if ch not in seen:
                result += ch
                seen.add(ch)
        return result


str1, str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)

if str2 == "1":
    print(res.size())
elif str2 == "2":
    print(res.changeSize())
elif str2 == "3":
    print(res.reverse())
elif str2 == "4":
    print(res.deleteSame())
