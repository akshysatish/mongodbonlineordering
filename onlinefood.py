# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 00:07:35 2018

@author: Akshay Satish
"""

import pymongo
from tkinter import *

client = pymongo.MongoClient()
db=client["online_delivery"]
collection = db["collection"]
root=Tk()
Label(root,text="Order Details").grid(row=0,column=5)
Label(root,text="OrderID").grid(row=2,column=0)
Label(root,text="Name").grid(row=2,column=6)
Label(root,text="Order").grid(row=2,column=9)
Label(root,text="Quantity").grid(row=2,column=14)

def showdetails():
    cursor=db.collection.find({})
    i=0
    for documents in cursor:
        Label(root,text=documents['Oid']).grid(row=i+3,column=0)
        Label(root,text=documents['name']).grid(row=i+3,column=6)
        Label(root,text=documents['Dish']).grid(row=i+3,column=9)
        Label(root,text=documents['Quantity']).grid(row=i+3,column=14)
        i=i+1
showdetails()

Ordid=(Entry(root))
Ordid.grid(row=3,column=18)

def deleteOrder():
    print(Ordid.get())
    OrderId=Ordid.get()
    print(type(OrderId))
    check = db.collection.delete_one({'Oid':OrderId})
    Label(root,text="Removed").grid(row=5,column=18)
    print(check.deleted_count)
    
#db.collection.delete_one({'Oid':1002})

Button(root,text="Remove Order",command=deleteOrder).grid(row=4,column=18)
root.mainloop()