from config.settings.base import *
from decouple import config

DEBUG = config("DEBUG")
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "../", "staticfiles")
