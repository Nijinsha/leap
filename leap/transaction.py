import time


class Transaction(object):
    """Blueprint of a single transaction in a list of transactions.
    A transaction is a single spent which has a sender, a receiver and a amount.
    """

    def __init__(self, sender, receiver, input_unspent_transactions, output_transactions):
        """Constructor to create a transaction object.
        :param sender : Address of the sender.
        :param receiver : Address of the receiver.
        :param input_unspent_transactions : <List{unspent transactions}> A list of unspent transactions which is greater
         than the transaction amount.
        :param output_transactions: <List{transactions} A list of output transactions.
        """
        self.sender = sender
        self.receiver = receiver
        self.input_unspent_transactions = input_unspent_transactions
        self.output_transactions = output_transactions
        self.timestamp = time.time()

    @staticmethod
    def calculate_input_unspent_transactions(amount):
        """This method create a list of unspent transactions that is greater than the amount transacted.
        :param amount: <int> The amount need to be transacted to a receiver.
        :return: <List{unspent transactions}> A list of unspent transactions.
        """
        pass

    @staticmethod
    def calculate_output_transactions(input_unspent_transactions,amount,current_miner_fee):
        """

        :param input_unspent_transactions: <List{unspent transactions}> A list of unspent transactions which is greater
        than the transaction amount.
        :param amount:<int> The amount need to be transacted to a receiver.
        :param current_miner_fee: The current miner fee which is obtained from the user or from the last block.
        :return: <List{output transactions}> A list transactions which can be later used by the receiver as
        input for his transaction
        """
