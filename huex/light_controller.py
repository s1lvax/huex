from prettytable import PrettyTable
import requests

class LightController:
    def __init__(self, conbee):
        self.conbee = conbee
        self.api_url = f'http://{conbee.gateway}:{conbee.port}/api/{conbee.api_key}'

    def show_all_lights(self):
        show_all_request = f'{self.api_url}/lights'
        response = requests.get(show_all_request)

        if response.ok:
            lights_data = response.json()
            self.format_and_print_lights(lights_data)
        else:
            print("Failed to retrieve lights data:", response.status_code)

    #format using prettytable
    def format_and_print_lights(self, lights_data):
        table = PrettyTable()
        table.field_names = ['ID', 'Device name', 'MAC', 'State']
        table.align = 'l'

        for light_id, light_info in lights_data.items():
            name = light_info.get('name')
            unique_id = light_info.get('uniqueid')
            color = '\033[92m●\033[0m' if light_info['state'].get('on') else '\033[91m●\033[0m'
            table.add_row([light_id, name, unique_id, color])

        print(table)

    def control_light(self, light_id, action):
        control_request = f'{self.api_url}/lights/{light_id}/state'
        control_response_headers = {'Content-Type': 'application/json'}
        if(action == 'on'):
            control_response_data = { "on": True }
        else:
            control_response_data = { "on": False }

        #request to create api key
        control_response = requests.put(control_request, json=control_response_data, headers=control_response_headers)

        if control_response.ok:
            print('Changed')
        else:
            print("Couldn't change the state of this light")
