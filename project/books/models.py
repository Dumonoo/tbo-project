from project import db, app
import re


# Book model
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    author = db.Column(db.String(64))
    year_published = db.Column(db.Integer, nullable=False)
    book_type = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='available')

    def __init__(self, name, author, year_published, book_type, status='available'):
        if not name or len(name.strip()) == 0:
            raise ValueError("Book name cannot be empty")
        if year_published <= 0:
            raise ValueError("Year published must be positive")
        if book_type not in ['2days', '5days', '10days']:
            raise ValueError("Invalid book type")
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        self.status = status

    def __repr__(self):
        return f"Book(ID: {self.id}, Name: {self.name}, Author: {self.author}, Year Published: {self.year_published}, Type: {self.book_type}, Status: {self.status})"


with app.app_context():
    db.create_all()