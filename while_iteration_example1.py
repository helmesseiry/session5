#print from 1 to 100
num=1
while num<=100:
    print(num)
    num=num+1

#infinite loop with escape mechanism
num = 1
while True:
    print(num)
    num=num+1
    if num>100:
        break # This is the escape mechanism

