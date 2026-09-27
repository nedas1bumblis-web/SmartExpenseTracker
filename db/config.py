import os
from dotenv import load_dotenv

load_dotenv()

REQUIRED_KEYS = ['pguser', 'pgpassword', 'pghost', 'pgport', 'pgdb']

def get_db_settings() -> dict:
    settings = {key: os.getenv(key.upper()) for key in REQUIRED_KEYS}
    missing = [key for key, value in settings.items() if value is None]
    if missing:
        raise Exception(f'Bad config, missing environment variables: {[k.upper() for k in missing]}')
    return settings