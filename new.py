import time

import requests
from tqdm import tqdm

BASE_URL = 'http://127.0.0.1:1401/mobicents/sendSms?'


def create_request(camp_id):
    sender = 'travel'
    username = 'jasmin_username'
    password = 'jasmin_password'
    to = '966539558341'
    smscNetworkId = '20509'
    msg = 'TestMessage-2024-09-19+08% 3A23%3A32.669157'
    dlr = 'yes'
    smscEncoding = 'GSM7'
    exposureLayerData = '5205329201% 3A6986399764%3A796%3A6801773949%3A46%3Abe436437-072e-4648-97d6-39f6eb4f6f7d'
    '%3A2451136746%3A5724%3A1726734212669025%3A1726734212670025%3A1726734212671025'

    ignoreUsernameValidationKey = 'a8yx136b139x1b2bn'
    check_duplication = 'False'
    return (f'{BASE_URL}sender={sender}&username={username}&' \
            f'password={password}&to={to}&smscNetworkId={smscNetworkId}&' \
            f'msg={msg}&smscEncoding={smscEncoding}&' \
            f'exposureLayerData={exposureLayerData}&' \
            f'ignoreUsernameValidationKey={ignoreUsernameValidationKey}&' \
            f'dlr={dlr}&' \
            f'check_duplication={check_duplication}')


def send_requests(number_of_requests):
    for i in tqdm(range(number_of_requests)):
        if i % 50 == 0:
            i = ''
        http_request = create_request(i)
        requests.get(http_request)
    # while True:
    #     http_request = create_request()
    #     requests.get(http_request)
    #     time.sleep(300)


if __name__ == '__main__':
    send_requests(101)
