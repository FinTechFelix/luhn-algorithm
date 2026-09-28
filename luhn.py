import re

# A valid ISIN is 12 ASCII characters: a two-letter country code, nine
# alphanumeric characters, and a final decimal check digit.
_ISIN_PATTERN = re.compile(r"^[A-Z]{2}[A-Z0-9]{9}[0-9]$")


class LuhnAlgorithm:

    def convert_to_numeric(self, isin):
        """Translate an uppercase alphanumeric string into decimal digits.

        Letters are expanded using A=10, B=11, ..., Z=35 and digits are kept
        as-is. Callers are expected to pass input that has already been
        validated as uppercase ASCII (see ``is_valid_isin``).
        """
        result = ""

        for char in isin:
            if char.isdigit():
                result += char
            else:

                result += str(ord(char) - 55)

        return result

    def apply_algorithm(self, number):
        """Return the Luhn checksum sum of a string of decimal digits."""
        total = 0
        reverse_digits = number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 0:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total

    def is_valid_isin(self, isin):
        """Return True if ``isin`` is a well-formed ISIN with a correct check digit.

        Malformed, lowercase, non-ASCII, or non-string input returns ``False``
        rather than raising an exception.
        """
        if not isinstance(isin, str):
            return False

        if _ISIN_PATTERN.fullmatch(isin) is None:
            return False

        numeric_isin = self.convert_to_numeric(isin[:-1])

        check_digit = int(isin[-1])

        calculated_check_digit = (10 - (self.apply_algorithm(numeric_isin) % 10)) % 10

        return calculated_check_digit == check_digit
