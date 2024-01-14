student = {"name": "alpha", "id":5}
print(student["name"])
print(student["id"])


student = {"name": "alpha", "id": 5, "course": "BSC CC"}
print('Display key-value pairs')
for key, value in student.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print('\nDisplay only keys')
for key in student.keys():
    print(key)

print('\nDisplay only values')
for value in student.values():
    print(value)

student = {"name": "alpha", "id": 5}
student["course"] = "BSC CC"
print(student)

student = {'name': 'alpha', 'id': 5, 'course': 'BSC CC'}
print('Student Details before altering the value\n', student)
student['course'] = 'BA B&M'
print('\nStudent Details after altering the value\n', student)

student = {'name': 'alpha', 'id': 5, 'course': 'BSC CC'}
print('Student Details before deleting the value\n', student)
del student['course']
print('\nStudent Details after deleting the value\n', student)

student1 = {'name': 'alpha', 'id':'5', 'course': 'BSC CC'}
student2 = {'name': 'beta', 'id': '10', 'course': 'BSC CC'}
student3 = {'name': 'gamma', 'id':'15', 'course': 'BA'}
student4 = {'name': 'delta', 'id':'20', 'course': 'BA'}
student = [student1, student2, student3, student4]
for std in student:
    print(std)

student = {
    "name": "alpha",
    "marks": ["Codelab-78", "codelab2-82"],
}
print(f"The student name {student["name"]} scored the following marks:")
for mark in student["marks"]:
    print("\t" + mark)

student1 = {
'name': 'alpha',
'marks': ['Codelab1 - 78', 'codelab2 - 82'],
}
year = {
'Year': 2022
}
student1.update(year)
print(student1)

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')