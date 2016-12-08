import urllib.request
import re


def get_book(book_id):
    url_book='https://api.douban.com/v2/book/'+str(book_id)
    url_book_op=urllib.request.urlopen(url_book,timeout=10)
    data_book=url_book_op.read().decode('utf-8')
    return data_book


def get_book_isbn(isbn_no):
    url_book = 'https://api.douban.com/v2/book/isbn/' + str(isbn_no)
    url_book_op = urllib.request.urlopen(url_book, timeout=10)
    data_book = url_book_op.read().decode('utf-8')
    return data_book


def get_movie(movie_id):
    url_movie = 'https://api.douban.com/v2/movie/subject/' + str(movie_id)
    url_movie_op = urllib.request.urlopen(url_movie, timeout=10)
    data_movie = url_movie_op.read().decode('utf-8')
    return data_movie


def get_movie_top250():
    url_movie = 'https://api.douban.com/v2/movie/top250'
    url_movie_op = urllib.request.urlopen(url_movie, timeout=10)
    data_movie = url_movie_op.read().decode('utf-8')
    return data_movie


def get_music(music_id):
    url_music = 'https://api.douban.com/v2/music/' + str(music_id)
    url_music_op = urllib.request.urlopen(url_music, timeout=10)
    data_music = url_music_op.read().decode('utf-8')
    return data_music


# print(get_book_isbn(9787807681700))
print(get_movie_top250())