# token
'''
The process of breaking a string into tokens is known as
tokenizing a string. In Python, you use the split method to tokenize strings.
# Strings to tokenize
str1 = 'one two three four'
str2 = '10:20:30:40:50'
str3 = 'a/b/c/d/e/f'




'''


def main():
    str1 = 'one two three four'

    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'

    str1=str(str1).split(' ')
    for i in str1 :print(f'token:{i}')
    print( )
    str1=str(str2).split(':')
    for i in str1 :print(f'token:{i}')

    print( )

    str1=str(str3).split('/')
    for i in str1 :print(f'token:{i}')

    
if __name__=='__main__':
    main()
