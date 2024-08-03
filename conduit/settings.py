from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class _Settings(BaseSettings):
    def __new__(cls):

        load_dotenv()
        return super().__new__(cls)

    PORT: int

SETTINGS  = _Settings()