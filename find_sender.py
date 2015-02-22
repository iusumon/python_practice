import fileinput
import re
pat = re.compile('From: (.*?) <.*>$')
for line in fileinput.input('test_mail.eml'):
    m = pat.match(line)
    if m:
        print(m.group(1))
