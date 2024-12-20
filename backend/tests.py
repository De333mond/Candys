from django.contrib.auth.models import User
from django.test import TestCase

from backend.models import Customer, BirthDateValidation, UserValidator, AddressValidation
from datetime import date


class UserValidatorTests(TestCase):

    def setUp(self):
        # Create a user instance first
        user = User.objects.create_user(username="testuser", password="password123")

        # Create a Customer instance for the user
        self.user = Customer.objects.create(
            user=user,
            birthdate=date(2000, 5, 15),  # 24 years old
            delivery_adress="123 Main St",
            get_emails=True
        )

    def test_birthdate_validation_valid(self):
        # Test for a valid birthdate (age between 16 and 60)
        birthdate_validation = BirthDateValidation()
        self.assertTrue(birthdate_validation.is_valid(self.user))

    def test_birthdate_validation_invalid_underage(self):
        # Test for an underage user (age under 16)
        self.user.birthdate = date(2009, 5, 15)  # 15 years old
        self.user.save()

        birthdate_validation = BirthDateValidation()
        self.assertFalse(birthdate_validation.is_valid(self.user))

    def test_birthdate_validation_invalid_overage(self):
        # Test for an overage user (age over 60)
        self.user.birthdate = date(1963, 5, 15)  # 61 years old
        self.user.save()

        birthdate_validation = BirthDateValidation()
        self.assertFalse(birthdate_validation.is_valid(self.user))


