# print 2 * table
def printLine(table, num, error=False):
    print(f"{table} * {num} = {table*num}") if error == False else print(f"\033[0;30;41m{table} * {num} = {2*num}\033[0m")

for num in range(1,13):
    try:
        if num == 4: raise Exception('incorrect multiplication')
        printLine(2, num)
    except Exception:
        printLine(3,num, True)
else: print("\U0001F606")

x = [1,2,3,4]

print([1 + i for i in x if i>2])