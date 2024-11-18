from flask_restful import Resource
from flask import request
from app.models import db, Wishlist
from app.schemas import WishlistSchema

wishlist_schema = WishlistSchema()
wishlists_schema = WishlistSchema(many=True)

class WishlistListResource(Resource):
    def post(self):
        """
        Create a new wishlist.
        """
        data = request.get_json()
        # Pass the session to the load method
        wishlist = wishlist_schema.load(data, session=db.session)
        db.session.add(wishlist)
        db.session.commit()
        return wishlist_schema.dump(wishlist), 201

class WishlistResource(Resource):
    def get(self, wishlist_id):
        """
        Get a specific wishlist by ID.
        """
        wishlist = Wishlist.query.get_or_404(wishlist_id)
        return wishlist_schema.dump(wishlist)

    def patch(self, wishlist_id):
        """
        Update a specific wishlist.
        """
        wishlist = Wishlist.query.get_or_404(wishlist_id)
        data = request.get_json()
        wishlist_schema.load(data, instance=wishlist, session=db.session, partial=True)  # Ensure session is passed here too
        db.session.commit()
        return wishlist_schema.dump(wishlist)

    def delete(self, wishlist_id):
        """
        Delete a specific wishlist.
        """
        wishlist = Wishlist.query.get_or_404(wishlist_id)
        db.session.delete(wishlist)
        db.session.commit()
        return '', 204
