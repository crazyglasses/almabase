
import requests


cnn = requests.get('http://rss.cnn.com/rss/edition.rss')
ycomb = requests.get('https://news.ycombinator.com/rss')
et = requests.get('http://economictimes.indiatimes.com/rssfeedsdefault.cms')
ys= requests.get('http://yourstory.com/feed/')

cnn_content = cnn.content
ycomb_content = ycomb.content
et_content = et.content
ys_content = ys.content
file = open('xml/cnn.xml','w')
file.write(cnn_content)
file.close 

file = open('xml/ycomb.xml','w')
file.write(ycomb_content)
file.close 

file = open('xml/et.xml','w')
file.write(et_content)
file.close 

file = open('xml/ys.xml','w')
file.write(ys_content)
file.close 

