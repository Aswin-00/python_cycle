#programe to print a prime from a 0  to inputed number

#python 3.10.12

'''
if a number is divisible only by itself and 1 than only it is consideres as a prime number

1. create a function to check if the number is prime or not
2. itrate  throw a range from 1 to n+1 where n is the input from the user
3. inside the loop we will put a condition and check if the number is prime or not 



'''
#create a function to check if the give number is prime or not

##def primenumber(n):
##    for i in range(2,n):
##        if (n%i==0):
##            return False
##    return True
##
##
###user intraction section
##
###a variable to recive user input
##
#rang=int(input("enter the range :- "))

#a loop to go throw the range
##for i in range(1,rang+1):
##    if(primenumber(i)==True):
##        print(i,end='  ')
##


# case 2
'''
using two loops to check if the number in first loop is divisible by the number
in second loop
and if the number is divisible than we set a variable t as true
and if not than we will set variable t a Flase

'''

rang=int(input("enter the range :- "))

# loop a to go throw the range
for i in range(2,rang+1):
    t=True

# loop b to go throw the range 2 to i

    for j in range(2,i):
        if (i%j==0):
            t=False
            break    
    if t==True:
        print(i, end=' ')
    
    
    




