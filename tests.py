from app import db, create_app
from app.models import User
import unittest

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testconfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hash(self):
        u=User(email='test@example.com')
        u.password = 'oNeTwo'
        self.assertTrue(u.verify_password('oNeTwo'))
        self.assertFalse(u.verify_password('TwoOne'))

if __name__ == '__main__':
    unittest.main(verbosity=2)

