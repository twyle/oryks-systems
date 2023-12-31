"""This module declares the app configuration.

The classes include:

BaseConfig:
    Has all the configurations shared by all the environments.

"""
import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration."""

    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get(
        "SECRET_KEY", "df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506"
    )
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", 'sqlite:///./oryks.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development confuguration."""

    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get(
        "SECRET_KEY", "df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506"
    )


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


class ProductionConfig(BaseConfig):
    """Production configuration."""

    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


Config = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": ProductionConfig,
    "staging": ProductionConfig,
}
