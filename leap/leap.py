from leap.blockchain import Blockchain
from leap.block import Block


def create_leap():
    """Method to create the leap blockchain.
    This is the main entry point of the application
    """
    blockchain = Blockchain()
    if check_for_genesis_block(blockchain):
        pass
    else:
        genesis_block = create_genesis_block()
        blockchain.add_block_to_chain(genesis_block)
        genesis_block_hash = genesis_block.hash_block
        setattr(blockchain, "current_block_hash", genesis_block_hash)  # Builtin method to set an attribute value.
    return


def check_for_genesis_block(blockchain):
    """Check if a chain has the genesis block.
    :param blockchain: the blockchain object
    :return: <Boolean> True if the genesis block is found.
    """
    success = True
    if not blockchain.chain:
        print("Blockchain is empty")
        success = False
    return success


def create_genesis_block():
    """Function to create a genesis block (The first block in the chain).
    :return: <Block>
    """
    return Block(index=0, previous_block_hash=0, transactions=None)
