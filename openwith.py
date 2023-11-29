
def write():
    inline=open('file.txt','w')
    # get  the numeber of dayes
    
    for i in range(int(input('Enter the number of days:- '))):
        inline.write(input(f"Enter the Amount for day{i+1} sales:- ")+'\n')
    inline.close()


def read_cal():
    total=0
    inline=open('file.txt','r')
    
    # get  the numeber of dayes
    for i in inline:
        total+=float(i)
    inline.close()
    return total
    
def main():
    write()
    print(f'Total of sales amount is= {read_cal():.2f}')    


if __name__=='__main__':
    main()
