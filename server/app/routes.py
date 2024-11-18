def register_routes(api):
    """
    Register all API routes.
    """
    from .resources.auth import SignupResource, LoginResource
    from .resources.user import UserListResource, UserResource
    from  .resources.admin import ApproveContentResource, DeactivateUserResource, ActivateUserResource
    from .resources.content import ContentListResource, ContentResource
    from .resources.category import CategoryListResource, CategoryResource
    from .resources.comment import CommentListResource, CommentResource
    from .resources.subscription import SubscriptionListResource, SubscriptionResource
    from .resources.wishlist import WishlistListResource, WishlistResource

    # Authentication
    api.add_resource(SignupResource, '/auth/signup')
    api.add_resource(LoginResource, '/auth/login')

    # User resources
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<int:user_id>')

    # Admin resources
    api.add_resource(ApproveContentResource, '/admin/content/approve/<int:content_id>')
    api.add_resource(DeactivateUserResource, '/admin/user/deactivate/<int:user_id>')
    api.add_resource(ActivateUserResource, '/admin/user/activate/<int:user_id>')
    # Content resources
    api.add_resource(ContentListResource, '/contents')
    api.add_resource(ContentResource, '/contents/<int:content_id>')

    # Category resources
    api.add_resource(CategoryListResource, '/categories')
    api.add_resource(CategoryResource, '/categories/<int:category_id>')

    # Comment resources
    api.add_resource(CommentListResource, '/comments')
    api.add_resource(CommentResource, '/comments/<int:comment_id>')

    # Subscription resources
    api.add_resource(SubscriptionListResource, '/subscriptions')
    api.add_resource(SubscriptionResource, '/subscriptions/<int:user_id>/<int:category_id>')

    # Wishlist resources
    api.add_resource(WishlistListResource, '/wishlists')
    api.add_resource(WishlistResource, '/wishlists/<int:wishlist_id>')
