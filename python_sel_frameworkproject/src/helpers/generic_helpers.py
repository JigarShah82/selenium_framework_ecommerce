import string
import random
import logging as logger


def generic_random_email_pwd(domain=None, email_prefix=None):

    if not domain:
        domain = 'testdomain.com'
    if not email_prefix:
        email_prefix = 'testuser'

    email_str_len = 10
    random_string = ''.join(random.choices(string.ascii_letters, k=email_str_len))
    email = email_prefix + '_' + random_string + '@' + domain
    logger.info(f"generated random email: {email}")

    pwd_str_len = 20
    random_pwd_str = ''.join(random.choices(string.ascii_letters, k=pwd_str_len))

    random_email_pwd = {"email": email, "password": random_pwd_str}
    return random_email_pwd


