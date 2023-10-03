'''
Design a program that generates a seven-digit lottery number.
The program should generate seven random numbers, each in the range of 0
through 9, and assign each number to a list element.
(Random numbers were discussed in Chapter 5.)
Then write another loop that displays the contents of the list.
'''

from random import randint as gen

def main():
    number=''
    temp=0
    for i in range(7):
        temp=gen(0,10)
        print(f'{temp:2}',end=' ')
        number+=str(temp)
    return(number)


if __name__=='__main__':
    main()
