a = input("Enter a number to find factorial: ")
factorial = 1

for i in range(1, int(a)+1):
    factorial *= i

print("Factorial of", a, "is", factorial)
##print( "is", factorial )
