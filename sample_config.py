from dotenv import load_dotenv

ENV = True # make it false for heruko
load_dotenv("config.env")

# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages

if not ENV:
  bot_token = "16901971:AAFqdM_SQE1PB2P1xLr67k"
  ARQ_API_KEY = "Get this from @ARQRobot"
  LANGUAGE = "en"
  ID = 6 # your api id
  HASH = "" # your apihash
  # Leave it as it is
  ARQ_API_BASE_URL = "https://grambuilders.tech"
else:
  from os import environ
  bot_token = str(environ.get("TOKEN", None))
  ARQ_API_KEY = str(environ.get("ARQ_API_KEY", None))
  LANGUAGE = str(environ.get("LANGUAGE", "en"))
  ID = int(environ.get("ID", 6)) # your api id
  HASH = str(environ.get("HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")) # your apihash
  # Leave it as it is
  ARQ_API_BASE_URL = str(environ.get("ARQ_API_BASE_URL", None))
