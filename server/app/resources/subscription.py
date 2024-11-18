from flask_restful import Resource
from flask import request
from app.models import db, Subscription
from app.schemas import SubscriptionSchema

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

class SubscriptionListResource(Resource):
    def post(self):
        data = request.get_json()
        
        subscription = subscription_schema.load(data, session=db.session)
        db.session.add(subscription)
        db.session.commit()
        return subscription_schema.dump(subscription), 201

class SubscriptionResource(Resource):
    def get(self, subscription_id):
        subscription = Subscription.query.get_or_404(subscription_id)
        return subscription_schema.dump(subscription)

    def patch(self, subscription_id):
        subscription = Subscription.query.get_or_404(subscription_id)
        data = request.get_json()
        subscription = subscription_schema.load(data, instance=subscription, partial=True)
        db.session.commit()
        return subscription_schema.dump(subscription)

    def delete(self, subscription_id):
        subscription = Subscription.query.get_or_404(subscription_id)
        db.session.delete(subscription)
        db.session.commit()
        return '', 204
