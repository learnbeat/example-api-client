import os
import string
import json
import requests
from enum import Enum
from datetime import datetime


class ROUTES(Enum):
    DEFAULT = os.getenv('HOST') + "/traininglists"
    WORDS = os.getenv('HOST') + "/traininglists/{list_id}/words"
    SESSIONS = os.getenv('HOST') + "/traininglists/{list_id}/sessions"
    RESPONSES = os.getenv('HOST') + "/traininglists/{list_id}/session/{session_id}/responses"


class API:
    # Todo: Add the provided token here so you don't have to manually add it on each run
    token = None
    routes = ROUTES
    current_route = None

    def __int__(self):
        return "create object"

    def set_token(self):
        while not self.token:
            self.token = input("Please enter your API token: ")

    def get_routes(self):
        return self.routes

    def get_route_by_index(self, index):
        return list(self.routes)[index].value

    def set_route(self, route):
        self.current_route = route

    def provide_parameters(self):
        parameters = {}
        for option in [t[1] for t in string.Formatter().parse(self.current_route) if t[1] is not None]:
            parameters[option] = input(f"Please provide a value for {option}: ")

        self.update_route_with_parameters(parameters)

    def update_route_with_parameters(self, parameters):
        self.current_route = self.current_route.format(**parameters)

    def make_request(self):
        header = {'Authorization': 'Bearer ' + self.token}
        response = requests.get(self.current_route, headers=header)

        if response:
            response = response.json()
            timestamp = datetime.now()
            with open(f'responses/{timestamp}.json', 'w') as fp:
                json.dump(response, fp)
            print(f'The request is successfully handled and the response is written to {timestamp}.json\n')
        else:
            print('The response seems empty, did you provide valid parameters?\n')
