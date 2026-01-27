# simplest if

import random
num = random.randint(1,10)
print("Random number: ", num)
#check if number is odd
# dont need to write ==1 for odd, 1 is true so can be kept blank. if you want even number, you can write if not because if not odd then it is even
if  num%2:
    print("Number is odd")
else:
    print("Number is even")
    print("This only shows for even numbers")
print("This always shows, thanks for playing")
