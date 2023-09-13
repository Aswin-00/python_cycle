#programe to print a prime from a 0  to inputed number

#python 3.10.12

'''
using two loops to check if the number in first loop is divisible by the number
in second loop
and if the number is divisible than we set a variable t as true
and if not than we will set variable t a Flase

'''

rang=int(input("enter the range :- "))

# loop a to go throw the range
for i in range(2,rang+1):
    
# loop b to go throw the range 2 to i

    for j in range(2,i):
        if (i%j==0):
            break    
    else:
        print(i, end=' ')
    
    
    




