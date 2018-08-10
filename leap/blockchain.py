class Blockchain(object):
    """Blueprint of the blockchain object.
    """

    def __init__(self):
        """Constructor to create a blockchain object.
        """
        self.chain = []
        self.unspent_transactions = []
        self.current_block_hash = None
        self.current_block_difficulty = 1

    def add_block_to_chain(self, block):
        """Method to add a block to the chain.
        """
        self.chain.append(block)

    @property
    def get_chain_index(self):
        return len(self.chain)
