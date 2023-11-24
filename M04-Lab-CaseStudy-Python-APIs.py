#!/usr/bin/env python
# coding: utf-8

# 

# In[ ]:


# SDEV220-Software Development - Python

# Name : M04 Lab - Case Study: Python APIs
# Author : M Mekoya 
# Date : 11-24-2023 
# Version: 1 
# Purpose: Python APIs
# 


# Navigate to the following URL, and watch the video on APIs and how to develop them in Python.  Complete the same steps and following along with the tutorial using VSCode:
# 
# REST API Crash CourseLinks to an external site.
# 
# Complete the following steps:
# After watching the video, create a CRUD API for a Book instead of a Drink in the video example above.  The Book model should have the following parameters:
# id
# book_name
# author
# publisher

# In[2]:


from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)


# In[ ]:


app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


# Creating Book Class with book_name, author and publisher

# In[ ]:


class Books (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column (db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"


# In[ ]:


@app.route ('/')
def index ():
    return 'Hello!'


# Getting Books

# In[ ]:


@app.route ('/Books')
def get_books ():
    Books = Books.query.all()
    output = []
    
    for book in Books:
        books_data = {'Name ' : Books.book_name, 'Author' : Books.author,
                     'Publisher ' : Books.publisher}
        output.append (Books_data)
        
    
    return {"Books" : output}


# In[ ]:


@app.route ('/Books/<id>')
def get_book(id):
    book = Books.query.get_or_404(id)
    return jsonify ({"name" : Books.name, "Author" : Books.author, "Publisher " : Books.publisher})


# Adding Book To the Database

# In[ ]:


@app.route ('/Books', methods = ['POST'])
def add_book ():
    books = Books (book_name = request.json ['name'],
                  author = request.json ['author'],
                  publisher = request.json ['publisher'])
    de.session.add(Books)
    db.session.commit ()
    return {'id' : Books.id}


# Deleting Book from the Database

# In[ ]:


@app.route ('/Books/<id>', methods = [DELETE])
def delete_book (id):
    book = Books.query.get (id)
    if book is None:
        return {"Error: Book Does not Exist!!!"}
    db.session.delete (Books)
    db.session.commite ()
    return {"Message" : "Successes!"}
    

