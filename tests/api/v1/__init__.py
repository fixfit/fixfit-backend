from flask.ext.testing import TestCase

from fixfit import create_application, db
from fixfit.models.user import User

from faker import Factory
fake = Factory.create()
import json

API_V1_PREFIX = '/api/v1'

class ApiTestCase(TestCase):

    def create_app(self):
        self.app = create_application('testing')
        return self.app

    def setUp(self):
        with self.app.app_context():
            db.create_all()
            self.load_data()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def load_data(self):

        # Add user
        # self.users = [
        #     {
        #         'first_name'  : fake.first_name(),
        #         'last_name'   : fake.last_name(),
        #         'email'       : fake.email(),
        #         'password'    : fake.password(),
        #         'phone_number': fake.phone_number(),
        #         'profile_pic' : fake.image_url(),
        #         'location'    : fake.address(),
        #     },
        #     {
        #         'first_name'  : fake.first_name(),
        #         'last_name'   : fake.last_name(),
        #         'email'       : fake.email(),
        #         'password'    : fake.password(),
        #         'phone_number': fake.phone_number(),
        #         'profile_pic' : fake.image_url(),
        #         'location'    : fake.address(),
        #     },
        #     {
        #         'first_name'  : fake.first_name(),
        #         'last_name'   : fake.last_name(),
        #         'email'       : fake.email(),
        #         'password'    : fake.password(),
        #         'phone_number': fake.phone_number(),
        #         'profile_pic' : fake.image_url(),
        #         'location'    : fake.address(),
        #     },
        # ]
        #
        # for user in self.users:
        db.session.add(User(email='trainee@test.com', password='haha'))
        db.session.add(User(email='trainer@test.com', password='haha'))
        db.session.commit()

    def get_headers_with_auth(self, username, password):
        response = self.client.post(
            '{}/auth'.format(API_V1_PREFIX),
            data=json.dumps({
                'username': username,
                'password': password
            })
        )
        return {
            'Authorization': 'Bearer ' + response.json['token'],
            'Content-Type': 'application/json'
        }

