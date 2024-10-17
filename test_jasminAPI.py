import unittest
from client import HttpClient

class Test_get_data(unittest.TestCase):

    def setUp(self):
        self.client=HttpClient('config.json')

    def test_get_data_success(self):
        result = self.client.make_request('')

        self.assertIn('Success',result)

    def test_get_data_failure_with_client_error(self):
        self.client.config['to']='9999'
        result = self.client.make_request('')

        self.assertIn('Success',result)
    def test_get_data_missing_sender(self):
        self.client.config['sender']=''
        result= self.client.make_request('')
        self.assertIn('Success', result)

    def test_invalid_parameter_format(self):
        self.client.config['smscEncoding'] = 'InvalidEncoding'
        result = self.client.make_request('')
        self.assertIn('Success', result)






if __name__ == '__main__':
    unittest.main()
