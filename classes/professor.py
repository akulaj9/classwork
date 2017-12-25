from person import Person

class Professor(Person):

    MAX_SALARY_LIMIT = 10000

    def __init__(self, name, age):
        super().__init__(name, age)
        self._salary = 0

    def print_info(self):
        super().print_info()
        print('Salary:      %s' % self._salary)
        print('*******************************')

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if 0 < salary <= self.MAX_SALARY_LIMIT:
            self._salary = salary
        else:
            raise ValueError('Salary is out of allowed range!')

    def __str__(self):
        return '%s: name: %s, age: %d' % (self.__class__.__name__,
                                          self.name,
                                          self.age)