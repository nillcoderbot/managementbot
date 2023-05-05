class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "17273188"
    API_HASH = "a2e5bb2b69d13ba7553941af16cc2d5b"

    CASH_API_KEY = "5LM757IEFP878M5I"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://yashu:yashu@cluster0.6ntqt2r.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/a058e18153b55d10c03f5.jpg"

    SUPPORT_CHAT = "night_talks_m"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "BPKZO6L9XVL8"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5538947006  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = [5538947006]  # List of groups that you want blacklisted.
    DRAGONS = [5538947006]  # User id of sudo users
    DEV_USERS = [5538947006]  # User id of dev users
    DEMONS = [5538947006]  # User id of support users
    TIGERS = [5538947006]  # User id of tiger users
    WOLVES = [5538947006]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
