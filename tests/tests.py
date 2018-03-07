import unittest
import json
from run import api,app
class Tests(unittest.TestCase):

    '''def test_get_all(self):
        response = self.app.get('auth/register')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['items']), 3)'''

    def test_invalid_JSON(self):
        """Test status code 405 from improper JSON on post to raw"""
        response = self.api.post('auth/register',
                                data="This isn't a json... it's a string!")
        self.assertEqual(response.status_code, 405)
if __name__ == '__main__':
    unittest.main()


