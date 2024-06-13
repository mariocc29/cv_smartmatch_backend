import os
import sys
import mongoengine

def initialize():
  if 'test' in sys.argv:
    MONGO_DATABASE_NAME = f"{os.getenv('MONGO_DB')}_test"
  else:
    MONGO_DATABASE_NAME = os.getenv('MONGO_DB')

  mongoengine.register_connection('default', db=MONGO_DATABASE_NAME, host=os.getenv('MONGO_HOST'))