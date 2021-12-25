from typing import Any
from app.phoneinfo import PhoneNumber

def exists_all_field_names(fields: list[str], d: dict[str, Any]) -> bool:
    for field in fields:
        if field not in d:
            return False

    return True

def test_valid_phonenumber():
    valid_number = '+16469804741'
    fields = (
        'International format',
        'Is valid',
        'Country code',
        'National number',
        'Geolocation',
        'Carrier',
        'Posible timezones'
    )
    phonenumber = PhoneNumber(valid_number)

    assert exists_all_field_names(fields, phonenumber.info())


def test_invalid_phonenumber():
    invalid_number = '+959325'
    fields = (
        'Number',
        'Is valid'
    )
    phonenumber = PhoneNumber(invalid_number)
    phone_info = phonenumber.info()
    assert exists_all_field_names(fields, phone_info) and phone_info['Is valid'] == 'No'


def test_no_phonenumber():
    bad_string = 'lkshdugvsdkjv'
    fields = (
        'Number',
        'Message'
    )
    phonenumber = PhoneNumber(bad_string)
    assert exists_all_field_names(fields, phonenumber.info())
