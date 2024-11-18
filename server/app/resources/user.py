from flask import request
from flask_restful import Resource
from app.models import db, User
from app.schemas import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserListResource(Resource):
    def get(self):
        # Get page and per_page from query parameters, defaulting to None
        page = request.args.get('page', default=None, type=int)
        per_page = request.args.get('per_page', default=None, type=int)

        if page is not None and per_page is not None:
            # If both page and per_page are provided, paginate the results
            users = User.query.paginate(page=page, per_page=per_page, error_out=False)
            return {
                'users': users_schema.dump(users.items),
                'total': users.total,
                'page': users.page,
                'per_page': users.per_page,
                'next_page': users.next_num,
                'prev_page': users.prev_num,
            }, 200
        else:
            # If no pagination parameters are provided, return all users
            users = User.query.all()
            return users_schema.dump(users), 200

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user), 200
    
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return user_schema.dump(user), 200
    
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully."}, 200
