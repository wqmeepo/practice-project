class Config:
    SECRET_KEY = 'wqmeepo'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wq:Ab127276@88.218.200.18:3306/testdb?charset=utf8mb4'
    DEBUG = True


config = {
    'default': DevelopmentConfig
}
