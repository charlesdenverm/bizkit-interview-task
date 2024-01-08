from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

def search_users(users, query):
    result = []

    for user in users:
        include = False

        for key, value in query.items():
            if key == 'id' and str(user.get(key)) == value:
                include = True
            elif key == 'name' and value.lower() in user.get(key, '').lower():
                include = True
            elif key == 'age' and int(user.get(key, 0)) in range(int(value) - 1, int(value) + 2):
                include = True
            elif key == 'occupation' and value.lower() in user.get(key, '').lower():
                include = True

        if include:
            result.append(user)

    return result

@bp.route("")
def search():
    return search_users(USERS, request.args.to_dict()), 200
