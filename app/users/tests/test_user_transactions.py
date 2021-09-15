from rest_framework.test import APITestCase


class UserTransactionsTestCase(APITestCase):

    def create_mock_user(self):
        payload = {
            "first_name": "John",
            "last_name": "Dohn",
            "email": "John_Dohn@yopmail.com"
        }
        url = '/users/api/v1/users/'
        response = self.client.post(url, payload)
        return response

    def setUp(self):
        self.user_id = self.create_mock_user().json()['id']
        self.transaction_url = f'/users/api/v1/users/{self.user_id}/transactions/'

    def test_transaction_create_with_valid_data(self):
        payload = {
            "amount": 500.55,
            "user": self.user_id,
            "method": 0
        }

        response = self.client.post(self.transaction_url, payload)
        self.assertEqual(response.status_code, 201)

        return response.json()['id']

    def test_transaction_create_with_invalid_data(self):
        payload = {
            "amount": -500.55,
            "user": self.user_id,
            "method": 0
        }

        response = self.client.post(self.transaction_url, payload)
        self.assertEqual(response.status_code, 400)

    def test_transaction_update_with_negative_amount(self):
        transaction_id = self.test_transaction_create_with_valid_data()
        url = f'{self.transaction_url}{transaction_id}/'
        payload = {
            "amount": -500.55,
        }
        response = self.client.patch(url, payload)

        self.assertEqual(response.status_code, 400)

    def test_transaction_retrieve(self):
        transaction_id = self.test_transaction_create_with_valid_data()
        url = f'{self.transaction_url}{transaction_id}/'

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0)

    def test_delete(self):
        transaction_id = self.test_transaction_create_with_valid_data()
        url = f'{self.transaction_url}{transaction_id}/'

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)

    def test_get_user_list(self):
        grouped_transaction_url = f'/users/api/v1/users/{self.user_id}/grouped-transactions/'
        response = self.client.get(grouped_transaction_url)
        self.assertEqual(response.status_code, 200)
