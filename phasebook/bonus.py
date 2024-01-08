from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("bonus", __name__, url_prefix="/bonus")

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

    def custom_sort(user):
       
        return (
            query.get('id', '') != '' and str(user.get('id', '')) == query.get('id', ''),
            query.get('name', '') != '' and query.get('name', '').lower() in user.get('name', '').lower(),
            query.get('age', '') != '' and int(query.get('age', 0)) - 1 <= int(user.get('age', 0)) <= int(query.get('age', 0)) + 1,
            query.get('occupation', '') != '' and query.get('occupation', '').lower() in user.get('occupation', '').lower()
        )


    result = sorted(result, key=custom_sort, reverse=True)
    return result

@bp.route("")
def search():
    return search_users(USERS, request.args.to_dict()), 200
