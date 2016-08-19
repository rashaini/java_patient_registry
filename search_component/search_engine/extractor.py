import urllib
import urlparse
from bs4 import BeautifulSoup, SoupStrainer
from urlparse import urljoin

class Extractor:

    '''Extracts relevant information from urls:
    Takes list of urls returned by Crawler as input
    Returns two maps urlToText and urlToLinks as output
    Implementation can be improved using an abstract class for map creation
    Look more into factory design pattern for object creation'''

    urlToText = {}
    urlToLinks = {}

    def __init__(self, myList):
        self.myList = myList
        Extractor.urlToText = urlToText
        Extractor.urlToLinks = urlToLinks

    def extract_text(self):
        for url in (self.myList):
            r = urllib.urlopen(url).read()
            soup = BeautifulSoup(r, "lxml")
            for s in soup(["script", "style"]):
                s.extract()
            t = soup.get_text()
            lines = (line.strip() for line in t.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            t = ' '.join(chunk for chunk in chunks if chunk)
            urlToText[url] = t

            return Extractor.urlToText

    def extract_links(self):
        for url in (self.myList):
            r = urllib.urlopen(url).read()
            soup = BeautifulSoup(response, parse_only=SoupStrainer('a', href=True))
            links = soup.find_all('a')
            links = [l.get('href') for l in links]
            links = [unicode(l) for l in links]
            links = [l for l in links if (l.startswith("https://") or l.startswith("http://"))]
            links = set(links)
            urlToLinks[url] = [links]

            return Extractor.urlToLinks
