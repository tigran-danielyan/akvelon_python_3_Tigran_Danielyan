from rest_framework.test import APITestCase


class UserTestCase(APITestCase):

    def setUp(self):
        self.url = '/users/api/v1/users/'

    def test_create_user_with_invalid_data(self):
        self.payload = {"first_name": "John"}
        response = self.client.post(self.url, self.payload)

        self.assertEqual(response.status_code, 400)

    def test_create_user_with_valid_data(self):
        self.payload = {
            "first_name": "John",
            "last_name": "Dohn",
            "email": "JohnDohn@yopmail.com",
        }
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, 201)
        return response

    def test_update_user(self):

        response = self.test_create_user_with_valid_data()
        self.assertEqual(response.status_code, 201)
        user_id = response.json()["id"]

        self.url = f'{self.url}{user_id}/'
        self.payload = {
            "last_name": "Smith",
        }
        response = self.client.patch(self.url, self.payload)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["last_name"], "Smith")

    def test_retrieve(self):
        user_id = self.test_create_user_with_valid_data().json()["id"]
        self.url = f'{self.url}{user_id}/'

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0)

    def test_retrieve_invalid(self):
        user_id = self.test_create_user_with_valid_data().json()["id"] + 1
        self.url = f'{self.url}{user_id}/'

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        user_id = self.test_create_user_with_valid_data().json()["id"]
        self.url = f'{self.url}{user_id}/'
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 200)

    def test_delete_invalid(self):
        user_id = self.test_create_user_with_valid_data().json()["id"] + 1
        self.url = f'{self.url}{user_id}/'
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 404)

    def test_get_user_list(self):
        self.test_create_user_with_valid_data()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0)

