class Employee:
    # Implement the Employee class with the necessary attributes and methods.
    '''' 
   - Represents a generic employee with the following attributes:
     - `employee_id` (a unique identifier for the employee)
     - `name` (the name of the employee)
     - `hourly_rate` (the hourly rate of the employee)
   - Has the following methods:
     - `__init__(self, employee_id, name, hourly_rate)` - constructor to initialize the employee.
     - `calculate_pay(self, hours_worked)` - calculates and returns the pay for the employee based on the given hours worked.
    '''

    def __init__(self, employee_id, name, hourly_rate):
        self.employee_id=employee_id
        self.name=name                  # (the name of the employee)
        self.hourly_rate=hourly_rate    # (the hourly rate of the employee)
        self.payroll=0
    def calculate_pay(self, hours_worked):
        pass
        

    

class FullTimeEmployee(Employee):


        def calulate_pay(self,hours_worked):
            self.payroll=hours_worked*self.hourly_rate
            return self.payroll

        def __str__(self):
            x=f'''
Employee ID: {self.employee_id}
Name: {self.name}
Hourly Rate: ${self.hourly_rate}
Payroll: ${self.payroll}
'''
            return x
            

    
class PartTimeEmployee(Employee):
    
    def __init__(self,employee_id, name, hourly_rate):
            super().__init__(employee_id, name, hourly_rate)

    def calulate_pay(self,hours_worked):
        
        self.payroll=hours_worked*self.hourly_rate
        return self.payroll

    def __str__(self):
        x=f'''
Employee ID: {self.employee_id}
Name: {self.name}
Hourly Rate: ${self.hourly_rate}
Payroll: ${self.payroll}
'''
        return x
        
def add_employee(employee_dict, employee_id, employee):
    employee_dict[employee_id]=employee
    

def get_employee_details(employee_dict, employee_id):
    print(employee_dict[employee_id])
    
def calculate_total_payroll(employee_dict):
        total_payroll=0
        for i in employee_dict:
            total_payroll+=employee_dict[i].payroll

        return total_payroll

    
