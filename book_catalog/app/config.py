import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@host:port/dbname')
