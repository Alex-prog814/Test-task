from django.contrib.auth import get_user_model
from applications.user.tests.test_setup import TestSetUp

User = get_user_model()


class TestViews(TestSetUp):
    def test_register_incorrect(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_register_correct(self):
        res = self.client.post(self.register_url, self.user_data1, format="json")
        self.assertEqual(res.status_code, 201)

    def test_user_exist(self):
        res1 = self.client.post(self.register_url, self.user_data1, format="json")
        res2 = self.client.post(self.register_url, self.user_data1, format="json")
        self.assertEqual(res2.status_code, 400)

    def test_transaction_correct(self):
        res = self.client.post(self.transaction_url, self.correct_transaction_data, format="json")
        self.assertEqual(res.status_code, 200)

    def test_transaction_incorrect(self):
        res = self.client.post(self.transaction_url, self.incorrect_transaction_data, format="json")
        self.assertEqual(res.status_code, 400)

    def test_transaction_sender_cash(self):
        start_cash = self.user2.cash_account
        res = self.client.post(self.transaction_url, self.correct_transaction_data, format="json")
        user = User.objects.get(inn=self.correct_transaction_data.get("from_user"))
        finish_cash = float(start_cash)  - float(self.correct_transaction_data.get("cash_amount"))
        self.assertEqual(float(user.cash_account), finish_cash)

    def test_transaction_recipient_cash(self):
        start_cash_user3 = self.user3.cash_account
        start_cash_user4 = self.user4.cash_account
        res = self.client.post(self.transaction_url, self.correct_transaction_data, format="json")
        user3 = User.objects.get(inn=self.user3.inn)
        user4 = User.objects.get(inn=self.user4.inn)
        finish_cash_user3 = float(start_cash_user3) + round(float(self.correct_transaction_data.get("cash_amount")) / len(self.correct_transaction_data.get("for_users")), 2)
        self.assertEqual(float(user3.cash_account), finish_cash_user3)
        finish_cash_user4 = float(start_cash_user4) + round(float(self.correct_transaction_data.get("cash_amount")) / len(self.correct_transaction_data.get("for_users")), 2)
        self.assertEqual(float(user4.cash_account), finish_cash_user4)
