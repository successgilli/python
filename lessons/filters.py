# def filter_grade(grade):
#     return grade != 'F'
grades = ['A','B','C','F','A','E','F']
print(list(filter(lambda grade: grade != 'F', grades)))

print([grade for grade in grades if grade != 'F'], ' list comprehension')
