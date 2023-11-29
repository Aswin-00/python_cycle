def main():


    try:
        file =open('f.txt','r')
        for i in file:
            print(i)
        file.close()

    except Exception  as e:
        print(f'Eroor:{e}')
        
        
    
