# Luhn Algorithm Validator

This repository provides a Python implementation of the **Luhn Algorithm**, commonly used to validate identification numbers such as **ISINs** (International Securities Identification Numbers), credit card numbers, and other identifiers.

## 🔍 What It Does

The `LuhnAlgorithm` class in `luhn.py` can:

- Convert alphanumeric ISINs into numeric form.
- Apply the Luhn algorithm to the numeric string.
- Validate the final check digit of an ISIN.

## 🧠 How It Works

The Luhn check digit is calculated by:
1. Converting the ISIN into a numeric string:
   - Letters are replaced by numbers (A=10, B=11, ..., Z=35).
2. Reversing the numeric string and applying the Luhn algorithm:
   - Every second digit is doubled, subtracting 9 if the result exceeds 9.
3. Summing the results and checking that the total modulo 10 equals zero.

## 🧪 Example Usage

```python
from luhn import LuhnAlgorithm

luhn = LuhnAlgorithm()

# Valid ISIN
print(luhn.is_valid_isin("US0378331005"))  # Output: True

# Invalid ISIN
print(luhn.is_valid_isin("US0373831005"))  # Output: False
