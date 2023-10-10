#rain fall
'''
Design a program that lets the user enter the total
rainfall for each of 12 months into a list.
The program should calculate and display the total
rainfall for the year, the average monthly rainfall,
the months with the highest and lowest amounts.
Sample Output

'''


def rainfall():
    rain=[]
    
    for i in range(12):
        rain.append(float(input(f"Enter rainfall for month {i+1}: ")))

    print(f'Total Rainfall for the year : {sum(rain)} inches')
    print(f'Average monthly Rainfall : {sum(rain)/len(rain)} inches')
    print(f'Month with the Higest rainfall month {rain.index(max(rain))+1} ({max(rain)}) inches')
    print(f'Month with the Higest rainfall month {rain.index(min(rain))+1} ({max(rain)}) inches')
    

if __name__=='__main__':
    rainfall()
