'''
Write a function to convert decimal number to Roman

M=1000    CM=900    D=500    CD=400,

C=100    XC=90    L=50    XL=40,

X=10    IX=9    V=5    IV=4    I=1

For example 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I

(https://roman-numerals.info/)

'''

class translator:

    def deciToRoman(self, num):
        out_str = ''
        if self.digitExtractor(num, 3) in range(1,10):
            out_str += self.digitExtractor(num, 3)*'M'
        if self.digitExtractor(num,2) == 9:
            out_str += 'CM'
        if self.digitExtractor(num,2) in range(5,9):
            out_str += 'D'+'C'*(self.digitExtractor(num,2)-5)
        if self.digitExtractor(num,2) == 4:
            out_str += 'CD'
        if self.digitExtractor(num,2) in range(0,4):
            out_str += 'C'*self.digitExtractor(num,2)
        if self.digitExtractor(num,1) == 9:
            out_str += 'XC'
        if self.digitExtractor(num,1) in range(5,9):
            out_str += 'L'+'X'*(self.digitExtractor(num,1)-5)
        if self.digitExtractor(num,1) == 4:
            out_str += 'XL'
        if self.digitExtractor(num,1) in range(0,4):
            out_str += 'X'*self.digitExtractor(num,1)
        if self.digitExtractor(num,0) == 9:
            out_str += 'IX'
        if self.digitExtractor(num,0) in range(5,9) :
            out_str += 'V'+'I'*(self.digitExtractor(num,0)-5)
        if self.digitExtractor(num,0) == 4:
            out_str += 'IV'
        if self.digitExtractor(num,0) in range(0,4):
            out_str += 'I'*self.digitExtractor(num,0)
        return out_str

    def romanToDeci(self, s):
        total = 0
        for iter in range(1,len(s)+1):
            index = iter-1
            heading = s[index-1]
            trailing = ''
            if index+1 == len(s):
                trailing = ''
            else:
                trailing = s[index+1]


            if s[index] == 'M':
                if heading == 'C':
                    total += 900
                else:
                    total += 1000

            if s[index] == 'D':
                if heading == 'C':
                    total += 400
                elif trailing == 'M':
                    total == total
                else:
                    total += 500

            if s[index] == 'C':
                if heading == 'X':
                    total += 90
                elif trailing == 'D':
                    total == total
                else:
                    total += 100
            
            if s[index] == 'L':
                if heading == 'X':
                    total += 40
                else:
                    total += 50
            
            if s[index] == 'X':
                if heading == 'I':
                    total += 9
                elif trailing == 'L':
                    total = total
                else:
                    total += 10
            
            if s[index] == 'V':
                if heading == 'I':
                    total += 4
                else:
                    total += 5
            
            if s[index] == 'I':
                if trailing != 'V':
                    total +=1


        return total
                    

        ### Enter Your Code Here ###
        pass

    def digitExtractor(self, num, pos):
        return num // 10**pos%10

print(" *** Decimal to Roman ***")
num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))