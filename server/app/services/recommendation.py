from app.models import Content, Subscription
from sqlalchemy.orm import joinedload

class RecommendationService:
    @staticmethod
    def get_recommendations(user_id):
        # Get the categories the user is subscribed to
        subscriptions = Subscription.query.filter_by(user_id=user_id).all()
        subscribed_categories = [sub.category_id for sub in subscriptions]

        # Query content based on subscriptions
        recommendations = Content.query.filter(
            Content.category_id.in_(subscribed_categories),
            Content.approved == True
        ).options(joinedload(Content.category)).all()

        return recommendations
