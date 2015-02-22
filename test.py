from urllib import urlopen
from BeautifulSoup import BeautifulSoup

text = urlopen('https://www.python.org/community/jobs/').read()
soup = BeautifulSoup(text)

jobs = set()
for link in soup('a', 'reference external'):
    print(link['href'])
