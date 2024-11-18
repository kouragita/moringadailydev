from flask_mail import Message
from extensions import mail
from app.models import User

class NotificationService:
    @staticmethod
    def send_notification_email(user_email, subject, message_body):
        msg = Message(subject, sender="noreply@example.com", recipients=[user_email])
        msg.body = message_body
        mail.send(msg)
    
    @staticmethod
    def send_bulk_notifications(user_ids, subject, message_body):
        users = User.query.filter(User.id.in_(user_ids)).all()
        for user in users:
            NotificationService.send_notification_email(user.email, subject, message_body)
