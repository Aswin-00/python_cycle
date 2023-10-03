#Write a Python program to print table

#python 3.10.12

'''
two loop exectution

'''


def table():
    print(" ",end=' ')
    for i in range(1,11):
        print((f'{i:4}'),end=' ')
    print()
    print('-'*70)

    for i in range(1,11):
        print((f'{i}|').rjust(4),end=' ')
        for j in range(1,11):
            print((f'{i*j:4}') ,end=' ')
        print('\n')


table()
