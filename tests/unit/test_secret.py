from core.security.secret import validator


def test_should_return_true_for_validator():
    secret = "NetORC123!"  # Contains one uppercase, number and special character, and is len > 8
    assert validator(secret) is True


def test_should_return_false_for_str_len_less_than_or_equal_to_eight():
    secret = "12345678"
    assert validator(secret) is False


def test_should_return_false_for_str_with_no_uppercase_characters():
    secret = "123456789"
    assert validator(secret) is False


def test_should_return_false_for_str_with_no_digits_characters():
    secret = "OneTwoThreeFourFiveSixSevenEightNine"
    assert validator(secret) is False


def test_should_return_false_for_str_with_no_special_characters():
    secret = "One2Three4Five6Seven8Nine"
    assert validator(secret) is False
