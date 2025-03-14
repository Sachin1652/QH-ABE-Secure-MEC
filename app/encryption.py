from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.toolbox.symcrypto import SymmetricCryptoAbstraction

group = PairingGroup("SS512")

def encrypt_data(data):
    key = group.random(GT)
    cipher = SymmetricCryptoAbstraction(group.hash(key))
    encrypted = cipher.encrypt(data.encode())
    return encrypted.hex()