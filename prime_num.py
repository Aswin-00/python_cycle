#write a programe
'''
Write a Boolean function named is_prime
which takes an integer as an argument and returns true if
the argument is a prime number, or false otherwise. Use
the function in a program that prompts the user to enter a number then
displays a message indicating whether the number is prime.

'''


def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True



def main():
    number=int(input("Enter a number you want to check :- "))

    if (is_prime(number)==True):
        print(f'The number {number} is prime Number')
    else:
        print(f"The number {number} is Not  prime Number")


if __name__=='__main__':
    main()    
    
