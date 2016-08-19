import urllib
import urlparse
from bs4 import BeautifulSoup, SoupStrainer

class Crawler:

    '''Instatiates a spider:
    Takes a seed url and domain name as input
    Returns a list of all urls in domain as output
    Visiting algorithm can be improved using tree and DFS or BFS'''

    visitedUrls = []
    toVisitUrls = []

    def __init__(self, url, domain):
        self.url = url
        self.domain = domain
        Crawler.visitedUrls = visitedUrls
        Crawler.toVisitUrls = toVisitUrls

    def visit(self, url):
        # read url
        response = urllib.urlopen(url).read()
        # add it to visited links
        Crawler.visitedUrls.append(url)
        #  extract all links
        soup = BeautifulSoup(response, parse_only=SoupStrainer('a', href=True))
        links = soup.find_all('a')
        links = [l.get('href') for l in links]
        links = [unicode(l) for l in links]
        links = [l for l in links if (l.startswith("https://") or l.startswith("http://"))]
        links = set(links)
        # add them to list to be visited
        for l in links:
            if l not in Crawler.visitedUrls:
                Crawler.toVisitUrls.append(l)
        # recursively call visit function on each link in list to be visited
        for url in toVisitUrls:
            self.visit(url)

        return Crawler.visitedUrls
