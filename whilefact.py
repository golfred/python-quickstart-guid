#whilefact.py
n = int(input('Enter an inter >=0: '))
fact = 1
i =2
while (i <= n):
    fact = fact * i
    i = i +1
print(str(n)+ ' factoral is '+str(fact))
