import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CETURB_BASE_URL = "https://gvbus-previsao.geocontrol.com.br/pontual-previsao"