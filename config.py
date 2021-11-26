import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../warehouse.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    HOST = os.environ.get("POSTGRESQL_HOST")
    PORT = os.environ.get("POSTGRESQL_PORT")
    USER = os.environ.get("POSTGRESQL_USER")
    PASSWORD = os.environ.get("POSTGRESQL_PASSWORD")
    DATABASE = os.environ.get("POSTGRESQL_DATABASE")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
    "default": DevelopmentConfig,
}
