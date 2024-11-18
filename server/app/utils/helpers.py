# def paginate_query(query, page, per_page):
#     """
#     Paginates the results of a SQLAlchemy query.
#     :param query: SQLAlchemy query object
#     :param page: Current page number
#     :param per_page: Items per page
#     :return: Dictionary with paginated data
#     """
#     paginated = query.paginate(page=page, per_page=per_page, error_out=False)
#     return {
#         "items": [item.to_dict() for item in paginated.items],
#         "total": paginated.total,
#         "pages": paginated.pages,
#         "current_page": paginated.page
#     }

# def format_response(data=None, message="Success", status=200):
#     """
#     Formats a consistent JSON response.
#     :param data: Response data
#     :param message: Success or error message
#     :param status: HTTP status code
#     :return: Dictionary representing the response
#     """
#     return {
#         "status": status,
#         "message": message,
#         "data": data
#     }
# from flask import jsonify

# def format_response(message, status):
#     return jsonify({"message": message, "status": status})

# def register_error_handlers(app):
#     """
#     Register custom error handlers for the Flask app.
#     """
#     @app.errorhandler(404)
#     def resource_not_found(e):
#         return format_response(message="Resource not found", status=404), 404

#     @app.errorhandler(500)
#     def internal_server_error(e):
#         return format_response(message="An internal error occurred", status=500), 500
