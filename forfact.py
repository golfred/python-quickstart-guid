# forfact.py
n = int(input('Enter an inter >=0: '))
fact = 1
for i in range(2,n+1):
    fact = fact * i
print(str(n)+ ' factoral is '+str(fact))
