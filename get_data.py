from pymongo import MongoClient
client = MongoClient()
db = client.news_articles
for post in db.et.find():
	print post