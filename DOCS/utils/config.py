import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    ENDPOINT = os.getenv("ENDPOINT")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")
    KEY = os.getenv("KEY")
