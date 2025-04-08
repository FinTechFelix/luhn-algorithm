class LuhnAlgorithm:

    def convert_to_numeric(self, isin):
        result = ""
        
        for char in isin:
            if char.isdigit():
                result += char
            else:
                
                result += str(ord(char) - 55)
        
        return result
        
    def apply_algorithm(self, number):
        
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
        
        numeric_isin = self.convert_to_numeric(isin[:-1])  
        
        check_digit = int(isin[-1])

        calculated_check_digit = (10 - (self.apply_algorithm(numeric_isin) % 10)) % 10
        
        return calculated_check_digit == check_digit

        
# Example usage:

luhn = LuhnAlgorithm()

print(luhn.is_valid_isin("US0378331005"))  # True
print(luhn.is_valid_isin("US0373831005"))  # False
