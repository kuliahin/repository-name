import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_DATABASE_URL') or 'mysql+mysqldb://root:@localhost/emr_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
