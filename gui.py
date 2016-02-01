import Tkinter
from Tkinter import *
import tkMessageBox
import datetime
from pymongo import MongoClient
client = MongoClient()
db = client.news_articles


top = Tkinter.Tk()

def openit():
	a = E1.get()
	b = int(E2.get())
	c = int(E3.get())
	d = int(E4.get())
	date1 = datetime.date(d, c, b)
	for post in db.cnn.find({"url": a}):
		print post['content']
	for post in db.et.find({"url": a}):
		print post
	for post in db.ys.find({"url": a}):
		print post
	for post in db.ycomb.find({"url": a}):
		print post

top.title("almabase")
top.geometry("400x200")
B = Tkinter.Button(top,text="submit",command=openit)
B.grid(row=8,column=1)
L1 = Label(top, text="Article Name")
E1 = Entry(top, bd =5)

L2 = Label(top, text="date")
E2 = Entry(top, bd =5)

L3 = Label(top, text="month")
E3 = Entry(top, bd =5)

L4 = Label(top, text="year")
E4 = Entry(top, bd =5)


L1.grid(row=1)
L2.grid(row=2)
L3.grid(row=3)
L4.grid(row=4)

E1.grid(row=1,column=1)
E2.grid(row=2,column=1)
E3.grid(row=3,column=1)
E4.grid(row=4,column=1)



top.mainloop()

