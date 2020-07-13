import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/pitch'

class ProdConfig(Config):
    '''
    Production configurations child class
    '''

class DevConfig(Config):
    '''
    Development configurations child class
    '''

    DEBUG = True