from datetime import datetime

class IdVerifier():
    def is_valid_id_number(self, id_number: str):
        if not id_number.isdecimal():
            return False

        if len(id_number) != 13:
            return False

        if self._is_date_valid(date=id_number[0:6]) is False:
            return False

        if self._is_citizenship_digit_valid(c_char=id_number[-3]) is False:
            return False

        if self._is_confimation_digit_valid(confirm_char=id_number[-2]) is False:
            return False
        
        if self._is_luhn_valid(id_number=id_number) is False:
            return False
        
        return True
    
    def _is_date_valid(self, date: str):
        '''
        Validates the first 6 bytes to ensure they're a valid date.

        NOTE: A serious pitfall of the SA ID number is the dedication
        of only 6 bytes for the date. The year only gets 2 bytes, 
        omitting the millenium and century.
        I have chosen to rather account for leap years and ommit
        clients over 100 years old using the datetime module which
        will default the millenium to 2000s for values from 00 up to 
        the current year's last two digits.
        '''
        try:
            year = date[0:2]
            month = date[2:4]
            day = date[4:6]
            date = datetime.strptime(f'{year}/{month}/{day}', '%y/%m/%d')
            return True
        except ValueError:
            return False
    
    def _is_citizenship_digit_valid(self, c_char):
        VALID_DIGITS = ('0','1')
        if c_char in VALID_DIGITS:
            return True
        else:
            return False
    
    def _is_confimation_digit_valid(self, confirm_char):
        VALID_DIGITS = ('8','9')
        if confirm_char in VALID_DIGITS:
            return True
        else:
            return False
    
    def _is_luhn_valid(self, id_number):
        if self._luhn_checksum(id_number) is 0:
            return True
        else:
            return False
    
    def _luhn_checksum(self, id_number):
        digits = len(id_number)
        sum = 0
        is_even = False
        
        for digit in range(digits - 1, -1, -1):
            d = ord(id_number[digit]) - ord('0')
        
            if (is_even == True):
                d = d * 2
    
            sum += d // 10
            sum += d % 10
    
            is_even = not is_even
        return sum % 10
