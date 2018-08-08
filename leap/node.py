from flask import Flask
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
    request_data = request.getjson()
    return json.dumps(request_data)


if __name__ == '__main__':
    app.run()
