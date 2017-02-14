# config.py


import os


class BaseConfig(object):
    """
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', '5(15ds+i2+%ik6z&!yer+ga9m=e%jcqiz_5wszg)r-z!2--b2d')
    DEBUG = os.environ.get('DEBUG', True)
    APIKEY = os.environ.get('APIKEY', "apikey")

