import os
from dotenv import load_dotenv

class Settings:

    def __init__(self):
        load_dotenv()

        self.IBGE_URL = os.getenv(
            "IBGE_URL",
            "https://servicodados.ibge.gov.br/api/v1"
        )

        self.TIMEOUT = 30
        self.MAX_RETRIES = 3