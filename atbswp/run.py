# print('hello world!')
# name = input('what is your name? ')
# print(f"hello {name}! welcome to python3. The length of your name is {len(name)}")
# age = int(input('what is your age? '))
# print('%s will be %d in a year' % (name, age + 1))
# print('its Gilbert!') if name == 'Gilbert' else print('no')
# with open('../pass.txt') as password:
# #     s1 = password.read()
# # auth = (input('enter your password: '))
# # while auth != (s1):
# #     auth = (input('password incorrect..enter a valid password: '))
# # print('authenticated')

#Guess Game

# print('Guessing Game Begins')

# secreteNum = 15

# while True:
#     try:
#         input_num = int(input('Im thinking of a num. what is the num? ') )
#         if secreteNum > input_num: print('you guess is too low')
#         elif secreteNum < input_num: print('your input is too high')
#         else: break
#     except:
#         print('input must be a number')
# print('end')
# print('Collatz function')

# def collatz(num):
#     number = num // 2 if num % 2 == 0 else (num * 3) + 1
#     print(number)
#     return number

# try: number = int(input('insert a number to collatz: '))
# except: print('please insert a number')
# while True:
#     number = collatz(number)
#     if number == 1: break
import pandas as pd
import numpy as np

li = ['1', '3', '6', '67']
li = np.array(li)
val = pd.DataFrame(li)
val = val.astype(int)
print(type(val[0][1]))