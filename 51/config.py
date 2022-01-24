class Config:
    SECRET_KEY = 'wqmeepo'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI =
    DEBUG = True


config = {
    'default': DevelopmentConfig
}
