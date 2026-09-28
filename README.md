# Luhn Algorithm Validator

This repository provides a Python implementation of the **Luhn Algorithm**, commonly used to validate identification numbers such as **ISINs** (International Securities Identification Numbers), credit card numbers, and other identifiers.

Version: `0.1.0` (provisional; no release has been tagged). This project is licensed under the MIT License (see `LICENSE`).

## 🔍 What It Does

The `LuhnAlgorithm` class in `luhn.py` can:

- Convert alphanumeric ISINs into numeric form.
- Apply the Luhn algorithm to the numeric string.
- Validate the final check digit of an ISIN.

## 📦 Installation

The project uses a `pyproject.toml` with a setuptools build backend and installs the existing top-level `luhn` module, so the import path is unchanged:

```bash
python3 -m pip install .
```

Then import it as before:

```python
from luhn import LuhnAlgorithm
```

## ✅ Behavior

`LuhnAlgorithm.is_valid_isin(isin)` returns `True` only for a syntactically well-formed ISIN whose check digit is correct and returns `False` for everything else instead of raising an exception. Before the checksum is calculated the input must be a `str` that fully matches the ASCII pattern `^[A-Z]{2}[A-Z0-9]{9}[0-9]$` (a two-letter country code, nine uppercase alphanumeric characters, and a final digit). This means non-string input, lowercase letters, Unicode characters/digits, wrong lengths, embedded whitespace, and leading/trailing junk are all rejected.

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

# Invalid ISIN (bad check digit)
print(luhn.is_valid_isin("US0373831005"))  # Output: False

# Malformed input (returns False instead of raising)
print(luhn.is_valid_isin("US037833100X"))  # Output: False
print(luhn.is_valid_isin(None))  # Output: False
```

## 🧪 Tests

The regression tests use only the standard library:

```bash
python3 -m unittest discover -s tests -v
```
