from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "24325615"))
API_HASH = getenv("API_HASH", "be5835a24d0cdaedc1cd256def4f9957")
BOT_TOKEN = getenv("BOT_TOKEN", "5497887119:AAEACkD_ckbUPBlgnwgVk0wZ5Ufpu9phDW4")
SESSION_NAME = getenv("SESSION_NAME", "BABAWUvUhIkHOcV6iBjqCF3GzZst-X5NY5tAAEvVQ6iBgUjF2lDy3JZ-N-NdNebk2sdTOjzaOSaZ8JCHv0EuP6VvI2ZMTON_fizt1zzZemaHRWZ6WJBrl65t-DCNEFWGn7nMSsY-SKBC9YK0rFkRrK3Glvs1eTz-4HbFTrlXdQd_dOQQjxl88_MsFzmAlkVutrMXvwl_-FRiymh_uTlqqzv011VyGPor93sg_JpU0iYtSBlnzmMUt2PWafOuGT8P8PzT7IcmpplWtNrF198huwvu30EG85EAZ0R6Nk0qCKhPrxlGOWFj8O-E9fZWejZ9I1_v5-xsuvv7EVvE_gWam-_UAAAAAUZPwtIA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "c_l_h")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Gotcar_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "c_l_h")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "w_1_4")

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
