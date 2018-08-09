def is_request_from_secure_wallet(request):
    """Check if the request if from the client wallet itself and not from somewhere else.
    :return: <Boolean>
    """
    value = False
    if request.remote_addr == '127.0.0.1':
        value = True
    return value
