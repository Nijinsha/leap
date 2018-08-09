from flask import Flask, request
from leap import leap
import json

app = Flask(__name__)


@app.route('/initialize')
def initialize_leap():
    """Route to initialize leap blockchain.
    If its  the first time this route gets called it will will create the genesis block and do all the initializer
    stuff.
    :return: <json> success. True if the initialization was successful.
    """
    leap.create_leap()
    return json.dumps(dict(success=True))


@app.route('/transaction/create', methods=['POST'])
def create_transaction():
    """Route to create a transaction.
    This route takes a post request with <sender_address> <receiver_address> <amount> as params and publish the
    transaction to all the nodes.
    :return: <json> success. True if the transaction request was successful.
    """
    response = None
    if request.remote_addr == '127.0.0.1':  # Do not allow anyone other than gui wallet of user to request the endpoint
        # or else anyone can initiate a transaction other than user.
        leap.create_transaction(request.data['sender'], request.data['receiver'], request.data['amount'])
        response = "success"
    else:
        response = "Failed! You don't have the right to do that."
    return response


if __name__ == '__main__':
    app.run()
