from student import Student
from professor import Professor
from pprint import pprint as pp


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
    student2.accept_test(12)
    student2.print_info()

    # print(type(Student))
    #
    # pp(student1.__dict__)
    # student1.__dict__['name'] = 'IVAN'
    # print(student1.name)
    #
    # pp(Student.__dict__)

    prof1 = Professor('Dr. Who', 42)
    prof1.print_info()



if __name__ == '__main__':
    main()

