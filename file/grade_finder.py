with open('context.txt','r') as f:
    line=f.readlines(1)
    for i in line:
        l=list(i.split(' ') )
    l.remove('\n')
    l=[int(i) for i in l]

    print(l)
    print(sum(l))
    print(sum(l)/len(l))
    
##with open('context.txt','a') as f:
##    x='aswin hello word'
##    
##    for i in x.split(' '):
##        f.write(i+'\n')
##
    
    

