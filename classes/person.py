class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = 0
        self.birth_date = None

    def print_info(self):
        print('*******************************')
        print('ID:         %s' % self.id)
        print('Name:       %s' % self.name)
        print('Age:        %s' % self.age)
        print('Birth date: %s' % self.birth_date)
