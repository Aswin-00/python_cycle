#Write a Python program to print table

#python 3.10.12

'''
two loop exectution

'''


def table():
    for i in range(1,11):
        print(i,end=' ')
    print()
    print('-'*30)

    for i in range(1,11):
        print(i,'|',end=' ')
        for j in range(1,11):
            print(f'{i*j}' ,end=' ')
        print('\n')
