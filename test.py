# # # from lessons.class_test import Parent as armpit, Child

# # # p3 = armpit('success', 14)
# # # print(p3.get_info())
# # # # print(Child('henry', 90))

# # from projects.bar_calc import Tab

# # print(Tab)

# # table1 = Tab()
# # table1.add_item()
# # table1.print_items(10, 10)
# from random import shuffle
# GUEST_LIST = {
# 	"Randy": "Germany", 
# 	"Karla": "France", 
# 	"Wendy": "Japan", 
# 	"Norman": "England", 
# 	"Sam": "Argentina"
# }

# def greeting(name):
# 	if name in GUEST_LIST:
#         print('het')
#     else:
#         print(return "Hi! I'm a guest.")
# def greeting(name):
#     if name in GUEST_LIST: 
#         return "Hi! I'm %s, and I'm from %s." %(name, GUEST_LIST[name])
#     else: 
#         return 'hi!, i\'m a guest'

# X = greeting('Randy')
# print(X)

# # def fxn(*li):
# #     print(type())
# #     print(sum(li,[]))

# # fxn([1],[2,3,4],[23,4])
# # x = [1,2,3]
# # shuffle(x)
# # print(x)
# with open('text.txt') as reader:
#     print(reader.readline(5))
#     print(reader.readline(5))
#     print(reader.readline(5))
#     print(reader.readline(5))
# with open('text.txt', 'r') as reader:
#     # line = reader.readline()
#     # while line != '':
#     #     print(line, end="")
#     #     line = reader.readline()
#     line = reader.readlines()
#     for li in line:
#         print(li, end="")

# with open('text.txt', 'r') as reader:
#     content = reader.readlines()
# with open('write.txt', 'w') as writer:
#     for text in reversed(content):
#         writer.write(text)
# with open('write.txt') as reader:
#     print(reader.read())
# with open('text.txt', 'r') as reader, open('write.txt', 'w') as writer:
#     read = reader.readlines()
#     writer.writelines(read)
# with open('write.txt', 'a') as writer:
#     writer.write('armpit')
# with open('text.txt') as reader:
#     read = reader.readlines()
#     # reader.seek(0)
# print(list(filter(lambda line: '>' not in line, read)))
# with open('text.txt') as reader:
#     read = reader.readlines()
#     # reader.seek(0)
# print(list(filter(lambda line: '>' not in line, read)))
# import pprint
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': '', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ','low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# def printBoard(board):
#     print(board['top-L'], '|', board['top-M'], '|', board['top-R'])
#     print('--+--+--')
#     print(board['mid-L'], '|', board['mid-M'], '|', board['mid-R'])
#     print('--+--+--')
#     print(board['low-L'], '|', board['low-M'], '|', board['low-R'])
# turn = 'X'
# print('welcome to tictactoe')
# for i in range(9):
#     printBoard(theBoard)
#     move = input(f'time for move {turn}')
#     theBoard[move] = turn
#     turn = 'X' if (turn == 'O') else 'O'
#     printBoard(theBoard)
# import jwt
# from time import time
# payload = { 'email': 'sucsuc', 'armpit': 222}
# payload2 = { 'email': 'successawaji', 'exp': time() + 60 }
# secrete = 'my key'
# token = jwt.encode(payload, secrete, algorithm='HS256').decode('utf-8')
# token2 = jwt.encode(payload, secrete, algorithm='HS256').decode('utf-8')
# print(jwt.decode(token2, secrete, algorithms=['HS256']))
import pandas as pd
# import numpy as np
# data = { 'a': 1, 'b': 2}
# print(pd.Series([1,2,3,45], ['a','b','c','d']))
# print(pd.Series(data))
# print(pd.DataFrame(np.random.randn(2,4), columns=['a','b','c','d']))
# print(pd.DataFrame(np.random.randn(2,4), columns=['a','b','c','d']).drop(['a', 'b'], axis = 1))

# df = pd.DataFrame(np.random.randn(2,4), columns=['a','b','c','d'])
# print(df)
# print(df.loc[0:,'a'])
# postgres://{username}:password@localhost:port/{db}
# connectionDetails = dict(user = "doadmin", password = "aisubw7jsb8pquja", host = "questionbank-postgresql-do-user-3646202-0.db.ondigitalocean.com",
# port = "25060", database = "QuestionBank", sslmode='require')
from sqlalchemy import create_engine
db = create_engine('postgres://doadmin:aisubw7jsb8pquja@questionbank-postgresql-do-user-3646202-0.db.ondigitalocean.com:25060/QuestionBank')
db.connect()
while True:
    try:
        db.execute('ALTER TABLE subtopic ADD CONSTRAINT PK_subtopic PRIMARY KEY ("Sub_Topic","Topic_id");')
        print('done!')
        break
    except Exception as e:

        strList = str(e).replace(')','').split()
        val = [int(x) for x in strList if x.isdigit()]
        id = val[0]

        print(id, ' cause of conflict')
        res = db.execute(f'SELECT * from subtopic where "Topic_id"={id};').fetchall()
        print(res)
        res = [y[0] for y in res]
        print(res)
        # res1 = db.execute(f'SELECT * from subtopicquestion where "sub_topic_id"={res[0]}').fetchall()
        # res2 = db.execute(f'SELECT * from subtopicquestion where "sub_topic_id"={res[1]}').fetchall()
        # print(res1, ' res1')
        # print(res2, ' res2')
        db.execute(f'DELETE from subtopic where "Id"={res[1]}')

# res2 = db.execute(f'INSERT into subtopicquestion (question_id, sub_topic_id) VALUES (30, 100)')
# # db.execute(f'DELETE FROM subtopicquestion where "sub_topic_id"=100')
# print('DONE!')

# print(pd.read_csv('cars.csv'))
# with pd.ExcelFile('Excel_Sample.xlsx') as x:
#     s1 = x.parse('Sheet1')
# print(s1)
# print(pd.read_excel('Excel_Sample.xlsx', 'Sheet1').isnull())
