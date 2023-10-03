#write 
'''
Design a program that asks the user to enter a series of 6 numbers. The program should store the numbers in a list then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list

'''
def main():
    # list to enter series of 6 number
    lst=[]
    for i in range(0,6):
        lst.append(int(input(f"Enter numeber {i+1}: ")))

    # using list build in function min,max,sum
    print(f'lowest number :- {min(lst)}')
    print(f'Highest  number :- {max(lst)}')
    print(f'Total of the numbers :- {sum(lst)}')
    print(f'Average of the numbers  :- {sum(lst)/len(lst):.3f}')
    
if __name__=='__main__':
    main()
