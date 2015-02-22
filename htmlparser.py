from HTMLParser import HTMLParser
from urllib import urlopen


class MyHTMLParser(HTMLParser):

    in_class = False

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value == 'reference external':
                self.in_class = True
        #print("Encountered a strat tag:", tag)

    def handle_data(self, data):
        if self.in_class:
            print data


text = urlopen('https://www.python.org/community/jobs/').read()
p = MyHTMLParser()
p.feed(text)
