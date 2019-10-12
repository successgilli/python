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
with open('text.txt') as reader:
    read = reader.readlines()
    # reader.seek(0)
print(list(filter(lambda line: '>' not in line, read)))