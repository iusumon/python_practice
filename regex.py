import re
import fileinput


field_pat = re.compile(r'\[(.+?)\]')
scope = {}


def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        exec code in scope
        return ""


lines = []

for line in fileinput.input('template.txt'):
    lines.append(line)

text = ''.join(lines)

print(field_pat.sub(replacement, text))
