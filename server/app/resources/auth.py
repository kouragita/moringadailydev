from flask import request, jsonify
from flask_restful import Resource
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import db, User

class SignupResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role', 'user')
        
        if User.query.filter_by(email=email).first():
            return {"message": "Email already exists."}, 400
        
        hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(user)
        db.session.commit()
        return {"message": "User created successfully."}, 201

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return {"message": "Invalid credentials."}, 401
        
        return {"message": "Login successful.", "user_id": user.id}, 200
