#Write a Python program to find interest rate

#python 3.10.12

'''
Write a Python program to calculate the future value of an
investment based on the principal amount, interest rate, and time period.

principal = 1000
rate_of_interest = 0.05 (5%)
time_period = 3, 

sn= pv=(1+R)**n


'''

def finalinterst():
    pr=float(input("enter the principal value :- "))
    rate=float(input("enter the rate_of_interest :- "))
    time=float(input("enter the time_period:- "))
    finalint=pr*((1+rate)**time)
    print(f'The future value of the investment is : {finalint:.3f}')
