from flask.ext.testing import TestCase

from fixfit import create_application, db
from fixfit.models.user import User

from faker import Factory
fake = Factory.create()
import json

API_V1_PREFIX = '/api/v1'
DEFAULT_PASSWORD = 'haha'

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

        # Add users
        traineeA = User(email='traineeA@test.com', password=DEFAULT_PASSWORD)
        traineeB = User(email='traineeB@test.com', password=DEFAULT_PASSWORD)
        trainerA = User(email='trainerA@test.com', password=DEFAULT_PASSWORD)
        trainerB = User(email='trainerB@test.com', password=DEFAULT_PASSWORD)

        db.session.add(traineeA)
        db.session.add(traineeB)
        db.session.add(trainerA)
        db.session.add(trainerB)
        db.session.commit()

        # Add cards
        # card_by_trainnee = Card(
        #        instructor_id=trainerA.id,
        #        creator_id=traineeA.id,
        #        price=10,
        #        desc='This is a great activity, please join!',
        #        image_url='sample_img_url.jpg',
        #        rating=4,
        #        level='beginner',
        #        title='Yoga Class',
        #        address='902 Clayton Rd',
        #        lat=37.468474,
        #        lng=-78.077783
        # )
        # card_by_trainner = Card(
        #        instructor_id=trainerA.id,
        #        creator_id=trainerA.id,
        #        price=10,
        #        desc='This is a great activity, please join!',
        #        image_url='sample_img_url.jpg',
        #        rating=4,
        #        level='beginner',
        #        title='Yoga Class',
        #        address='902 Clayton Rd',
        #        lat=37.468474,
        #        lng=-78.077783
        # )
        # db.session.add(card_by_trainnee)
        # db.session.add(card_by_trainner)
        # db.session.commit()

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

