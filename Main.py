from client import client
from key import token


# To load new modules, copy/paste the line below, uncommented, with X filled in for the name of your file
# from modules import X

from modules import _debug
from modules import about
from modules import emoji_stats
from modules import exec
from modules import exit
from modules import info
from modules import markov
from modules import message_log
from modules import morse
from modules import music
from modules import nou
from modules import ntp
from modules import ping
from modules import pingreact
from modules import stats
from modules import time
from modules import units
from modules import uwu

client.run(token)
