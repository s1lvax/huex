import json
import requests
import os

class Conbee:
    def __init__(self):
        self.ensure_config_exists()
        self.load_config()

    def ensure_config_exists(self):
        config_path = 'config.json'
        if not os.path.exists(config_path):
            print('Config file does not exist. Creating one...')
            self.create_config(config_path)

    def load_config(self):
        with open('config.json', 'r') as file:
            config_data = json.load(file)
        self.api_key = config_data.get('api_key')
        self.name = config_data.get('name')
        self.gateway = config_data.get('gateway')
        self.port = config_data.get('port')

    def create_config(self, config_path):
        try:
            discover_response = requests.get('https://phoscon.de/discover')
            discover_response.raise_for_status()
            conbee_data = discover_response.json()
            
            if not isinstance(conbee_data, list) or not conbee_data:
                raise ValueError("Received data is not in the expected format.")

            #fill the values from the autodiscover
            config_data = {
                'name': conbee_data[0].get('name'),
                'gateway': conbee_data[0].get('internalipaddress'),
                'port': conbee_data[0].get('internalport', 80) 
            }

            #Generate User's API key
            def wait_for_enter():
                print("Press Enter once you click 'Authenticate App' on your dashboard")
                input()
            
            #wait for user to click the authenticate button
            wait_for_enter()
            api_response_headers = {'Content-Type': 'application/json'}
            api_response_data = { "devicetype": "huex" }
            api_response_url = f"http://{config_data['gateway']}:{config_data['port']}/api"

            #request to create api key
            api_response = requests.post(api_response_url, json=api_response_data, headers=api_response_headers)

            if api_response.ok:
                api_data = api_response.json()
                config_data['api_key'] = api_data[0]['success'].get('username')
                with open(config_path, 'w') as file:
                    json.dump(config_data, file)
                    print(f"Config file created at {config_path}")
            else:
                #print("Error:", api_response.status_code)
                if api_response.status_code == 403:
                    print('The Authenticate App button was not pressed.')

        except requests.RequestException as e:
            print(f"Error retrieving data: {e}")
        except ValueError as e:
            print(f"Data format error: {e}")
        except IOError as e:
            print(f"Error writing to {config_path}")
