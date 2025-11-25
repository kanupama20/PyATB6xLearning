## 1 to 100 no, for no divisible eby 3 print 'fizz', for no divisible by 5 print 'buzz'
# for no divisible by both 3 and 5 print ' fizzbuzz'

for i in range (1, 101):

    if i%3==0 and i%5==0:
        print(str(i) + "\tFizzBuzz")

    elif i%3==0:
        print(str(i) + "\tFizz")

    elif i%5==0:
        print(str(i) + "\tBuzz")

    else: print(i)