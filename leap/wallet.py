import ecdsa
# TODO : May be converted into a class file


def generate__key_pair():
    """Function to generate key pair.
    This function uses ECDSA algorithm to generate a public/private key pair.
    :return: <Boolean> True if the generation was successful.
    """
    success = True
    try:
        private_key = ecdsa.SigningKey.generate()
        public_key = private_key.get_verifying_key()
        success = save_key_pair(private_key, public_key)
    except RuntimeError:
        print("Could not create key/pair or save them to file.")
        success = False
    return success


def get_private_key():
    """Read the ECDSA private key from the file.
    :return: private key.
    """
    return ecdsa.SigningKey.from_pem(open("data/private.pem").read())


def get_public_key():
    """Read the ECDSA public key from the file.
    :return: public key.
    """
    return ecdsa.VerifyingKey.from_pem(open("data/public.pem").read())


def save_key_pair(private_key, public_key):
    """Function to save the public and private key created for the wallet to disk.
    :param private_key: The generated private key.
    :param public_key: The public key obtained from private key.
    :return: <Boolean> True if the save was a success.
    """
    success = True
    try:
        open("data/private.pem", "wb").write(private_key.to_pem())
        open("data/public.pem", "wb").write(public_key.to_pem())
    except RuntimeError:
        print("Something went wrong while writing the key pair to disk.")
        success = False
    return success
