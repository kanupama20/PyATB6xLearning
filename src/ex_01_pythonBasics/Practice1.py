a = int(input("Enter a number to find factorial: "))
factorial = 1

if a<= 0:
    print("Factorial of", a, "is", factorial)
else:
    for i in range(1, a+1):
        factorial *= i
    print("Factorial of", a, "is", factorial)

