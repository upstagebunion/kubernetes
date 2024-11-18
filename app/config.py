import os

db_user = "user"
db_password = "userpassword"
db_host = "mysql-service"
db_name = "testdb"

#app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"


class Config:
    #SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///projects.db")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas

config = {
    'default': Config,
    'testing': TestingConfig
}