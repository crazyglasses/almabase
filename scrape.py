
import requests
bbc = requests.get('http://www.cnn.com/')
_bbc_content = bbc.content


file = open('bbc.txt','w')
file.write(_bbc_content)
file.close 
