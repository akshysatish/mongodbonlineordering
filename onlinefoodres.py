# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 04:09:35 2018

@author: Akshay Satish
"""

import pymongo
from tkinter import *

client = pymongo.MongoClient()
db=client["online_delivery"]
collection = db["restaurants"]
root=Tk()
Label(root,text="Enter Order").grid(row=0,column=5)
Label(root,text="Enter Name").grid(row=1,column=3)
name=Entry(root)
name.grid(row=1,column=5)
Label(root,text="Enter Dish").grid(row=2,column=3)
Order=Entry(root)
Order.grid(row=2,column=5)
Label(root,text="Enter Quantity").grid(row=3,column=3)
Quantity=Entry(root)
Quantity.grid(row=3,column=5)


def insertOrder():
    i="1002"
    count = db.collection.find({}).count()
    db.collection.insert_one({
            "Oid":str(count+1),
            "name":name.get(),
            "Dish":Order.get(),
            "Quantity":Quantity.get()})

Submit=Button(root,text="Submit",command=insertOrder).grid(row=4,column=6)
root.mainloop()