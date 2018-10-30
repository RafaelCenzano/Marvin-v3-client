#Imports
from os import path, mkdir
from os import system as terminal
import json

if __name__ == '__main__' and path.isfile('app.py') and path.isfile('requirements.txt') and path.isfile('marvin-env/site-packages/__init__.py'):

    try:

        try:
            mkdir('marvin-data')
        except FileExistsError:
            print('Error marvin-data folder exists already might interfere with marvin data')

        contacts_path = path.join('data','contacts.json')
        settings_path = path.join('data','settings.json')
        contact_data = {"contacts":{},"nicks":{}}
        settings_data = {"settings":{"voice":"female","UI":"enabled"}}

        with open(settings_path, 'w') as newfile:
            json.dump(settings_data, newfile)
        with open(contacts_path, 'w') as newfile1:
            json.dump(contact_data, newfile1)

    except Exception as e:
        print('We ran into a problem\nPlease report this issue ' + str(e) + '\nFiles couldn\'t be created properly')

    try:
        terminal('pip install -r requirements.txt -t marvin-env/site-packages/ --upgrade')
    except Exception as e:
        print('We ran into a problem\nPlease report this issue ' + str(e) + '\nFiles couldn\'t be installed properly')

else:
    print('Make sure to run this script in the Marvin-v3-client folder/directory')
