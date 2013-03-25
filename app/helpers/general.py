import string


def check_naive(mystring):
    allowed = string.ascii_letters + string.digits + '_' + '-'
    return all(c in allowed for c in mystring)
