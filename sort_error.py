if __name__ == '__main__':
    records=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    outlist=[]
##    for _ in range(int(input())):
##        name = input()
##        score = float(input())
##        records.append([name,score])

        
    print(records)
    records.sort()
    print(records)
    for i in range(1,3):
        outlist.append(records[i][0])
    outlist.sort()
    
    print(*outlist,sep='\n')
    
    
            
    
