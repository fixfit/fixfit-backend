from faker import Factory
import json

from tests.api.v1 import API_V1_PREFIX, ApiTestCase

fake = Factory.create()

class UserTestCase(ApiTestCase):

    def test_create_user(self):
        user = {
            'email': fake.email(),
            'password': fake.password()
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
                'traineeA@test.com',
                'haha'
            )
        )
        self.assert200(response)
        self.assertIsNotNone(response.json)

    def test_delete_user(self):
        self.assert200(
            self.client.get(
                '{}/users/{}'.format(
                    API_V1_PREFIX,
                    1
                )
            )
        )

        response = self.client.delete(
            '{}/users/{}'.format(
                API_V1_PREFIX,
                1
                )
        )
        self.assert200(response)

        self.assert404(
            self.client.get(
                '{}/users/{}'.format(
                    API_V1_PREFIX,
                    1
                )
            )
        )
