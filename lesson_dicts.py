import pprint
# initialization
dict_en_es = {'world': 'mundo',
              'language': 'idioma',
              'See you later': 'Hasta la vista'}

print(dict_en_es)
print(type(dict_en_es))

print(dict_en_es['world'])
dict_en_es['hi'] = 'hola'
pprint.pprint(dict_en_es)
print(dict_en_es['hi'])

capitals = {'UA':'Kyiv',
            'France': 'Paris',
            'Great Britan': 'London'}
capitals['USA'] = 'Washington'
capitals ['Italia'] = 'Roma'
print(capitals)

streets = {}
streets['Odessa'] = ['Deribasovskaya', 'Dolgaya', 'Kanatnaya']
streets['Kyiv'] = ['Khreschyatyk', 'Lenina', 'Volodymirska']
pprint.pprint(streets)

companies = {}
companies['Apple'] = ['Iphone', 'Macbook', 'Ipod']
companies['Samsung'] = ['Telephone', 'TV', 'PC']
companies['Nike'] = ['Boost', 'Sequence', 'FreeRun', 'Pegasus 33']

pprint.pprint(companies)
companies['Nike'].append('Pegasus 34')
pprint.pprint(companies)

companies['Nike'].remove('Pegasus 34')
pprint.pprint(companies)

del companies['Nike']
pprint.pprint(companies)

if 'Nike' in companies:
    print('Found and Deleted!')
    del companies ['Nike']
else:
    print('Not found!')

print("*********")
for world_en in dict_en_es.keys():
    print("%-15s -> %s" % (world_en, dict_en_es[world_en]))

for world_en in dict_en_es:
    print("%-15s -> %s" % (world_en, dict_en_es[world_en]))

for world_en in dict_en_es.values():
    print("%s" % (world_en))

for k, v in dict_en_es.items():
    print("%-15s -> %s" % (k, v))


# real examples-2
person_1 = {'name':'Richard Feynman',
            'age': 99,
            'birth_place': 'USA',
            'birth_date': "1918-01-01",
            'awards':['Nobel Prize in Phisics', 'USA Science Medal']}

person_2 = {'name':'Albert Einstein',
            'age': 138,
            'birth_place': 'Germany',
            'birth_date': "1879-03-14",
            'awards':['Nobel Prize in Physics', 'Planck Medal']}

person_3 = {'name':'Nicola Tesla',
            'age': 161,
            'birth_place': 'Croatia',
            'birth_date': "1856-07-10",
            'awards':['Edison Medal']}

physicits = [person_1, person_2, person_3]
pprint.pprint(physicits)

# add new key-value pairs
person_1['hobby'] = "painting"
person_2['hobby'] = "violin"
person_3['hobby'] = "pigeons"
person_3['hobby'] = "electricity" # second assignment overrides the 1st one
pprint.pprint(physicits)

# get with default
employee_1 = {"name":"Alex", "salary": 10000, "dep": "Sales", "bonus":200}
employee_2 = {"name":"Nick", "salary": 20000, "dep": "Sales"}
employee_3 = {"name":"Sue",  "salary": 50000, "dep": "IT", "bonus":500}
employee_4 = {"name":"Phil", "salary": 5000,  "dep": "BoardOfDirectors", "bonus":10000}

employees = [employee_1, employee_2, employee_3, employee_4]

for i in range(len(employees)):
#    current_salary = employees[i]['salary']
#    new_salary = current_salary * 2
#    employees[i]['salary] = new_salary
    employees[i]['salary'] *= 2

pprint.pprint(employees)

for i in range(len(employees)):
    if 'bonus' in employees[i]:
        employees[i]['bonus'] *=2
    else:
        employees[i]['bonus'] = 1000

pprint.pprint(employees)
employees.sort(key=lambda elem: elem['name'])
pprint.pprint(employees)

employees.sort(key=lambda elem: elem ['bonus'], reverse=True)
pprint.pprint(employees)
unicodes = {i:chr(i) for i in range(10000)}
pprint.pprint(unicodes)
