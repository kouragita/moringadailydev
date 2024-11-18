from app.models import db, User, Category, Content, Comment, Subscription, Wishlist
from werkzeug.security import generate_password_hash

def seed_data():
    # Clear existing data
    db.drop_all()
    db.create_all()
    
    # Users
    admin = User(
        username='admin_user',
        email='admin@example.com',
        password=generate_password_hash('adminpass', method='pbkdf2:sha256'),
        role='admin'
    )
    writer = User(
        username='tech_writer',
        email='writer@example.com',
        password=generate_password_hash('adminpass', method='pbkdf2:sha256'),
        role='tech_writer'
    )
    regular_user = User(
        username='regular_user',
        email='user@example.com',
        password=generate_password_hash('adminpass', method='pbkdf2:sha256'),
        role='user'
    )

    # Add users
    db.session.add_all([admin, writer, regular_user])
    db.session.commit()

    # Categories
    categories = [
        Category(name='Technology', description='Latest tech trends and news.'),
        Category(name='Health', description='Tips and news on health and wellness.'),
        Category(name='Entertainment', description='Movies, music, and pop culture.')
    ]
    db.session.add_all(categories)
    db.session.commit()

    # Content
    content_items = [
        Content(
            title='AI in 2024',
            description='How artificial intelligence is shaping the world.',
            content_type='article',
            category_id=1,
            posted_by=2,
            approved=True  # Admin approved
        ),
        Content(
            title='Top 10 Healthy Habits',
            description='Daily habits for a healthier lifestyle.',
            content_type='video',
            category_id=2,
            posted_by=2,
            approved=False  # Pending admin approval
        ),
        Content(
            title='Upcoming Movie Releases',
            description='Exciting movies to look forward to this year.',
            content_type='audio',
            category_id=3,
            posted_by=2,
            approved=True  # Admin approved
        )
    ]
    db.session.add_all(content_items)
    db.session.commit()

    # Comments
    comments = [
        Comment(
            content_id=1,
            user_id=3,
            text='This is such an insightful article about AI!'
        ),
        Comment(
            content_id=3,
            user_id=3,
            text='I can’t wait to see these movies!'
        )
    ]
    db.session.add_all(comments)
    db.session.commit()

    # Subscriptions
    subscriptions = [
        Subscription(user_id=3, category_id=1),
        Subscription(user_id=3, category_id=2)
    ]
    db.session.add_all(subscriptions)
    db.session.commit()

    # Wishlist
    wishlists = [
        Wishlist(user_id=3, content_id=1),
        Wishlist(user_id=3, content_id=3)
    ]
    db.session.add_all(wishlists)
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == '__main__':
    from app import create_app  # Ensure this is your app factory method
    app = create_app()
    with app.app_context():
        seed_data()
