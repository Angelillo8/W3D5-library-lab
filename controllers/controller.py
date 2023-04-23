from flask import render_template, request, redirect, url_for
from app import app
from models.books import books, get_book, add_new_book, delete_book
from models.book import Book

@app.route('/library')
def index():
    return render_template('index.html', title = 'Home', books = books)

@app.route('/library/<title>')
def single_book(title):
  print(title)
  book = get_book(title)
  return render_template('book.html', book = book)

@app.route('/library', methods = ['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return index()

@app.route('/delete/<title>', methods=['POST'])
def delete(title):
  delete_book(title)
  return redirect('/library')