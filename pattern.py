#programe to print pattern

#python 3.10.12

'''


print a pattern of star

'''


def pattern(n):
    for i in range(0,n):
        print(((i+(i+1))*'*').center(n*4))
i=0
while True:
    pattern(i)
    i+=1
    


