from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(db.String(), nullable=False, default='user')  # 'admin', 'tech_writer', or 'user'
    active = db.Column(db.Boolean, nullable=False, default=True)
    
    subscriptions = db.relationship('Subscription', back_populates='user', lazy='dynamic')
    wishlists = db.relationship('Wishlist', back_populates='user', lazy='dynamic')
    comments = db.relationship('Comment', back_populates='user', lazy='dynamic')
    contents = db.relationship('Content', back_populates='posted_by_user', lazy='dynamic')

# Category model
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    contents = db.relationship('Content', back_populates='category', lazy='dynamic')
    subscriptions = db.relationship('Subscription', back_populates='category', lazy='dynamic')

# Content model

class Content(db.Model):
    __tablename__ = 'contents'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content_type = db.Column(db.String(), nullable=False)  # 'video', 'audio', or 'article'
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False, index=True)
    posted_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    approved = db.Column(db.Boolean, default=False, index=True)
    
    # Relationships
    category = db.relationship('Category', back_populates='contents', lazy='joined')
    posted_by_user = db.relationship('User', back_populates='contents', lazy='joined')
    comments = db.relationship(
        'Comment', back_populates='content', lazy='dynamic', cascade='all, delete-orphan'
    )
    wishlists = db.relationship(
        'Wishlist', back_populates='content', lazy='dynamic', cascade='all, delete-orphan'
    )

# Comment model
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=True)
    
    content = db.relationship('Content', back_populates='comments')
    user = db.relationship('User', back_populates='comments')
    parent = db.relationship('Comment', remote_side=[id], back_populates='replies')
    replies = db.relationship('Comment', back_populates='parent', lazy='dynamic')

# Subscription model
class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    
    user = db.relationship('User', back_populates='subscriptions')
    category = db.relationship('Category', back_populates='subscriptions')

# Wishlist model
class Wishlist(db.Model):
    __tablename__ = 'wishlists'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), nullable=False)
    
    user = db.relationship('User', back_populates='wishlists')
    content = db.relationship('Content', back_populates='wishlists')
