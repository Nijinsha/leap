import time
import collections


class Transaction(object):
    """Blueprint of a single transaction in a list of transactions.
    A transaction is a single spent which has a sender, a receiver and a amount.
    """

    def __init__(self, sender, receiver, amount, input_unspent_transactions=None, output_transactions=None):
        """Constructor to create a transaction object.
        :param sender : Address of the sender.
        :param receiver : Address of the receiver.
        :param input_unspent_transactions : <List{unspent transactions}> A list of unspent transactions which is greater
         than the transaction amount. # TODO: The authenticity and validity of this should be verified by the miner when
                                      # TODO:  he receive this transaction.
        :param output_transactions: <List{transactions} A list of output transactions.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.input_unspent_transactions = input_unspent_transactions
        self.output_transactions = output_transactions
        self.timestamp = time.time()

    @property
    def to_ordered_dict(self):
        """Property method to convert the object to a ordered dictionary.
        :return: <Dict{object}> Returns and ordered dictionary of object member variables.
        """
        return collections.OrderedDict(self.__dict__)

    def sign_transaction(self):
        pass

    def calculate_input_unspent_transactions(self):
        """This method create a list of unspent transactions that is greater than the amount transacted.
        :return: <List{unspent transactions}> A list of unspent transactions.
        """
        pass

    def calculate_output_transactions(self, current_miner_fee):
        """Method to create a list of outputs of a transaction.
        :param current_miner_fee: The current miner fee which is obtained from the user or from the last block.
        :return: <List{output transactions}> A list transactions which can be later used by the receiver as
        input for his transaction.
        """
        pass
