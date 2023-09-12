#Write a Python program to solve a quadratic equation 

#python 3.10.12

'''
For example, if the user enters a = 1, b = -3, and c = 2, the output will be:

0=b**2-4ac

b+(c)


'''


def quad():
    print("ax**2 +bx +c ")
    a=int(input("enter value of a :- "))
    b=int(input("enter value of b :- "))
    c=int(input("enter value of c :- "))
    delt=(b**2)-(4*a*c)
    if delt>0:
        root1=(-b +(delt**0.5))/2*a
        root2=(-b -(delt**0.5))/2*a
        print(f'have two roots and they are  root1={root1},root2={root2} ')
    if delt==0:
        root=-b/2*a
        print(f'have single root root= {root}')
        
    else:
        print("no roots")

quad()
