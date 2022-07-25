
from trezor import wire
#from trezor.messages import MessageType
from trezor.log import info;

from apps.common.paths import PATTERN_BIP44


#wire.add(MessageType.MobilecoinGetSubaddress, apps.mobilecoin, "get_subaddress")

CURVE = "ed25519"
SLIP44_ID = 866
PATTERN = PATTERN_BIP44

def boot() -> None:
    info("booting mobilecoin app")


    pass

