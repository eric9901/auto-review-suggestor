
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
#get google  result

def getUrl(search):
	results = 10 # valid options 10, 20, 30, 40, 50, and 100
	page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
	soup = BeautifulSoup(page.content, "html.parser")
	links = soup.findAll("a")
# a queue of urls to be crawled 
	new_urls = deque();
#get all http link of the searching result
	for link in links :
		link_href = link.get('href')
		if "url?q=" in link_href and not "webcache" in link_href:
			new_urls.append(link.get('href').split("?q=")[1].split("&sa=U")[0])
	return new_urls


def getEmail(new_urls):
# a set of urls that we have already crawled
	processed_urls = set()
	email=''


# process urls one by one until we exhaust the queue
	while len(new_urls):
	# move next url from the queue to the set of processed urls
		url = new_urls.popleft()
		processed_urls.add(url)
     
	# extract base url to resolve relative links
		parts = urlsplit(url)
		base_url = "{0.scheme}://{0.netloc}".format(parts)
		path = url[:url.rfind('/')+1] if '/' in parts.path else url
	# get url's content
		print("Processing %s" % url)
		try:
			response = requests.get(url)
		except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
		# ignore pages with errors
			continue
	# extract all email addresses and add them into the resulting set
		match= re.search(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""", response.text, re.I)
		if match:
			new_email = match.group(0)
			email=new_email
    #None check
			if email:
				print(email)
				new_urls.clear()
		else:
			email=''
	return email
	

  
   