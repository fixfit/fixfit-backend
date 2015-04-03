
from tests.api.v1 import API_V1_PREFIX, ApiTestCase

class UserTestCase(ApiTestCase):

    def test_get_activity(self):
        response = self.client.get(
            '{}/activities'.format(API_V1_PREFIX)
        )
        self.assert200(response)
        activities = [
            doc['name'] for doc in response.json['activities']
        ]
        self.assertTrue('Strength' in activities)
        self.assertTrue('Mountain Climbing' in activities)
        self.assertTrue('Cycling' in activities)
        self.assertTrue('Swimming' in activities)
        self.assertTrue('Running' in activities)
