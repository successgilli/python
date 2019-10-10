ninjas = ['yoshi', 'vic', 'sunday', 'gizzard']

for ninja in ninjas:
    if ninja == 'vic': continue
    elif ninja == 'sunday': 
        print(f'{ninja} is a black belt')
        break
    else: print(ninja)
else: print('loop done')
print("*"*10)
# for index in range(0, len(ninjas), 2):
#     print(ninjas[index], ' ', index)
