# def validate_email(email):
#     import re
#     email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     return re.match(email_regex, email) is not None

# def validate_password(password):
#     """
#     Validates password strength:
#     - At least 8 characters
#     - Includes both letters and numbers
#     """
#     if len(password) < 8:
#         return False
#     has_number = any(char.isdigit() for char in password)
#     has_letter = any(char.isalpha() for char in password)
#     return has_number and has_letter

# def validate_non_empty(value, field_name):
#     if not value.strip():
#         raise ValueError(f"{field_name} cannot be empty.")
