class Config(object):
        DEBUG = False
        TESTING = False
        CSRF_ENABLED = True
        SECRET_KEY = "This is not permanent"
        SQLALCHEMY_DATABASE_URI = "postgresql://josh:tinker12@localhost/mapdb"

class ProductionConfig(Config):
        DEFUG = False

class StagingConfig(Config):
        DEVELOPMENT = True
        Debug = True

class DevelopmentConfig(Config):
        DEVELOPMENT = True
        Debug = True

class TestingConfig(Config):
        TESTING = True
