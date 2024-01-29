from app import os

class Config(object):
   DEBUG=False
   TESTING=False


class ProductionConfig(Config):
   # *** FLASK CONFIG OBJ ***
   ENV="production"


class DevelopmentConfig(Config):
   # *** FLASK CONFIG OBJ ***
   ENV="development"
   DEBUG=True

class TestingConfig(Config):
   # *** FLASK CONFIG OBJ ***
   ENV="testing"
   TESTING=True
