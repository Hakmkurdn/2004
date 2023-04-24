from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "24325615"))
API_HASH = getenv("API_HASH", "be5835a24d0cdaedc1cd256def4f9957")
BOT_TOKEN = getenv("BOT_TOKEN", "5497887119:AAGLz5H5aprth55WfYZdsfkR0KBNSIk4z8w")
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1wBu6bvBTzYY08lkx4_Sf8BoK51sG-eShFvde2JLUTMjJfYVvjgWvvEo_SbxjuSrxd0KSUWTp6zLYec7_YL74EUk6aCE4lDA9T2hejOJQVLuWRzi5zEmPuireJV6FklNKQyJTs2h55ZHo_ScMBRFESpWtEwxA6hZKmOdFJM9osCl_ZYryIoZYMGMha9nguezpzX8AAl-HBHlSPr3w7SfNQGRJbp2OgtS7VIJFRhIwKm0o6hOnCQcjbi63dxRPE2OE4SUz-vhVaf8ptZ4F3IiSc2QXoVdCwR3FUABc8jcAETWRe5_8nWQGMmkuNt0IBfLoF3KreGv5Jj2vIXDA7pBG94xpc=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "c_l_h")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Gotcar_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "W_1_4")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "W_1_4")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5355696037").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5474599634").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
