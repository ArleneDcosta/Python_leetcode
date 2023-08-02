from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLACHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)

'''Below code is for one to many , 1 author for many books'''
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', backref='author')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

'''Below code is for its object creation'''

# Create an Author object
author = Author(name='John Doe')

# Create multiple Book objects associated with the author
book1 = Book(title='Book 1', author=author)
book2 = Book(title='Book 2', author=author)

# Add the author and books to the session and commit the changes to the database
db.session.add(author)
db.session.add(book1)
db.session.add(book2)
db.session.commit()
'*******************************************************'

'''Below code is for many to many '''

authors_books = db.Table('authors_books',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', secondary=authors_books, backref='authors')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    authors = db.relationship('Author', secondary=authors_books, backref='books')
'''Below code is for object creation for the same'''

# Create an Author object
author1 = Author(name='John Doe')

# Create another Author object
author2 = Author(name='Jane Smith')

# Create a Book object
book = Book(title='Book 1')

# Associate author1 and author2 with the book
book.authors.append(author1)
book.authors.append(author2)

# Add the authors and book to the session and commit the changes to the database
db.session.add(author1)
db.session.add(author2)
db.session.add(book)
db.session.commit()
