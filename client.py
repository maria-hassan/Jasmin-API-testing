import requests


def get_data(sender, to, smscNetworkId, msg, smscEncoding, exposureLayerData, ignoreUsernameValidationKey):
    url = "http://93.189.103.72:5001/mobicents/sendSms"
    params = {
        'sender': sender,
        'to': to,
        'smscNetworkId': smscNetworkId,
        'msg': msg,
        'smscEncoding': smscEncoding,
        'exposureLayerData': exposureLayerData,
        'ignoreUsernameValidationKey': ignoreUsernameValidationKey
    }
    try:
        response = requests.get(url, params=params)
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error Occured:{e}")
        return None


if __name__ == "__main__":
    sender = 'travel'
    to = '966539558341'
    smscNetworkId = '20509'
    msg = 'TestMessage-2024-09-19 08:23:32.669157'
    smscEncoding = 'GSM7'
    exposureLayerData = '5205329201:6986399764:796:6801773949:46:be436437-072e-4648-97d6-39f6eb4f6f7d:2451136746:5724:1726734212669025:1726734212670025:1726734212671025'
    ignoreUsernameValidationKey = 'a8yx136b139x1b2bn'
    result = get_data(sender, to, smscNetworkId, msg, smscEncoding, exposureLayerData, ignoreUsernameValidationKey)

    if result:
        print(result)
    else:
        print("Nothing received")
