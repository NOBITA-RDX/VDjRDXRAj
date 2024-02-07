from VDjRDXMUSIC.core.bot import RDX
from VDjRDXMUSIC.core.dir import dirr
from VDjRDXMUSIC.core.git import git
from VDjRDXMUSIC.core.userbot import Userbot
from VDjRDXMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RDX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
