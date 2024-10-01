import unittest
from client import get_data

class Test_get_data(unittest.TestCase):

    def test_get_data_success(self):
        result = get_data(
            sender='travel',
            to='966539558341',
            smscNetworkId='20509',
            msg='TestMessage-2024-09-19 08:23:32.669157',
            smscEncoding='GSM7',
            exposureLayerData='5205329201:6986399764:796:6801773949:46:be436437-072e-4648-97d6-39f6eb4f6f7d'
                              ':2451136746:5724:1726734212669025:1726734212670025:1726734212671025',
            ignoreUsernameValidationKey='a8yx136b139x1b2bn')

        self.assertIn('Success',result)

    def test_get_data_failure_with_client_error(self):
        result = get_data(
            sender="1234",
            to="5678",
            smscNetworkId="1",
            msg="Test Message",
            smscEncoding="GSM",
            exposureLayerData="layer_data",
            ignoreUsernameValidationKey="True"
        )
        if result is not None:
            self.assertIn("Error \"Parameter exposureLayerData does not have a suitable length\"", result)
        else:
            self.assertIsNone(result)

    def test_get_data_missing_sender(self):
        result = get_data(
            sender=None,
            to='966539558341',
            smscNetworkId='20509',
            msg='TestMessage-2024-09-19 08:23:32.669157',
            smscEncoding='GSM7',
            exposureLayerData='5205329201:6986399764:796:6801773949:46:be436437-072e-4648-97d6-39f6eb4f6f7d:2451136746:5724:1726734212669025:1726734212670025:1726734212671025',
            ignoreUsernameValidationKey='a8yx136b139x1b2bn'
        )
        if result is not None:
            self.assertIn("Error \"Missing mandatory parameter: sender\"", result)
        else:
            self.assertIsNone(result)

    def test_get_data_invalid_invalid_exposureLayerData_length_missing_to_number(self):
        result = get_data(
            sender='travel',
            to='INVALID_NUMBER',
            smscNetworkId='20509',
            msg='TestMessage-2024-09-19 08:23:32.669157',
            smscEncoding='GSM7',
            exposureLayerData='some_data',
            ignoreUsernameValidationKey='a8yx136b139x1b2bn')

        if result is not None:
            self.assertIn("Error \"Parameter exposureLayerData does not have a suitable length\"", result)
        else:
            self.assertIsNone(result)

    def test_get_data_invalid_exposureLayerData_length_missing_smscNetworkId(self):
        result = get_data(
            sender='travel',
            to='966539558341',
            smscNetworkId=None,
            msg='TestMessage',
            smscEncoding='GSM7',
            exposureLayerData='some_data',
            ignoreUsernameValidationKey='valid_key'
        )
        if result is not None:
            self.assertIn("Error \"Parameter exposureLayerData does not have a suitable length\"", result)
        else:
            self.assertIsNone(result)

    def test_get_data_missing_exposureLayerData(self):
        result = get_data(
            sender='travel',
            to='966539558341',
            smscNetworkId='20509',
            msg='TestMessage',
            smscEncoding='GSM7',
            exposureLayerData=None,
            ignoreUsernameValidationKey='valid_key'
        )
        if result is not None:
            self.assertIn("Unknown error: 'el_message_id'", result)
        else:
            self.assertIsNone(result)

    def test_get_data_missing_ignoreUsernameValidationKey(self):
        result = get_data(
            sender='travel',
            to='966539558341',
            smscNetworkId='20509',
            msg='TestMessage',
            smscEncoding='GSM7',
            exposureLayerData='some_data',
            ignoreUsernameValidationKey=None
        )
        if result is not None:
            self.assertIn("Error", result)
        else:
            self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main()
