from sqlalchemy_utils.types.password import PasswordType
from sqlalchemy_utils.types.phone_number import PhoneNumberType
from sqlalchemy.orm import validates
from datetime import datetime

from fixfit import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), default='')
    last_name = db.Column(db.String(50), default='')
    email = db.Column(db.String(256))
    password = db.Column(PasswordType(
        schemes=['pbkdf2_sha512']
    ))
    phone_number = db.Column(PhoneNumberType())
    location = db.Column(db.String(50))
    profile_pic = db.Column(db.Text, default='')
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)

    public_fields = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'location',
        'profile_pic',
        'updated_at',
        'updated_at',
    ]

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email
        return email

    def to_dict(self):
        return dict(
            (k, getattr(self, k)) for k in self.public_fields
        )
