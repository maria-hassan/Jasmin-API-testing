import unittest
from client import get_data
from unittest.mock import patch, MagicMock
import requests


class Test_get_data(unittest.TestCase):

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = 'sucessful'
        mock_response.text = 'Successful Response'
        mock_get.return_value = mock_response
        test_response='Error “Argument [to] has an invalid value: [966505246009aaa].”'

        result = get_data(
            sender='travel',
            to='966539558341',
            smscNetworkId='20509',
            msg='TestMessage-2024-09-19 08:23:32.669157',
            smscEncoding='GSM7',
            exposureLayerData='5205329201:6986399764:796:6801773949:46:be436437-072e-4648-97d6-39f6eb4f6f7d:2451136746:5724:1726734212669025:1726734212670025:1726734212671025',
            ignoreUsernameValidationKey='a8yx136b139x1b2bn'
        )


        mock_get.assert_called_once_with(
            "http://93.189.103.72:5001/mobicents/sendSms",
            params={
                'sender': 'travel',
                'to': '966539558341',
                'smscNetworkId': '20509',
                'msg': 'TestMessage-2024-09-19 08:23:32.669157',
                'smscEncoding': 'GSM7',
                'exposureLayerData': '5205329201:6986399764:796:6801773949:46:be436437-072e-4648-97d6-39f6eb4f6f7d:2451136746:5724:1726734212669025:1726734212670025:1726734212671025',
                'ignoreUsernameValidationKey': 'a8yx136b139x1b2bn'
            }
        )


        self.assertEqual(result, 'Successful Response')

    @patch('requests.get')
    def test_get_data_failure_clienterror(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
        #mock_response.content='Client Error'
        mock_get.return_value = mock_response

        result = get_data(
            sender="1234",
            to="5678",
            smscNetworkId="1",
            msg="Test Message",
            smscEncoding="GSM",
            exposureLayerData="layer_data",
            ignoreUsernameValidationKey="True"
        )

        mock_get.assert_called_once()
        self.assertIsNone(result)

    @patch('requests.get')
    def test_missing_sender(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = None
        mock_response.content='failed'
        mock_get.return_value = mock_response

        result = get_data(
            sender=None,
            to='966539558341',
            smscNetworkId='20509',
            msg='TestMessage-2024-09-19 08:23:32.669157',
            smscEncoding='GSM7',
            exposureLayerData='5205329201:6986399764:796:6801773949:46:be436437-072e-4648-97d6-39f6eb4f6f7d:2451136746:5724:1726734212669025:1726734212670025:1726734212671025',
            ignoreUsernameValidationKey='a8yx136b139x1b2bn'
        )
        self.assertIsNone(result)

    @patch('requests.get')
    def test_invalid_to_number(self,mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = None
        mock_response.content = 'failed'
        mock_get.return_value = mock_response

        result = get_data(
            sender='travel',
            to='Invalid number',
            smscNetworkId='20509',
            msg='TestMessage-2024-09-19 08:23:32.669157',
            smscEncoding='GSM7',
            exposureLayerData='5205329201:6986399764:796:6801773949:46:be436437-072e-4648-97d6-39f6eb4f6f7d:2451136746:5724:1726734212669025:1726734212670025:1726734212671025',
            ignoreUsernameValidationKey='a8yx136b139x1b2bn'
        )
        self.assertIsNone(result)

    @patch('requests.get')
    def test_missing_smscNetworkId(self,mock_get):
        mock_response=MagicMock()
        mock_response.status_code=400
        mock_response.text=None
        mock_response.content='failed'
        mock_get.return_value=mock_response

        result = get_data(
            sender='travel',
            to='966539558341',
            smscNetworkId=None,
            msg='TestMessage-2024-09-19 08:23:32.669157',
            smscEncoding='GSM7',
            exposureLayerData='5205329201:6986399764:796:6801773949:46:be436437-072e-4648-97d6-39f6eb4f6f7d:2451136746:5724:1726734212669025:1726734212670025:1726734212671025',
            ignoreUsernameValidationKey='a8yx136b139x1b2bn'
        )
        self.assertIsNone(result)

    @patch('requests.get')
    def test_invalid_exposureLayerData(self,mock_get):
        mock_response=MagicMock()
        mock_response.status_code=400
        mock_response.text=None
        mock_response.content='failed'
        mock_get.return_value=mock_response

        result=get_data(
            sender='travel',
            to='966539558341',
            smscNetworkId='20509',
            msg='TestMessage-2024-09-19 08:23:32.669157',
            smscEncoding='GSM7',
            exposureLayerData='5205329201@6986399764@796@6801773949@46@be436437-072e-4648-97d6-39f6eb4f6f7d:2451136746:5724:1726734212669025:1726734212670025:1726734212671025',
            ignoreUsernameValidationKey='a8yx136b139x1b2bn'
        )
        self.assertIsNone(result)

    @patch('requests.get')
    def test_missing_ignoreUsernameValidationKey(self,mock_get):
        mock_response=MagicMock()
        mock_response.status_code=400
        mock_response.text=None
        mock_response.content='failed'
        mock_get.return_value=mock_response

        result = get_data(
            sender='travel',
            to='966539558341',
            smscNetworkId='20509',
            msg='TestMessage-2024-09-19 08:23:32.669157',
            smscEncoding='GSM7',
            exposureLayerData='5205329201@6986399764@796@6801773949@46@be436437-072e-4648-97d6-39f6eb4f6f7d:2451136746:5724:1726734212669025:1726734212670025:1726734212671025',
            ignoreUsernameValidationKey=None
        )
        self.assertIsNone(result)







if __name__ == '__main__':
    unittest.main()
