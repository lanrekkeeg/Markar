from uuid import uuid4
import re
def generate_token():
    """
    this function will generate token for user
    """
    rand_token = uuid4()
    return rand_token

def convert_into_email(roll_no):
    """
    this will convert p15-6058 into p156058@nu.edu.pk

    TODO: validation of roll no required
    """
    roll_clean = re.sub(r"-", "", roll_no)
    email = roll_clean+"@nu.edu.pk"
    return email
