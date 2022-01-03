from werkzeug.security import safe_str_cmp
from user import User

# users = [
#     {
#         'id': 1,
#         'username': 'raj',
#         'password': 'asdf'
#     }
# ]
users = [
    User(1,'raj','asdf')
]

# username_mapping = {'raj':{
#         'id': 1,
#         'username': 'raj',
#         'password': 'asdf'
#     }
# }
username_mapping = {u.username: u for u in users}
userid_mapping ={}

# userid_mapping = {'id':{
#         'id': 1,
#         'username': 'raj',
#         'password': 'asdf'
#     }
# }

def authenticate(username,password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)