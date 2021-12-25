import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import NumberParseException, PhoneNumberFormat


class PhoneNumber:
    def __init__(self, phonenumber: str):
        self.number = phonenumber

    def _parse(self):
        return phonenumbers.parse(self.number)

    def _international(self, parsed):
        return phonenumbers.format_number(parsed, PhoneNumberFormat.INTERNATIONAL)

    def _geolocation(self, parsed) -> str:
        return geocoder.description_for_number(parsed, 'en')

    def info(self) -> dict:
        try:
            info = {}
            parsed = self._parse()
            if phonenumbers.is_valid_number(parsed):
                info['International format'] = self._international(parsed)
                info['Is valid'] = 'Yes'
                info['Country code'] = parsed.country_code
                info['National number'] = parsed.national_number
                info['Geolocation'] = self._geolocation(parsed)
                info['Carrier'] = carrier.name_for_number(parsed, 'en')
                info['Posible timezones'] = str(timezone.time_zones_for_number(parsed))
            else:
                info['Number'] = self.number
                info['Is valid'] = 'No'
            return info
        except NumberParseException as e:
            return {'Number': self.number, 'Message': str(e)}