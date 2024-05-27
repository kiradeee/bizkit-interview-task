from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    id = request.args.get('id', type=str)
    name = request.args.get('name', type=str)
    age = request.args.get('age', type=int)
    occupation = request.args.get('occupation', type=str)
    
    result = search_users(USERS, id=id, name=name, age=age, occupation=occupation)

    return result

def search_users(users, id=None, name=None, age=None, occupation=None):
    result = []

    if id is None and name is None and age is None and occupation is None:
        return users

    if id is not None:
        result += [user for user in users if user['id'] == id]

    if name is not None:
        result += [user for user in users if name.lower() in user['name'].lower()]

    if age is not None:
        result += [user for user in users if age - 1 <= user['age'] <= age + 1]

    if occupation is not None:
        result += [user for user in users if occupation.lower() in user['occupation'].lower()]

    result = [dict(t) for t in {tuple(d.items()) for d in result}]

    return result