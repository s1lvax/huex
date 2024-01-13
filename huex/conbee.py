import json
import requests
import pkg_resources
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

class Conbee:
    def __init__(self):
        self.config_path = os.path.join(PROJECT_ROOT, 'config.json')
        self.ensure_config_exists()
        self.load_config()

    def ensure_config_exists(self):
        if not os.path.exists(self.config_path):
            print('Config file does not exist. Creating one...')
            self.create_config()

    def load_config(self):
        with open(self.config_path, 'r') as file:
            config_data = json.load(file)
        self.api_key = config_data.get('api_key')
        self.name = config_data.get('name')
        self.gateway = config_data.get('gateway')
        self.port = config_data.get('port')

    def create_config(self):
        try:
            discover_response = requests.get('https://phoscon.de/discover')
            discover_response.raise_for_status()
            conbee_data = discover_response.json()
            
            if not isinstance(conbee_data, list) or not conbee_data:
                raise ValueError("Received data is not in the expected format.")

            config_data = {
                'name': conbee_data[0].get('name'),
                'gateway': conbee_data[0].get('internalipaddress'),
                'port': conbee_data[0].get('internalport', 80) 
            }

            def wait_for_enter():
                print("Press Enter once you click 'Authenticate App' on your dashboard")
                input()

            wait_for_enter()
            api_response_headers = {'Content-Type': 'application/json'}
            api_response_data = {"devicetype": "huex"}
            api_response_url = f"http://{config_data['gateway']}:{config_data['port']}/api"

            api_response = requests.post(api_response_url, json=api_response_data, headers=api_response_headers)

            if api_response.ok:
                api_data = api_response.json()
                config_data['api_key'] = api_data[0]['success'].get('username')
                with open(self.config_path, 'w') as file:
                    json.dump(config_data, file)
                    print(f"Config file created at {self.config_path}")
            else:
                if api_response.status_code == 403:
                    print('The Authenticate App button was not pressed.')

        except requests.RequestException as e:
            print(f"Error retrieving data: {e}")
        except ValueError as e:
            print(f"Data format error: {e}")
        except IOError as e:
            print(f"Error writing to {self.config_path}")

