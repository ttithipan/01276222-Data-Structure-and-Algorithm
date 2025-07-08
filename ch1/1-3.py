print(" *** Summation of each digit ***")
input_number = input("Enter a positive number : ")
sum_of_digits = sum(int(digits) for digits in input_number)
print(f"Summation of each digit =  {sum_of_digits}")
