##break - brings outside the loop ,whereas pass, and continue are similar
# but there is difference explained in program below
print("for loop with 'pass'")
for i in range (5):
    if i==3:
        pass
    print(i)

 ## output is - 0, 1, 2, 3, 4
print("for loop with 'continue'")
for i in range(5):
    if i == 3:
        continue
    print(i)

## output is 0, 1, 2, 4

## continue skips the for iteration and pass does nothing but keep the for iteration.
# if you want to do nothing then use 'pass'.
# If you want to skip the current iteration then use 'continue'