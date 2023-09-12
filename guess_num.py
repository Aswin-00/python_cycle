#programe guess the number programme

#python 3.10.12

'''


'''

import random as rd

def main():
    print('''I've selected a random tow-digit number between 1 to 99.\n can you  guess what it is ?''')
    
    gnum=rd.randint(10,100)
    while True:

        ans=int(input("enter the number:- "))
        if ans==gnum:
            print(f"congrates ! you guessed it :{gnum}")
            break
        elif gnum<ans:
            print("To high")
        else:
            print("To low")
main()        
    



