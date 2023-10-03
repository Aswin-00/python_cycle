#write a programe to calculate monthly payment amount
'''
Suppose you have taken out a loan for a certain amount of money with
a fixed monthly interest rate and monthly payments, and you want to
determine the monthly payment amount necessary to pay off
the loan within a specific number of months. The formula is as follows:
P=(R*A)/(1-((1+R)*-M))

The terms in the formula are:
• P is the payment amount per month.
• R is the monthly interest rate, as a decimal (e.g., 2.5% 5 0.025).
• A is the amount of the loan.
• M is the number of months.
Write a program that prompts the user to enter the monthly
interest rate as a percentage, the loan amount, and the desired number of months. The program should pass
these values to a function that returns the monthly payment amount necessary.
The program should display the loan amount, interest rate, payment months, and monthly payment amount.
'''


Annual_amount=0
Months=0
Rate=0


def equation(Rate,Annual_amount,Months):
    up=Rate*Annual_amount
    down=1-(1+Rate)**(-Months)
    return up/down

def user_input():
    Aamoutt=int(input("Enter the loan amount :-$"))
    rate=float(input("Enter the annual interset rate % :-"))
    Months= int(input("Enter the number of months : "))
    print(equation())

def main():
    user_input()
    print('Loan Details: ')
main()
