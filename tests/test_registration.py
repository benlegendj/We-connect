import unittest
import json
from run import app

class UserAuthClass(unittest.TestCase):

    def test_user_can_register(self):
        self.app = app.test_client()
        response = self.app.post("/user",
                                    data=json.dumps(dict(username="test_user",
                                                    password="testpassword")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)




    def test_user_login(self):
        self.app=app.test_client()
        resp_login=self.app.post("/api/auth/",
                                   data=json.dumps(dict(username="test_username",
                                        password="test_password")),
                                   content_type="application/json")
        self.assertEqual(resp_login.status_code, 200)


    def test_business_registration(self):
        self.app = app.test_client()


if __name__ == '__main__':
    unittest.main()

