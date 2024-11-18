import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db, User

SECRET_KEY = "your_secret_key"

class AuthService:
    @staticmethod
    def hash_password(password):
        # Using pbkdf2:sha256 for password hashing
        return generate_password_hash(password, method="pbkdf2:sha256")
    
    @staticmethod
    def verify_password(password, hashed_password):
        return check_password_hash(hashed_password, password)
    
    @staticmethod
    def generate_token(user_id):
        payload = {
            "user_id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token
    
    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload["user_id"]
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired.")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token.")
