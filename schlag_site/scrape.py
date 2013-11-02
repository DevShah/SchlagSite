import urllib2
from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://carnegiemellon.esuds.net/RoomStatus/machineStatus.i?bottomLocationId=341').read())

for i in xrange(1, 11):
	if (i % 2 == 0 and i < 10):
		a = soup('tr', {'class': 'even'})[(i-1)/2]
		row = a('td')
		print row[0], row[1], row[2], row[3], row[4]
		print "---------"
	else:
		a = soup('tr', {'class': 'odd'})[(i)/2]
		row = a('td')
		print row[0], row[1], row[2], row[3], row[4]
		print "---------"
