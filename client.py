import json
import logging
import requests

class HttpClient:
    def __init__(self, config_path):
        with open(config_path) as config_file:
            self.config = json.load(config_file)
            self.base_url = self.config['base_url'].rstrip('/')
            self.headers = self.config['headers']
            self.timeout = int(self.headers.pop("timeout", 60))
            self.default_params = self.config['params']

    def make_request(self, endpoint, method='GET', params=None, data=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logging.info(f"Making {method} request to {url} with params: {params or self.default_params}")

        final_params = self.default_params.copy()
        if params:
            final_params.update(params)

        # Make the HTTP request
        if method.upper() == 'GET':
            response = requests.get(url, headers=self.headers, params=final_params, timeout=self.timeout)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=self.headers, json=data, params=final_params, timeout=self.timeout)

        return response.text

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client = HttpClient('config.json')
    response = client.make_request('')
    print(response)
