from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.common.keychain import Keychain
    from apps.common.paths import Bip32Path

    from trezor.enums import MoneroNetworkType

    from .xmr.crypto import Sc25519
    from .xmr.credentials import AccountCreds


def get_creds(
    keychain: Keychain, address_n: Bip32Path, network_type: MoneroNetworkType
) -> AccountCreds:
    from apps.monero.xmr import monero
    from apps.monero.xmr.credentials import AccountCreds

    node = keychain.derive(address_n)

    key_seed = node.private_key()
    spend_sec, _, view_sec, _ = monero.generate_monero_keys(key_seed)

    creds = AccountCreds.new_wallet(view_sec, spend_sec, network_type)
    return creds


def compute_tx_key(
    spend_key_private: Sc25519,
    tx_prefix_hash: bytes,
    salt: bytes,
    rand_mult_num: Sc25519,
) -> bytes:
    from apps.monero.xmr import crypto

    rand_inp = crypto.sc_add_into(None, spend_key_private, rand_mult_num)
    passwd = crypto.keccak_2hash(crypto.encodeint(rand_inp) + tx_prefix_hash)
    tx_key = crypto.compute_hmac(salt, passwd)
    return tx_key


def compute_enc_key_host(
    view_key_private: Sc25519, tx_prefix_hash: bytes
) -> tuple[bytes, bytes]:
    from apps.monero.xmr import crypto

    salt = crypto.random_bytes(32)
    passwd = crypto.keccak_2hash(crypto.encodeint(view_key_private) + tx_prefix_hash)
    tx_key = crypto.compute_hmac(salt, passwd)
    return tx_key, salt
