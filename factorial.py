#programe to print factorial of number

#python 3.10.12

'''
factorial 5=120


'''


def factorial(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return(x)

print(factorial(5))
print(factorial(2))
print(factorial(6))
