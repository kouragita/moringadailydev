from flask_restful import Resource
from flask import request
from app.models import db, Comment
from app.schemas import CommentSchema

# Pass session explicitly when initializing the schema
comment_schema = CommentSchema(session=db.session)
comments_schema = CommentSchema(many=True, session=db.session)

class CommentListResource(Resource):
    def get(self):
        # Fetch all comments
        comments = Comment.query.all()
        return comments_schema.dump(comments), 200
    
    def post(self):
        data = request.get_json()  # Getting the JSON data from the request
        try:
            # Pass session explicitly when deserializing
            comment = comment_schema.load(data, session=db.session)  # Pass session here
            db.session.add(comment)
            db.session.commit()
            return comment_schema.dump(comment), 201  # Return the serialized data
        except Exception as e:
            db.session.rollback()  # Rollback in case of an error
            return {"message": f"Failed to create comment: {str(e)}"}, 400

class CommentResource(Resource):
    def delete(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()
        return {"message": "Comment deleted successfully."}, 200
