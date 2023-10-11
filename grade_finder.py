#write a code to find grade of the studen

'''
Write a program that asks the user to enter five test scores. The program should display a letter grade for each score and the average test score.
Write the following functions in the program:
• calc_average. This function should accept five test scores as arguments and return the average of the scores.
• determine_grade. This function should accept a test score as an
argument and return a letter grade for the score based on the following grading scale:


'''

# used * to input all the mark of the user in to a tuple
# sum method is used to find sum 
def calc_average(mark):
    type(mark)
    return(sum(mark)/len(mark))

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
    rng=5
    mark=[]
    for i in range(rng):
        mark.append(float(input(f'Enter the grade for the test {i+1}: ')))
    print(f'Score \t  \t Letter Grade')
    print('-'*70)
    for i in range(rng):
                print(f'Mark {i+1}  \t {mark[i]:1} : {determin_grade(mark[i])}')
    print(' ')
    print(f'Average of all marks {calc_average(mark)}')
 
