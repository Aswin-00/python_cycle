##Write a Python program that prints numbers from 1 to 100.

#python 3.10.12

'''

For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
For numbers that are multiples of both 3 and 5, print "FizzBuzz."


'''


def fizzbizz():
    for i in range(1,100):
        if i%5==0 and i%3==0:
            print('fizzbizz',end=' ')
        elif i%5==0:
            print('bizz' ,end=' ')
        elif i%3==0:
            print('fizz',end=' ')
        else:
            print(i,end=' ')
            
    

fizzbizz()
