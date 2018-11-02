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

    uneeded_dirs = ['word2number-1.1.dist-info','beautifulsoup4-4.6.3.dist-info','bs4-0.0.1.dist-info',
                    'certifi-2018.10.15.dist-info','chardet-3.0.4.dist-info','Click-7.0.dist-info',
                    'Flask-1.0.2.dist-info','gTTS_token-1.1.2.dist-info','gTTS-2.0.1.dist-info',
                    'idna-2.7.dist-info','itsdangerous-1.1.0.dist-info','Jinja2-2.10.dist-info',
                    'MarkupSafe-1.0.dist-info','playsound-1.2.2.dist-info','PyAudio-0.2.11.dist-info',
                    'requests-2.20.0.dist-info','six-1.11.0.dist-info','SpeechRecognition-3.8.1.dist-info',
                    'urllib3-1.24.dist-info','Werkzeug-0.14.1.dist-info','word2number-1.1.dist-info']

    for dirs in uneeded_dirs:
        pass

else:
    print('Make sure to run this script in the Marvin-v3-client folder/directory')
