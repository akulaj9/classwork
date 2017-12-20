from person import Person

class Professor(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.salary = 0

    def print_info(self):
        super().print_info()
        print('Salary:      %s' % self.salary)
        print('*******************************')
