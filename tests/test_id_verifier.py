from django.test import TestCase

from client.forms.create_client_form import CreateClientForm
from client.utils import id_verifier
from client.utils.id_verifier import IdVerifier

class CreateClientFormTest(TestCase):
    def test_is_valid_id_number_valid_id(self):
        id = '9301225151086'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), True
        )
    
    def test_is_valid_id_number_invalid_month(self):
        id = '9313225151086'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), False
        )

    def test_is_valid_id_number_invalid_day(self):
        id = '9302325151086'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), False
        )
    
    def test_is_valid_id_number_too_few_numbers(self):
        id = '93012251510'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), False
        )
    
    def test_is_valid_id_number_too_many_numbers(self):
        id = '930122515108632'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), False
        )
    
    def test_is_valid_id_number_leap_year(self):
        id = '1202295151089'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), True
        )
    
    def test_is_valid_id_number_empty_number(self):
        id = ''

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), False
        )
    
    def test_is_valid_id_number_non_numeric_char(self):
        id = '9301225a51086'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), False
        )
    
    def test_is_valid_id_number_citizenship_digit_wrong(self):
        id = '9301225151286'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), False
        )

    def test_is_valid_id_number_confirmation_digit_wrong(self):
        id = '9301225151046'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), False
        )

    def test_is_valid_id_number_invalid_luhn_digit(self):
        id = '9301225151082'

        id_verifier = IdVerifier()

        self.assertEqual(
            id_verifier.is_valid_id_number(id), False
        )
