import feedparser
import requests 
import pymongo
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient()
db = client.news_articles





def parse_des(link_address):
	connect_timeout=1
	try:
		con = requests.get(link_address)
		con_content = con.content
		file=open('temp.txt','w')
		file.write(con_content)
		file.close
		soup=BeautifulSoup(open("temp.txt"),"lxml")
		for tag in soup.find_all('p'):
			if(tag.name=="a" and tag.name=="script" and tag.name=="li" and tag.name=="ul" and tag.name=="div" and tag.name=="link" and tag.name=="span"):
				tag.replaceWith('')
		for script in soup(["script", "style","a","li","span"]):
			script.extract()    # rip it out
		text = soup.get_text()
		return text;
	except:
		a=" "
		return a;



a = feedparser.parse(r'/home/crazyglasses/Documents/almabase/git/xml/cnn.xml')
b = feedparser.parse(r'/home/crazyglasses/Documents/almabase/git/xml/et.xml')
c = feedparser.parse(r'/home/crazyglasses/Documents/almabase/git/xml/ycomb.xml')
d = feedparser.parse(r'/home/crazyglasses/Documents/almabase/git/xml/ys.xml')
l1 = len(a['entries'])
for post in range(0,l1):
	cnn = db.cnn
	if(a.entries[post].has_key('title')):
		title = a.entries[post].title 
	else: 
		title=" "	
	if(a.entries[post].has_key('link')):
		link = a.entries[post].link
	else:
		link=""	
	if(a.entries[post].has_key('published')):
		pub_date  = a.entries[post].published
	else:
		pub_date=""	
	if(a.entries[post].has_key('link')):	
		description = parse_des(link)
	else:
		description=" Not available"
	post = {"title":title,
	         "url":"cnn.com",
            "link":link,
            "Date":pub_date,
            "content":description
            }

	post_id = cnn.insert(post)
	print post_id



l2 = len(b['entries'])
for post in range(0,l2):
	et = db.et
	if(b.entries[post].has_key('title')):
		title = b.entries[post].title 
	else: 
		title=" "	
	if(b.entries[post].has_key('link')):
		link = b.entries[post].link
	else:
		link=""	
	if(b.entries[post].has_key('published')):
		pub_date  = b.entries[post].published
	else:
		pub_date=""	
	if(b.entries[post].has_key('link')):	
		description = parse_des(link)
	else:
		description=" Not available"
	post = {"title":title,
	         "url":"economictimes.com",
            "link":link,
            "Date":pub_date,
            "content":description
            }

	post_id = et.insert(post)
	print post_id



l3 = len(c['entries'])
for post in range(0,l3):
	ycomb = db.ycomb
	if(c.entries[post].has_key('title')):
		title = c.entries[post].title 
	else: 
		title=" "	
	if(c.entries[post].has_key('link')):
		link = c.entries[post].link
	else:
		link=""	
	if(c.entries[post].has_key('published')):
		pub_date  = c.entries[post].published
	else:
		pub_date=""	
	if(c.entries[post].has_key('link')):	
		description = parse_des(link)
	else:
		description=" Not available"
	post = {"title":title,
	         "url":"ycombinator.com",
            "link":link,
            "Date":pub_date,
            "content":description
            }

	post_id = ycomb.insert(post)
	print post_id


l4 = len(d['entries'])
for post in range(0,l4):
	ys = db.ys
	if(d.entries[post].has_key('title')):
		title = d.entries[post].title 
	else: 
		title=" "	
	if(d.entries[post].has_key('link')):
		link = d.entries[post].link
	else:
		link=""	
	if(d.entries[post].has_key('published')):
		pub_date  = d.entries[post].published
	else:
		pub_date=""	
	if(d.entries[post].has_key('link')):	
		description = parse_des(link)
	else:
		description=" Not available"
	post = {"title":title,
	         "url":"yourstory.com",
            "link":link,
            "Date":pub_date,
            "content":description
            }

	post_id = ys.insert(post)
	print post_id



