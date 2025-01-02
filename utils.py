import random

import queries

def get_verification_code(email:str):
    code = random.randint(100,9999)
    if queries.get_user_code(email=email,code=code):
        return get_verification_code(email=email)
    return code
