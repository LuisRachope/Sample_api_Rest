from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server


app, api = server.app, server.api

#Lista de livros para retornar como DB
books_db = [
    {'id': 0, 'title': 'War and Peace'},
    {'id': 1, 'title': 'Clean Code'},
    {'id': 2, 'title': 'In Search of Lost Time'},
    {'id': 3, 'title': 'Ulysses'},
    {'id': 4, 'title': 'Don Quixote'},
    {'id': 5, 'title': 'One Hundred Years of Solitude'},
    {'id': 6, 'title': 'The Great Gatsby'},
    {'id': 7, 'title': 'Moby Dick'},
    {'id': 8, 'title': 'Hamlet'},
    {'id': 9, 'title': 'The Odyssey'},
    {'id': 10, 'title': 'The Divine Comedy'}
]

@api.route('/books')
class BookList(Resource):
    def get(self, ):
        return books_db

    def post(self, ):
        response = api.payload
        books_db.append(response)
        try:
            return response, 200
        except:
            return 404

