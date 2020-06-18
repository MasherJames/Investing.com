import os


class Config():
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    """Configurations for Staging."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_TESTING_URL')


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
