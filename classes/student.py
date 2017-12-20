from person import Person

class Student(Person):

    NUMBER_OF_TASKS = 37
    TEST_WEIGHTS = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]
    NUMBER_OF_TESTS = len(TEST_WEIGHTS)

    def __init__(self, name, age):
        print('Hello from Student!', id(self), self)
        super().__init__(name, age)
        self.phone = None
        self.hw_tasks = [0] * Student.NUMBER_OF_TASKS
        self.tests = [0] * Student.NUMBER_OF_TESTS

    def print_info(self):
        super().print_info()
        print('Phone:      %s' % self.phone)
        print('Rank:       %s' % self.total_rank())
        print('*******************************')

    def accept_task(self, num_task):
        self.hw_tasks[num_task - 1] = 1

    def accept_test(self, num_test):
        self.tests[num_test - 1] = 1

    def total_rank(self):
        result = sum(self.hw_tasks)
        for i in range(self. NUMBER_OF_TESTS):
            result +=(self.tests[i] * self.TEST_WEIGHTS[i])


        return result