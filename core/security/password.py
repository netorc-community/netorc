def password_validator(password: str):
    special_characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    if len(password) <= 8:
        return False

    if not any(x.isupper() for x in password):
        return False

    if not any(x.isdigit() for x in password):
        return False

    if not any(x in special_characters for x in password):
        return False

    return True
