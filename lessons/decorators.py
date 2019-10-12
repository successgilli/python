# x = lambda a,b: a+b
# print(x(2,3))
def decorate(func):
    def wrapper():
        print('before func, this happens ')
        func()
        print('this happens after func ')
    return wrapper

@decorate
def func():
    print('I love my life')
func()
