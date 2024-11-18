# import os

# class Config:
#     """Base configuration."""
#     SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     DEBUG = False
#     TESTING = False
#     CORS_HEADERS = "Content-Type"
#     JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")

# class DevelopmentConfig(Config):
#     """Development configuration."""
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL", "sqlite:///dev.db")

# class TestingConfig(Config):
#     """Testing configuration."""
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///test.db")

# class ProductionConfig(Config):
#     """Production configuration."""
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///prod.db")
#     DEBUG = False

# # Map configurations for environment
# configurations = {
#     "development": DevelopmentConfig,
#     "testing": TestingConfig,
#     "production": ProductionConfig
# }

class Config:
    DEBUG = True 
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///dailydev.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://moringadb_user:S6vv0iSnB17LwZsf2B1zJ7MZMCCocVw5@dpg-cssv6t8gph6c7399f9eg-a.oregon-postgres.render.com/moringadb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
