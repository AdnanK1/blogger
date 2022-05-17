import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adnan:adnank720@localhost/blogger'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://zkegooymmmwpcz:acdca99c384267dc807e7224c8d4a458b782b33b406542ec5823ca992e4adbab@ec2-3-229-11-55.compute-1.amazonaws.com:5432/d6acpdt1d37rth'
    
    
class DevConfig(Config):
    
    DEBUG = True
    pass
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
