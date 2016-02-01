from bs4 import BeautifulSoup
soup = BeautifulSoup(open("random.txt"),"lxml")
for tag in soup.find_all('p'):
	if(tag.name=="a" and tag.name=="script" and tag.name=="li" and tag.name=="ul" and tag.name=="div" and tag.name=="link" and tag.name=="span"):
		tag.replaceWith('')
for script in soup(["script", "style","a","li","span"]):
    script.extract()    # rip it out

print soup.get_text()