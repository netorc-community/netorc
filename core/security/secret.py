def validator(secret: str) -> bool:
    """
    Validates a secret string meets security conditions.

    Args:
        secret: string.

    Returns:
        False, if a condition is not met.
        True, if all conditions are met.

    """

    special_characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    if len(secret) <= 8:
        return False

    if not any(x.isupper() for x in secret):
        return False

    if not any(x.isdigit() for x in secret):
        return False

    if not any(x in special_characters for x in secret):
        return False

    return True
