from BeautifulSoup import BeautifulStoneSoup
from urllib import urlopen
from textwrap import wrap


# URL = 'http://www.bbc.com/news/feeds/rss2'
URL = 'http://feeds.bbci.co.uk/news/rss.xml?edition=asia'

soup = BeautifulStoneSoup(urlopen(URL).read())


for item in soup('item'):
    print item.title.string
    print '-'*len(item.title.string)
    print '\n' .join(wrap(item.description.string))
    print '{%s}\n' % item.link.string
