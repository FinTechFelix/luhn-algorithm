import unittest

from luhn import LuhnAlgorithm


class IsValidIsinTests(unittest.TestCase):
    def setUp(self):
        self.luhn = LuhnAlgorithm()

    def test_valid_isins_are_accepted(self):
        for isin in ("US0378331005", "GB0002634946"):
            with self.subTest(isin=isin):
                self.assertTrue(self.luhn.is_valid_isin(isin))

    def test_invalid_checksum_is_rejected(self):
        self.assertFalse(self.luhn.is_valid_isin("US0373831005"))

    def test_non_string_input_returns_false(self):
        values = (
            None,
            123456789012,
            1234.5,
            b"US0378331005",
            ["US0378331005"],
            {"isin": "US0378331005"},
            True,
        )
        for value in values:
            with self.subTest(value=repr(value)):
                self.assertFalse(self.luhn.is_valid_isin(value))

    def test_malformed_input_returns_false(self):
        cases = {
            "empty": "",
            "too short": "US037833100",
            "too long": "US03783310055",
            "check digit must be numeric": "US037833100X",
            "first char must be a letter": "1S0378331005",
            "second char must be a letter": "U10378331005",
            "lowercase": "us0378331005",
            "unicode digit": "US03783310\u0665",
            "unicode letter": "\u00dcS0378331005",
            "internal space": "US 378331005",
            "leading space": " US0378331005",
            "trailing space": "US0378331005 ",
            "trailing newline": "US0378331005\n",
            "leading junk": "X US0378331005",
        }
        for label, value in cases.items():
            with self.subTest(case=label):
                self.assertFalse(self.luhn.is_valid_isin(value))


if __name__ == "__main__":
    unittest.main()
