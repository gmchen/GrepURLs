import urllib2
import lxml.html
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup
import sys
import re

original_url = sys.argv[1]
print "Finding all URLs..."
connection = urllib2.urlopen(original_url)
dom =  lxml.html.fromstring(connection.read())

links = []

for link in dom.xpath('//a/@href'):
	links.append(link)

for i in range(len(links)):
	links[i] = urljoin(original_url, links[i])

links <- list(set(links))

for link in links:
	print link
