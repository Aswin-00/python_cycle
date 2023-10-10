#write a code to find grade of the studen

'''
Write a program that asks the user to enter five test scores. The program should display a letter grade for each score and the average test score.
Write the following functions in the program:
• calc_average. This function should accept five test scores as arguments and return the average of the scores.
• determine_grade. This function should accept a test score as an argument and return a letter grade for the score based on the following grading scale:


'''

# used * to input all the mark of the user in to a tuple
# sum method is used to find sum 
def calc_average(*mark):
    print(type(mark))
    print(sum(mark)/len(mark))

def determin_grade(number):
    if number <=100 and number >=90:
        return ("A")
    elif number <=89 and number >=80:
        return ("B")
    elif number <=79 and number >=70:
        return ("C")
    elif number <=69 and number >=60:
        return ("D")
    else:
        return ('F')


    
if __name__=='__main__':
    mark=[]
    for i in range(5):
        mark.append(float(input(f'Enter the grade for the test {i+1}: ')))
    print(f'Score \t Letter Grade')
    print(f'-'*70)
    for i in range(5):
                print(f'mark {i+1 :2,mark[i]} : {determin_grade(mark[i])}')
 
