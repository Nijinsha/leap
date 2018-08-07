import time
import hashlib
import json
import pickle


class Block(object):
    """Blueprint of a single block in the blockchain.

    """

    def __init__(self, index, previous_block_hash, transactions):
        """Constructor to create a block.
                :param index : <int> The index of the block.
                :param previous_block_hash : Hash of the previous block in the chain.
                :param transactions :<List{transaction}> List of transactions to add to the block.
                """
        self.index = index
        self.nonce = 0
        self.previous_block_hash = previous_block_hash
        self.transactions = transactions
        self.time = time.time()

    # TODO: Should this be static or class method??
    @staticmethod
    def get_block_hash(index):
        """Method to get the has of the block.
            :param index : <int> index of the block in the chain.
            :return : hash of the block.
        """
        # TODO: Require implementation
        pass

    # TODO: Should this be static or class method??
    @staticmethod
    def generate_genesis_block(index):
        return Block(index=0, previous_block_hash=0, transactions=None)

    @property
    def hash_block(self):
        """Method the hash the block.
        This method takes in the block and coverts it into an hashable form and returns the hash.
        """
        # TODO : Refactor the algorithm and improve it. This method only does basic things
        block_string = pickle.dumps(self)
        block_hash = hashlib.sha3_256(block_string).digest()
        # The above lines converts the object into __str__() representation and hashes it using sha3_256 algorithm.
        return block_hash
