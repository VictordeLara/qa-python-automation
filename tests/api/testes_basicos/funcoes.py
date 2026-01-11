def email_valido(email):
    return "@" in email and "." in email


def divdir(a,b):
    if b == 0 :
        return None
    return a / b