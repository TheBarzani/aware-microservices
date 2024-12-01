import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DATABASE_NAME = os.getenv("DATABASE_NAME")