def main():
    try:
        # expect hourly error 
        hour=int(input('Enter the hourly pay:- '))

        #pay_rate
        pay_rate=float(input("Enter  you hourly pay :- "))

        #out to b shown
        print(f"pay:- {hour*pay_rate}")

    #execptoin can be Value by Error 
    except ValueError as e:
        
        #display and show error 
        print(f'Error: {e}')
        main()


#stacktrace

main()
        
