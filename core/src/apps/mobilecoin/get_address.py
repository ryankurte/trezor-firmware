from typing import TYPE_CHECKING

from trezor import wire
from trezor.messages import MobilecoinSubaddressKeys, RistrettoPoint, RistrettoPrivate
from trezor.ui.layouts import show_address
from trezor.log import info;

from apps.common import paths
from apps.common.keychain import auto_keychain, Keychain

if TYPE_CHECKING:
    from trezor.messages import MobilecoinGetSubaddress

    from apps.common.keychain import Keychain

@auto_keychain(__name__)
async def get_address(
    ctx: wire.Context, msg: MobilecoinGetSubaddress, keychain: Keychain
) -> MobilecoinSubaddressKeys:
    
    await paths.validate_path(ctx, keychain, msg.wallet)

    info("Get subaddress called");

    return MobilecoinSubaddressKeys(msg.wallet, msg.index, RistrettoPrivate, RistrettoPoint)
