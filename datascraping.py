import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time


ob = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ob)) 

opener.addheaders = [('User-agent','Mozilla/5.0')]


def main():
    try:
	page = "https://www.huffingtonpost.com/section/taste/feed"
	sourcecode = opener.open(page).read() #full sc 
	#print sourcecode
	try:
	    titles = re.findall(r'<title>(.*?)</title> ',sourcecode)
	     links = re.findall(r'<link>(.*?)</link>',sourcecode)
	    #for title in titles:
	    #	print title
	    for link in links:
	    	print 'Visiting',link
		linksource = opener.open(link).read()
		#print linksource
	      content = re.findall(r'<div>(.*?)</div>',linksource)
		for theContent in content:
			print theContent
			time.sleep(55)
	except Exception, e:
		print str(e)
	
     except Exception, e:
     	print str(e)
main()
