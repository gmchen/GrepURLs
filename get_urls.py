import urllib2
import lxml.html
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup
import sys
import re
import socket

original_url = sys.argv[1]
regex = sys.argv[2]
print "Finding all URLs..."
connection = urllib2.urlopen(original_url)
dom =  lxml.html.fromstring(connection.read())

links = []

for link in dom.xpath('//a/@href'):
	links.append(link)

for i in range(len(links)):
	links[i] = urljoin(original_url, links[i])

print "Found " + str(len(links)) + " links!"

final_links = []
print "Searching links for matches..."

for i in range(len(links)):
	print str(i)
	link = links[i]
	if(not re.search("\.html$", link) and not re.search("/[^\.]*$", link, re.IGNORECASE)):
		continue
	# Try three times to get the text; after three failures, move on
	f = None
	for i in range(10):
		try:
			f = urllib2.urlopen(link, timeout = 1)
		except urllib2.URLError:
			pass
		except socket.timeout:
			pass
	if f == None:
		continue
	soup = BeautifulSoup(f)
	current_text = soup.getText()
	if(re.search(regex, current_text)):
		final_links.append(link)

for final_link in final_links:
	print final_link
