#password checker

'''
• The password must be at least seven characters long.
• It must contain at least one uppercase letter.
• It must contain at least one lowercase letter.
• It must contain at least one numeric digit.

When a student sets up his or her password, the password must be
validated to ensure it meets these requirements. You have been asked
to write the code that performs this validation. You decide to write a function named valid_password that accepts the password as an argument and returns either true or false, to indicate whether it is valid. 

'''


def main():
    password=input("Enter the password : ")

    if condition(password)==True:
        print('This password is valid')
    else:
        print('This password is invalid !')
        


def condition(pasw):
    if lenght_condition(pasw) ==True and upper_condition(pasw)==True:
        if lower_condition(pasw) ==True and number_condition(pasw) ==True:
            return True
    return False

def lenght_condition(pasw):
    if len(pasw)>=7:
        return True
    return False

def upper_condition(pasw):
    for x in pasw:
        if x.isupper()==True:
            return True
    else:
        return False
    
def lower_condition(pasw):
    for x in pasw:
        if x.islower()==True:
            return True
    else:
        return False

def number_condition(pasw):
    for x in pasw:
        if x.isnumeric()==True:
            return True
    else:
        return False
        
    

'''
def main():
    password = input("Enter the password: ")

    if valid_password(password):
        print('This password is valid')
    else:
        print('This password is invalid!')


def valid_password(pasw):
    conditions = [
        len(pasw) >= 7,
        any(c.isupper() for c in pasw),
        any(c.islower() for c in pasw),
        any(c.isnumeric() for c in pasw)
    ]
    return all(conditions)


if __name__ == "__main__":
    main()

'''



if __name__=="__main__":
    main()
