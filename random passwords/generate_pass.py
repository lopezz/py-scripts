"""
Generate a random password based of the lenght specified
optional arguments can be passed to specify the use of
different sets of characters.
"""
import random
import string

def generate_pass(lenght=8, lower=True, upper=True, digits=True, special=True):
    """Returns a random password based of the lenght specified

    Optional arguments:
    lentght -- the lenght of the password, defaults to 8.
    lower -- Use lowercase characters.
    upper -- Use upper characters.
    digits -- Use numbers.
    special -- Use special characters (such as '?*+{}...')
    """
    lowercase = string.ascii_lowercase if lower else ''
    uppercase = string.ascii_uppercase if upper else ''
    digit_chars = string.digits if digits else ''
    special_chars = string.punctuation if special else ''
    alphabet = lowercase + uppercase + digit_chars + special_chars
    if alphabet != '':
        try:
            return ''.join(random.SystemRandom().sample(alphabet, lenght))
        # SystemRandom() uses os.urandom(), this is not available in all systems
        # If a randomness source is not found, NotImplementedError will be raised.
        except NotImplementedError:
            return ''.join(random.sample(alphabet, lenght))
    else:
        raise Exception('There must be at least one true value')
