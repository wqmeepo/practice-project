class Config:
    SECRET_KEY = 'wqmeepo'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:321@localhost:3306/testdb'
    DEBUG = True


config = {
    'default': DevelopmentConfig
}
