class Student:

    NUMBER_OF_TASKS = 37
    TEST_WEIGHTS = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]
    NUMBER_OF_TESTS = len(TEST_WEIGHTS)

    def __init__(self, name, age):
        print('Hello from Student!', id(self), self)
        self.name = name
        self.age = age
        self.phone = None
        self.birth_date = None
        self.hw_tasks = [0] * Student.NUMBER_OF_TASKS
        self.tests = [0] * Student.NUMBER_OF_TESTS

    def print_info(self):
        print('*******************************')
        print('Name:       %s' % self. name)
        print('Age:        %s' % self.age)
        print('Phone:      %s' % self.phone)
        print('Birth date: %s' % self.birth_date)
        print('Rank:       %s' % sum(self.hw_tasks))
        print('*******************************')

    def accept_task(self, num_task):
        self.hw_tasks[num_task - 1] = 1

    def accept_test(self, num_test):
        self.tests[num_test - 1] = 1


def main():
    student1 = Student('Ivan', 18)
    print(type(student1), id(student1))

    student2 = Student('Mariya', 18)
    print(type(student2), id(student2))

    #student1.name = 'Ivan Ivanov'
    #student1.age = 18
    print(student1.name, student1.age)
    student1.age += 1
    print(student1.name, student1.age)

    print(student2.name, student2.age)
    student2.name = 'Alice'
    print(student2.name, student2.age)

    student1.accept_task(1)
    student1.accept_task(3)
    student1.accept_task(5)
    student1.print_info()
    student2.print_info()


if __name__ == '__main__':
    main()

