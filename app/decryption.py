from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.toolbox.symcrypto import SymmetricCryptoAbstraction

group = PairingGroup("SS512")

def decrypt_data(encrypted_hex):
    key = group.random(GT)  # In a real implementation, securely store/retrieve the key
    cipher = SymmetricCryptoAbstraction(group.hash(key))
    decrypted = cipher.decrypt(bytes.fromhex(encrypted_hex))
    return decrypted.decode()