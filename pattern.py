#programe to print pattern

#python 3.10.12

'''


print a pattern of star

'''


def pattern(n):
    for i in range(0,n):
        print(((i+(i+1))*'*').center(n*4))




def pattern_hardcode(n):
    for i in range(0,n):
        print()
        print(' '*(n-i),end='')
        print("*"*(i),end='')
##        print("*"*(i-1),end='')
##    
        
pattern_hardcode(5)

patter(5)
