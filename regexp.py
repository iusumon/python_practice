import re
text = "This is my, text for iusumon@gmail.com regexp Search iu_sumon@yahoo.com operations."

#m = re.findall('<.*?>', '<H1>Title</H1>')
#m = re.findall('.*', text)
#m = re.findall('.+', text)
#m = re.findall('.?', text)
#m = re.findall('a{6}', 'aaaaa')
#m = re.findall('a{3,6}', 'aaaa')
#m = re.findall('a{3,6}', 'aaaa')
#m = re.findall('a{3,6}?', 'aaaaaa')
#m = re.findall(r'([\w\.\_]+?@.[\w\.\_]+)', text)
#m = re.findall('a{3,6}?', 'aaaaaa')
m = re.findall('[\w]+', text)
#m = re.split('\W+', text)
#print(''.join(m))
print(m)
