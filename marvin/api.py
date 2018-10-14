from requests import get
from marvin.essentials import speak


#########################
# File to hold Api work #
#########################


class ApiService():
    def __init__(speak_type):
        self.speak_type = speak_type

    def defineAPI(self, definition):
        url = ('https://marvin-api-server.herokuapp.com/definition/' + definition)
        self.requested_definition = get(url)
        print('Retrieving Definition')
        if self.requested_definition.json()['definition'] is not None:
            definition_found = self.requested_taco.json()['definition']
            type = self.requested_taco.json()['type']
            speak(definition + ' is a ' + type + '\nThe definition is ' + 'definition_found', self.speak_type)
