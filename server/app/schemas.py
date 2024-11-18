from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models import User, Category, Content, Comment, Subscription, Wishlist
from app.models import db

# User schema
class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True  # Enable deserialization of instances
        sqla_session = db.session

    id = auto_field()
    username = auto_field()
    email = auto_field()
    role = auto_field()
    active = auto_field() 
    subscriptions = fields.Nested('SubscriptionSchema', many=True, exclude=('user',))
    wishlists = fields.Nested('WishlistSchema', many=True, exclude=('user',))

# Category schema
class CategorySchema(SQLAlchemySchema):
    class Meta:
        model = Category
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    name = auto_field()
    description = auto_field()
    contents = fields.Nested('ContentSchema', many=True, exclude=('category',))

# Content schema
class ContentSchema(SQLAlchemySchema):
    class Meta:
        model = Content
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    title = auto_field()
    description = auto_field()
    content_type = auto_field()
    category_id = fields.Int(required=True)  # Use IDs for creation
    posted_by = fields.Int(required=True)  # Use user ID for creation
    approved = auto_field(dump_only=True)  # Don't allow setting during creation

    # Properly reference the actual schema class for nested fields
    category = fields.Nested(CategorySchema, exclude=('contents',), dump_only=True)
    comments = fields.Nested('CommentSchema', many=True, exclude=('content',), dump_only=True)
    posted_by_user = fields.Nested(UserSchema, only=('id', 'username'), dump_only=True)

# Comment schema
class CommentSchema(SQLAlchemySchema):
    class Meta:
        model = Comment
        include_fk = True  # Include foreign key fields
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    content_id = fields.Int(load_only=True)
    user_id = fields.Int(load_only=True)
    text = auto_field()
    parent_comment_id = auto_field()
    replies = fields.Nested('CommentSchema', many=True, exclude=('parent_comment_id',))
    content = fields.Nested(ContentSchema, only=('id', 'title'), dump_only=True)
    user = fields.Nested(UserSchema, only=('id', 'username'), dump_only=True)

# Subscription schema
class SubscriptionSchema(SQLAlchemySchema):
    class Meta:
        model = Subscription
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    user = fields.Nested(UserSchema, only=('id', 'username'))
    category = fields.Nested(CategorySchema, only=('id', 'name'))

# Wishlist schema
class WishlistSchema(SQLAlchemySchema):
    class Meta:
        model = Wishlist
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    user_id = fields.Int(required=True)
    content_id = fields.Int(required=True)
    user = fields.Nested(UserSchema, only=('id', 'username'))
    content = fields.Nested(ContentSchema, only=('id', 'title'))
