from flask import request
from flask_restful import Resource
from app.models import db, Content
from app.schemas import ContentSchema, UserSchema, CategorySchema  # Ensure all required schemas are imported
import logging
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

logging.basicConfig(level=logging.ERROR)

content_schema = ContentSchema(session=db.session)
contents_schema = ContentSchema(many=True, session=db.session)


class ContentListResource(Resource):
    def get(self):
        """
        Retrieve all approved contents.
        """
        try:
            contents = Content.query.filter_by(approved=True).all()
            if not contents:
                return {"message": "No approved contents found."}, 404
            return contents_schema.dump(contents), 200
        except Exception as e:
            logging.error(f"Error retrieving contents: {str(e)}")
            return {"message": f"Failed to retrieve contents: {str(e)}"}, 500

    def post(self):
        """
        Create a new content entry.
        """
        data = request.get_json()
        if not data:
            return {"message": "No input data provided"}, 400
        try:
            content = content_schema.load(data, session=db.session)
            db.session.add(content)
            db.session.commit()
            return content_schema.dump(content), 201
        except ValidationError as err:
            db.session.rollback()
            logging.error(f"ValidationError: {err.messages}")
            return {"errors": err.messages}, 400
        except IntegrityError as ie:
            db.session.rollback()
            logging.error(f"IntegrityError: {str(ie)}")
            return {"message": "Integrity error occurred, possibly a duplicate entry."}, 400
        except Exception as e:
            db.session.rollback()
            logging.error(f"Exception: {str(e)}")
            return {"message": f"Failed to create content: {str(e)}"}, 400


class ContentResource(Resource):
    def get(self, content_id):
        """
        Retrieve a specific content by its ID.
        """
        try:
            content = Content.query.get_or_404(content_id)
            return content_schema.dump(content), 200
        except Exception as e:
            logging.error(f"Error retrieving content by ID: {str(e)}")
            return {"message": f"Failed to retrieve content: {str(e)}"}, 404

    def put(self, content_id):
        """
        Update an existing content entry by its ID.
        """
        content = Content.query.get_or_404(content_id)
        data = request.get_json()
        try:
            content.title = data.get('title', content.title)
            content.description = data.get('description', content.description)
            db.session.commit()
            return content_schema.dump(content), 200
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error updating content: {str(e)}")
            return {"message": f"Failed to update content: {str(e)}"}, 400

    def delete(self, content_id):
        """
        Delete a specific content entry by its ID.
        """
        content = Content.query.get_or_404(content_id)
        try:
            db.session.delete(content)
            db.session.commit()
            return {"message": "Content deleted successfully."}, 200
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error deleting content: {str(e)}")
            return {"message": f"Failed to delete content: {str(e)}"}, 400
