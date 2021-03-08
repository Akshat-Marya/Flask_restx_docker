  
import unittest
import json
import sys
sys.path.append('./')
from app.test.base import BaseTestCase

class TestDataUpload(BaseTestCase):

    def test_house_price_prediction(self):
            """ Test for house price prediction """
            with self.client:
                response = self.client.post(
                    '/api/price',
                    data=json.dumps({'X':[1,2,3,4,5,6,7,8,9,10,11,12,13]}),
                    content_type='application/json'
                )
                self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()