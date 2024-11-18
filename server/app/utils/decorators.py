# from flask import request, jsonify
# from functools import wraps
# from services.auth_service import AuthService
# from models import User

# def role_required(roles):
#     """
#     A decorator to enforce role-based access control.
#     :param roles: List of roles allowed (e.g., ["admin", "tech_writer"]).
#     """
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             token = request.headers.get("Authorization")
#             if not token:
#                 return jsonify({"message": "Authorization token is missing"}), 401
            
#             try:
#                 user_id = AuthService.decode_token(token)
#                 user = User.query.get(user_id)
#                 if user.role not in roles:
#                     return jsonify({"message": "Access denied. Insufficient permissions"}), 403
#             except ValueError as e:
#                 return jsonify({"message": str(e)}), 401
            
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
