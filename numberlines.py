#Adding Line Numbers to a python script

import fileinput

for line in fileinput.input(inplace=False):
    line = line.rstrip()
    num = fileinput.lineno()
    print('%-40s # %2i' % (line, num))
