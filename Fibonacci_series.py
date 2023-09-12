#programe to print a fabonacci series

#python 3.10.12

'''
a series which add pervios number together to form a new number in the series
0,1,1,2,3 .......

'''


def fab(n):
    x,y=0,1
    print(x,y,end=' ')
    for i in range(0,n):
        z=x+y
        x,y=y,z
        print(z,end=' ')

fab(8)
