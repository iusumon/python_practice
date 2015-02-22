import fileinput

for line in fileinput.input(inplace=True):
    line = line.rstrip()
    hash_index = line.index('#', 40)
    print(line[:hash_index])
