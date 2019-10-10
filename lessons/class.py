# class first_class:
#     age = 10
#     name = 'gilbert'
# p1 = first_class()
# print(p1.name)

# class meth:
#     def __init__(self, name='gilbert', age=25):
#         self.name = name
#         self.age = age
    
#     def get_name(self):
#         print(f'hello {self.name} your age is {self.age}')

# p1 = meth('henry', 30)
# print(p1.get_name())
# p1.age = 50
# print(print(p1.get_name()))
# class meth2(meth):
#     pass
# p2 = meth2('ben', 59)

# print(p2.get_name())

class Parent:
    def __init__(self, name = 'dafaultName', age = 'none supplied'):
        self.name = name
        self.age = age
    
    def get_info(self):
        print(f'my name is {self.name} with age {self.age}')

p1 = Parent('Gilbert', 4090)
print(p1.name)
print(p1.get_info())

class Child(Parent):
    def __init__(self, name = 'none supplied', age = 'second noe availabele', birth_day = 'none supplied'):
        super().__init__(name, age)
        self.birth_day = birth_day
    def get_info(self):
        print('nothing for you')
p2 = Child('Angel', birth_day = '2nd of june')
print(p2.birth_day)