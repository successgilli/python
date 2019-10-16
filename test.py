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
# def progress_days(runs):
# 	li = []
# 	for index in range(len(runs)):
# 		if runs[index + 1]:
# 			if runs[index + 1] > runs[index]: print('yes')
# progress_days([1,4,2,5])
def progress_days(runs):
	li = []
	for index in range(len(runs) -1, 0, -1):
		if runs[index] > runs[index - 1]:
			li.append(runs[index])
	print(len(li))
progress_days([1,2,42,43,4])
def cast_out_nines(a, b, r):
	digital_roots = []
	def cacl_dr(given):
		dr1 = given
		while dr1 >= 10:
			print('yes')
			if dr1 < 10: break
			dr1 = sum([int(val) for val in list(str(dr1))])
			print(dr1)
		print(dr1, ' dr1')
		digital_roots.append(dr1)
	for given in [a, b, r]:
		cacl_dr(given)
	cacl_dr(a*b)
	print(digital_roots)
	return 'correct!' if digital_roots[2] == digital_roots[3] else 'wrong'

			
		
print(cast_out_nines(9, 9, 81))
	
li = [
	[1,2,43],
	[2,4,5]
]
x = 3 + \
	4
print(5//2)