from os import getenv
import time 
from dotenv import load_dotenv

load_dotenv()

START_TIME = time.time()

SESSION_NAME = getenv("SESSION_NAME", "BAB1lg2nIBbZvPdl26oOIJFf3fI1_-wFkTc0bETw8OM8ipVgSAaJADM1WyIIDHSCBtiT-kTdEy9qPQ9orw4lywX0njZqucrpGCoh1qaCJ3yV3A99xB1fDlbSMAUCRNvhfgOptHK2Gn9wGkGtl4A_5z86aXnbpM6bTvifqbC_VmOvEix65nMFWLw6qmb9zqPzgtXCKPzFZ5rlRU0dby2_DJi9n3uIBL9MmMNmGlx5qHabTkAjrF1I6iLBqz4CBXublUw0WlvBcmy2eLm1gfeDKU3G1CHf3R15qZgmo0q85V-WAtmtofwAD3HZ7TdfFJo3PHBiWHvozizEvkMcZjsT8OZLchXFSwA")

BOT_TOKEN = getenv("BOT_TOKEN", "1352238235:AAHIX_2SljgPxaIUWG7I3yCNmB2j1rgFmlk")

BOT_NAME = getenv("BOT_NAME", "SASKBOT")

OWNER_ID = int(getenv("OWNER_ID", "1360358971")) 

UBOT_ID = int(getenv("BOT_ID","1352238235"))

START_PIC = getenv("START_PIC", "https://telegra.ph/file/9c64c9d589ebfc8e56ce5.jpg")

PLAY_PIC = getenv("PLAY_PIC", "https://telegra.ph/file/9c64c9d589ebfc8e56ce5.jpg")

API_ID = int(getenv("API_ID", "7093984"))

API_HASH = getenv("API_HASH", '645227d5c2f9e55ba614a6c88ac2e6fd')

BOT_USERNAME = getenv("BOT_USERNAME", "SASKBOT")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

SUMMONER = getenv('SUMMONER', 'False')

PROXY = getenv('PROXY')

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1360358971").split()))
SUDO_USERS.append(1360358971)
  
