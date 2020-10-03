from uuid import uuid4

def generate_token():
    """
    this function will generate token for user
    """
    rand_token = uuid4()
    return rand_token