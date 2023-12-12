#course manageent
'''
1. `Course` class:
   - Represents a university course with the following attributes:
     - `course_code` (a unique identifier for the course)
     - `course_name` (the name of the course)
     - `credits` (the number of credit hours for the course)
   - Has the following methods:
     - `__init__(self, course_code, course_name, credits)` - constructor to initialize the course.
     - `get_course_info(self)` - returns a string describing the course.

2. `LectureCourse` class (inherits from `Course`):
   - Represents a lecture-based course and has additional attributes:
     - `instructor` (the instructor's name)
     - `meeting_time` (the time and days the class meets).
   - Overrides the `get_course_info()` method to provide a description specific to lecture courses.

3. `LabCourse` class (inherits from `Course`):
   - Represents a lab-based course and has additional attributes:
     - `lab_instructor` (the lab instructor's name)
     - `lab_schedule` (the schedule for lab sessions).
   - Overrides the `get_course_info()` method to provide a description specific to lab courses.


'''
import random as randint 

class Course:
    def __init__(self,course_code, course_name, course_credits):
        self.course_code=course_code
        self.course_name=course_name
        self.course_credits=course_credits


    def get_course_info(self):
        print(self.course_name+' is the name of the course ')
    
    def __str__(self):
        return(self.course_name)
    


class LabCourse(Course):
    def __init__(self,course_code, course_name, course_credits,lab_instructor,lab_sechedule):
        super().__init__(course_code, course_name, course_credits)

    def get_course_info(self):
        print(f'''
{self.course_name}
Credits: {self.course_credits}
Lab Instructor: {self.lab_instructor}
Lab Schedule: {self.lab_sechedule}
''')

'''
4. `Student` class:
   - Represents a student with the following attributes:
     - `student_id` (a unique identifier for the student)
     - `name` (the name of the student)
   - Has the following methods:
     - `__init__(self, student_id, name)` - constructor to initialize the student.
     - `enroll(self, course)` - allows a student to enroll in a course.
     - `get_enrolled_courses(self)` - returns a list of courses in which the student is enrolled.
     - `__str__(self)` - returns a string representation of the student.


'''


class Student:
    def __init__(self, name):
        self.student_id=radint(1111,9999)
        self.name=name
        self.course_list=[]

    def eroll(self,course):
        self.course_list.append(course)
        
    def get_enrolled_courses(self):
        print(*self.course_list sep='\n')

    def __str__(self):
        return(self.name)
    
x=Course('123332','python','6')
x.get_course_info()


        
        
        
