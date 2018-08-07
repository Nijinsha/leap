class Blockchain(object):
    """Blueprint of the blockchain object.
    """
    def __init__(self):
        """Constructor to create a blockchain object.
        """
        self.chain = []
        self.unspent_transactions = []
        self.current_block_hash = None

    def add_block_to_chain(self, block):
        """Method to add a block to the chain.
        """
        self.chain.append(block)