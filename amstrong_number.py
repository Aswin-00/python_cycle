#Write a Python program to find and print all
#Armstrong numbers in the range of 1 to 1000.



#what is a armstrong number a
'''
eg:-
407 has a 3 number in it

sum of 4 power 3 + 0 power 3 + 7 power 3 =407
 those number which statisfis this conditions are called amstrong numbers

'''


def powerfind(num):
    i=0
    while(int(num/10**(i))!=0):
        i+=1
    return(i)



def amstrong(number,power):
    n=power-1
    temp=number
    sumup=0
    while (n!=-1):
       y=temp//(10**n)
##       print(y,n)
       temp=temp%(10**n)
##       print(temp)
       n-=1
       sumup+=y**(power)
##       print(sumup,'sum')
    if(sumup==number):
        return True
    else:
        return False


for i in range(1,1001):
    if amstrong(i,powerfind(i))==True:
        print(i,end=' ')


