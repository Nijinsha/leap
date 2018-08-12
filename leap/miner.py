from leap.block import Block

run_miner = False


def run_mining(blockchain):
    """Function to perform mining operation.
    """
    while run_miner:
        index = blockchain.get_chain_index()
        current_block_hash = blockchain.current_block_hash
        transactions = None  # get_verified_transactions()
        block = Block(index=index, current_block_hash=current_block_hash, transactions=transactions)
        current_block_difficulty = blockchain.current_block_difficulty
        block_difficulty = 0
        while block_difficulty <= current_block_difficulty:
            block.nonce += 1
            block_hash = block.hash_block()
            block_difficulty = calculate_block_difficulty(block_hash)
            print(block_hash)


def get_verified_transactions():
    # TODO : Requires implementation
    return


def calculate_block_difficulty(block_hash):
    """Function to calculate block difficulty.
    """
    hash_binary = convert_hash_to_binary(block_hash)
    leading_zeros_count = hash_binary.index('1')
    return leading_zeros_count


def convert_hash_to_binary(hash_string):
    """Function to convert hash to binary.
    :return: Binary representation of hash string
    """
    hash_binary = ''.join(format(ord(x), 'b') for x in hash_string)
    return hash_binary
