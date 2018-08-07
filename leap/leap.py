from leap.blockchain import Blockchain
from leap.block import Block


def create_leap():
    """Method to create the leap blockchain.
    This is the main entry point of the application
    """
    blockchain = Blockchain()
    if check_for_genesis_block():
        pass
    else:
        genesis_block = create_genesis_block()
        append_block_to_blockchain(blockchain,genesis_block)


def check_for_genesis_block():
    """Check if a chain has the genesis block.
    :return: <Boolean> True if the genesis block is found.
    """
    success = True
    if not Blockchain.chain:
        print("Blockchain is empty")
        success = False
    return success


def create_genesis_block():
    """Function to create a genesis block (The first block in the chain).
    :return: <Block>
    """
    return Block(index=0, previous_block_hash=0, transactions=None)


def append_block_to_blockchain(blockchain, block):
    """Function to append the created block to blockchain.
    """
    blockchain.chain.append(block)
    return