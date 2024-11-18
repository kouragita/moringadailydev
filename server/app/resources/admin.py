from flask_restful import Resource
from app.models import db, Content, User

class ApproveContentResource(Resource):
    def patch(self, content_id):
        """
        Approve a content item by ID.
        """
        try:
            content = Content.query.get_or_404(content_id)
            content.approved = True
            db.session.commit()
            return {"message": "Content approved successfully."}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"Failed to approve content: {str(e)}"}, 400


class DeactivateUserResource(Resource):
    def patch(self, user_id):
        """
        Deactivate a user by ID.
        """
        try:
            user = User.query.get_or_404(user_id)
            if not user.active:  # Prevent unnecessary updates
                return {"message": "User is already deactivated."}, 200
            user.active = False
            db.session.commit()
            return {"message": "User deactivated successfully."}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"Failed to deactivate user: {str(e)}"}, 400


class ActivateUserResource(Resource):
    def patch(self, user_id):
        """
        Activate a user by ID.
        """
        try:
            user = User.query.get_or_404(user_id)
            if user.active:  # Prevent unnecessary updates
                return {"message": "User is already active."}, 200
            user.active = True
            db.session.commit()
            return {"message": "User activated successfully."}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"Failed to activate user: {str(e)}"}, 400
