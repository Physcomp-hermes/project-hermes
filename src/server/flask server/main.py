from flask import Flask
from flask_restx import Api, Resource, fields, reqparse
import requests
# from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.exceptions import BadRequest
import random
from datetime import datetime
import sqlite3

DATABASE_NAME = "hermes.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME, detect_types=sqlite3.PARSE_DECLTYPES)
    return conn


app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='API Title', description='A simple API')

ns = api.namespace('actors', description='Actors operations')

actor = api.model('Actor', {
    'id': fields.Integer(readonly=True, description='The unique integer identifier'),
    'name': fields.String(required=True, description='name of an actor'),
    'last-update': fields.DateTime(required=True, description='the time the collection is stored in the database'),
    '_links': fields.Raw(),
})

todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

class ActorDAO(object):
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        statement = "SELECT * FROM actor"
        cursor.execute(statement)

        res = cursor.fetchall()

        response = []
        for r in res:
            response.append({'id': r[0],
                             'name': r[1],
                             'last-update': datetime.fromisoformat(r[2]),  # .strftime('%d/%m/%Y')
                             '_links': {'self': {'href': r[3]}}})

        return response

    @staticmethod
    def get(id):
        db = get_db()
        cursor = db.cursor()
        statement = "SELECT id, name, last_update, href FROM actor WHERE id = ?"
        cursor.execute(statement, [id])
        res = cursor.fetchone()
        if not res:
            api.abort(404, "Actor {} doesn't exist".format(id))
        response = {'id': res[0],
                    'name': res[1],
                    'last-update': datetime.fromisoformat(res[2]),  # .strftime('%d/%m/%Y')
                    '_links': {'self': {'href': res[3]}}}
        return response

    @staticmethod
    def create(data):
        db = get_db()
        cursor = db.cursor()

        name = data['person']['name']
        last_update = datetime.now()
        href = data['person']['_links']['self']['href']

        statement = f"INSERT INTO actor(name, last_update, href) VALUES (?, ?, ?)"
        cursor.execute(statement, [name, last_update, href])
        db.commit()

        response = {'id': cursor.lastrowid,
                    'name': name,
                    'last-update': last_update,  # .strftime('%d/%m/%Y')
                    '_links': {'self': {'href': href}}}

        return response

    @staticmethod
    def update(id, data):
        db = get_db()
        cursor = db.cursor()
        statement = "UPDATE actor SET name = ?, last_update = ? WHERE id = ?"
        last_update = datetime.now()
        cursor.execute(statement, [data['name'], last_update, id])
        db.commit()

        response = {'id': cursor.lastrowid,
                    'name': data['name'],
                    'last-update': last_update,
                    '_links': {'self': {'href': 'href'}}}

        return response

    @staticmethod
    def delete(id):
        db = get_db()
        cursor = db.cursor()
        statement = "DELETE FROM actor WHERE id = ?"
        print(cursor.execute(statement, [id]))
        print(db.commit())
        return True


DAO = ActorDAO()


@ns.route('/<int:id>')
@ns.response(404, 'Actor not found')
@ns.param('id', 'The task identifier')
class Actor(Resource):
    """Show a single actor and lets you delete them"""

    @ns.doc('get_actor')
    @ns.marshal_with(actor)
    def get(self, id):
        """Fetch a given resource"""
        return DAO.get(id)

    @ns.doc('delete_actor')
    @ns.response(204, 'Actor deleted')
    def delete(self, id):
        """Delete a task given its identifier"""
        if DAO.delete(id):
            return 'deleted', 200

        return '', 204

    @ns.expect(actor)
    @ns.marshal_with(actor)
    def put(self, id):
        """Update a task given its identifier"""
        return DAO.update(id, api.payload)


post_parser = reqparse.RequestParser()
post_parser.add_argument('name', required=True, help="Name cannot be blank!")

get_parser = reqparse.RequestParser()
get_parser.add_argument('order', type=str, default="+id", help='Order by name or id')
get_parser.add_argument("page", type=int, required=False, default=1, help="Page number")
get_parser.add_argument("size", type=int, required=False, default=10, help="Page size")
get_parser.add_argument('filter', type=str, default="id, name")


@ns.route('')
class Actors(Resource):
    """Shows a list of all actors, and lets you POST to add new actors"""

    @ns.doc('list_actors')
    @ns.expect(get_parser)
    @ns.marshal_list_with(actor)
    def get(self):
        """List all actors"""
        args = get_parser.parse_args()

        print(args)

        return DAO.get_all()

    @ns.doc('add_actor')
    @ns.expect(post_parser)
    @ns.marshal_with(actor, code=201)
    def post(self):
        """Add a new actor"""
        name = post_parser.parse_args()["name"]
        response = requests.get(f"https://api.tvmaze.com/search/people?q={name}")


        # print(response.json())

        if not response.json():
            raise BadRequest('Actor name not found')

        return DAO.create(random.choice(response.json())), 201


if __name__ == "__main__":
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='127.0.0.1', port=5000, debug=False)
