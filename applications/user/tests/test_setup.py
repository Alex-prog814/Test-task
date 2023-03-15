from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase

User = get_user_model()


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.transaction_url = reverse("transaction")

        self.user_data1 = {
            "username": "user1",
            "inn": "0987654321",
            "cash_account": "2345.20",
            "password": "test123",
            "password_confirmation": "test123"
        }

        self.correct_transaction_data = {
            "for_users": ["09876543213", "09876543214"],
            "from_user": "09876543212",
            "cash_amount": "1000.00"
        }

        self.incorrect_transaction_data = {
            "for_users": ["094857334", "094857334"],
            "from_user": "0987654321",
            "cash_amount": "50000.00"
        }

        # create users
        self.client = APIClient()
        self.user2 = User(**{
            "username": "user2",
            "inn": "09876543212",
            "cash_account": "5000.20",
            "password": "test124"
        })
        self.user3 = User(**{
            "username": "user3",
            "inn": "09876543213",
            "cash_account": "3000.20",
            "password": "test125"
        })
        self.user4 = User(**{
            "username": "user4",
            "inn": "09876543214",
            "cash_account": "1000.20",
            "password": "test126"
        })
        self.user2.save()
        self.user3.save()
        self.user4.save()

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
