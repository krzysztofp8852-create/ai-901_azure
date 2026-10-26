"""Sprawdza środowisko labów AI-901: pakiety, plik .env i logowanie do Azure."""

import logging
import os

from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

logging.getLogger("azure.identity").setLevel(logging.CRITICAL)
load_dotenv()

for name in ("PROJECT_ENDPOINT", "MODEL_DEPLOYMENT_NAME"):
    status = "ustawione" if os.getenv(name) else "BRAK (uzupełnij .env)"
    print(f"{name}: {status}")

try:
    DefaultAzureCredential().get_token("https://ai.azure.com/.default")
    print("Logowanie do Azure: OK")
except Exception as e:
    print(f"Logowanie do Azure: nie działa ({type(e).__name__}). Uruchom `az login`.")
