import nltk
import json
from nltk import *
from nltk.text import Text
from nltk.tag import pos_tag

from urllib2 import Request, urlopen, URLError


text1 = open("alumni.txt","r").read().decode('utf-8')
tokens = nltk.tokenize.word_tokenize(text1)
text = nltk.Text(tokens)
print len(tokens)
synonyms = ['National Insitute of Techology, Warangal',
			'National Institue of Technology , Warangal',
			'National Institure of Technology, Warangal',
			'National institute of Technolgy, Warangal',
			'National Institute of Technology (Regional Engineering College) (REC) (NIT) - Warangal',
			'National Institute of Technology Warangal',
			'National Institute of Technology Warangal (NITW)',
			'National Institute of Technology Warangal, AP, India',
			'National Institute of Technology Warangal,A.P.',
			'National Institute of Technology, Warangal, A.P., India',
			'National Institute of technology warangal,chemical engg',
			'National Institute of Technology, Warangal (RECW)',
			'National Institute of Technology, Warangal, Andhra Pradesh, India'
			'National Institute of Technology, Warangal, India',
			'National Institute of Technology,warangal (civil)',
			'National Institute of Technology(NIT) - Warangal',
			'National Institute of Techology,Warangal',
			'National Institute of Techonology, Warangal',
			'National Institution of Technology,warangal',
			'National Intitute Of Technology,Warangal',
			'NIT WAR',
			'NIT Waranagl',
			'NIT WARANGAL',
			'NIT Warangal (Adhra Pradesh)',
			'NIT Warangal 08',
			'nit warangal ECE',
			'NIT WARANGAL IN COM SCIENCE',
			'NIT WARANGAL IN COMPUTER SCIENCE AND ENGINEERING',
			'nit warangal-eee branch',
			'NIT Warangal, India',
			'NIT Warangal,AP',
			'NIT Warangal(Electrical and Electronics Engg.)',
			'NIT Warangal/Deemed University',
			'NIT Waranngal',
			'nit warrangal',
			'NIT, Warangal   09-13',
			'NITW',
			'NITW,ECE',
			'NITW/GITAM',
			'NITWARANGAL-EEE',
			'nitwrangal',
			'REC Warangal',
			'REC Warangal 1974-79',
			'REC Warangal, AP',
			'Regional Engineering College, Warangal',
			'Regional Engineering College, Warangal, AP, India',
			'Regional Engineering College, Warangal (AP)',
			'REC/NIT Warangal',
]

value=0
for x in text:
	for y in synonyms:
		if(x==y):
			value+=1

a1 = value
a2 = text.count("alumni of NITW")
a3 = text.count("alumnus of NITW")
a4 = text.count("alumni of nitwrangal")

count = a1+a2+a3+a4
if(count>0):
	val=0.2
else:
	val=-0.2




text1 = open("alumni.txt","r").read().decode('utf-8')
text = pos_tag(text1.split())

propernouns = [word for word,pos in text if pos == 'NNP']

print propernouns
count=0
for a in propernouns:
	request = Request('http://www.nitwaa.in/api/search?q='+a)
	try:
		response = urlopen(request)
		kittens = response.read()
		x = json.loads(kittens)
		a = x['data']['total_results']
		print a
		count = count+a
		print kittens[:200]
	except URLError, e:
	    print 'No kittez. Got an error code:', e

if(count>0):
	val1 = 0.4
else:
	val1 = -0.4



