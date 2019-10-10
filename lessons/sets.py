def intro(dictionary):
    for ninja in set(dictionary.values()):
        print(f'there are {list(dictionary.values()).count(ninja)} {ninja} belts')

dict3 = {}
print(f'user dict3 {dict3}')
while True:
    print('enter \'done\' when you want to stop adding values')
    key = input("insert a key: ")
    if key == 'done': break
    value = input("insert its value: ")
    dict3[key] = value
intro(dict3)
