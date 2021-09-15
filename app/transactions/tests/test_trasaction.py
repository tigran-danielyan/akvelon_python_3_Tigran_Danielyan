from rest_framework.test import APITestCase


class TransactionTestCase(APITestCase):

    def setUp(self):
        self.url = '/transactions/api/v1/transactions/'

    def test_get_user_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

