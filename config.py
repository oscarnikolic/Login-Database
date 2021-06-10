import os
from flask.cli import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
asset_dir = os.path.join(basedir, 'asset')
data_dir = os.path.join(asset_dir, 'data')
load_dotenv(os.path.join(basedir, os.path.pardir, '.env'))
DATABASE_URL = os.environ.get('DATABASE_URL')
print(DATABASE_URL)

class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    THREADS_PER_PAGE = 2
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL

config = DevelopmentConfig