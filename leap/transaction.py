

class Transaction(object):
    """Blueprint of a single transaction in a list of transactions.
    A transaction is a single spent which has a sender, a receiver and a amount.
    """
    def __init__(self, sender, receiver, amount):
        """Constructor to create a transaction object
        :param sender : Address of the sender.
        :param receiver : Address of the receiver.
        :param amount: <int> Amount of coin send in the transaction.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
