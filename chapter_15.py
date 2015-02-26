#from urllib import urlopen
#import re
#
#p = re.compile('<a class="reference external" href="http(.*?)">(.*?)</a>')
#text = urlopen('https://www.python.org/community/jobs/').read()
#for url, name in p.findall(text):
#    print('%s %s' % (name, url))

#from subprocess import Popen, PIPE
#
#text = open('messy.html').read()
#tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
#
#tidy.stdin.write(text)
#tidy.stdin.close()
#
#print(tidy.stdout.read())

#from urllib import urlopen
#from HTMLParser import HTMLParser
#
#
#class Scraper(HTMLParser):
#
#    in_cls_external = False
#    in_link = False
#
#    def handle_starttag(self, tag, attrs):
#        attrs = dict(attrs)
#
#        if tag == 'a' and 'href' in attrs and 'class' in attrs:
#            if attrs['class'] == 'reference external':
#                self.in_cls_external = True
#                self.in_link = True
#                self.chunks = []
#                self.url = attrs['href']
#                #print(self.url)
#
#    def handle_data(self, data):
#        if self.in_link:
#            self.chunks.append(data)
#
#    def handle_endtag(self, tag):
#        if tag == 'a':
#            if self.in_cls_external and self.in_link:
#                print('%s %s' % (''.join(self.chunks), self.url))
#            self.in_link = False
#
#
#text = urlopen('https://www.python.org/community/jobs/').read()
#parser = Scraper()
#parser.feed(text)
#parser.close()

#from urllib import urlopen
#from BeautifulSoup import BeautifulSoup
#
#text = urlopen('https://www.python.org/community/jobs/').read()
#soup = BeautifulSoup(text)
#
#
#def f(s):
#    return s.lower()
#
#
#jobs = set()
#for header in soup('h1'):
#    links = header('a', 'reference external')
#    if not links:
#        continue
#    link = links[0]
#    jobs.add('%s %s' % (link.string, link['href']))
#
##print('\n'.join(sorted(jobs, key=f)))
#print('\n'.join(sorted(jobs, key=lambda s: s.lower())))
