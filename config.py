import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Share configuration for application"""

    SECRET_KEY = 'Trust guess me'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    """Path and name db in my config"""

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://buxtabaraxta:07079185Qq@buxtabaraxta.mysql.pythonanywhere-services.com/buxtabaraxta@tr_task'

config = {
    'devconfig': DevConfig,

    'default': DevConfig
}
