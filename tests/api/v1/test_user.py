from faker import Factory
import json

from tests.api.v1 import API_V1_PREFIX, ApiTestCase

fake = Factory.create()

class UserTestCase(ApiTestCase):

    def test_create_user(self):
        user = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(),
            'phone_number': fake.phone_number(),
            'profile_pic': fake.image_url(),
            'location': fake.address(),
        }
        resp = self.client.post(
            '{}/users'.format(API_V1_PREFIX),
            data=json.dumps(user)
        )
        self.assert_200(resp)

    def test_users_get(self):
        response = self.client.get(
            '{}/me'.format(API_V1_PREFIX),
            headers=self.get_headers_with_auth(
                'ngoc@zopim.com',
                'haha'
            )
        )
        self.assert200(response)
        print response.json
        self.assertIsNotNone(response.json)
