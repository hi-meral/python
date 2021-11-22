class Employee(object):
    
    def __init__(self,firstname,lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
        
        
    def fullname(self):
        return f'{self.firstname.title()} {self.lastname.title()}'

    def email(self):
        return f'{self.firstname.lower()}.{self.lastname.lower()}@gmail.com'



class Developer(Employee):

    def __init__(self, firstname, lastname, language) -> None:
        super().__init__(firstname, lastname)

emp = Employee("Meral","Maradia")

print(emp.email())
print(emp.fullname())