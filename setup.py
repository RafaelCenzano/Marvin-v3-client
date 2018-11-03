#Imports
from os import path, mkdir, listdir, remove
from os import system as terminal
from json import dump
from platform import system
from shutil import rmtree, move

# Run code if file directly called and app.py, requirements.txt, and __init__.py in marvin-env exists to make many checks that setup.py called in right directory
if __name__ == '__main__' and path.isfile('app.py') and path.isfile('requirements.txt') and path.isfile(path.join('marvin-env','lib','site-packages','__init__.py')):

    try:
        # Make marvin-data directory to store any json and data needed to run marvin
        mkdir('marvin-data')
        print('\nmarvin-data folder created for marvin data\n')

        # If folder exsists prompt user that this can potentially interfere with marvin code
    except FileExistsError:
        print('Error marvin-data folder exists already might interfere with marvin data')

    try:
        # create any os paths for json files
        contacts_path = path.join('marvin-data','contacts.json')
        settings_path = path.join('marvin-data','settings.json')

        # create json data for the json files
        contact_data = {"contacts":{},"nicks":{}}
        settings_data = {"settings":{"voice":"female","UI":"enabled"}}

        # create json files
        with open(settings_path, 'w') as newjsonfile:
            dump(settings_data, newjsonfile)
        print('\nCreate settings.json files')

        with open(contacts_path, 'w') as newjsonfile1:
            dump(contact_data, newjsonfile1)
        print('Create contacts.json files\n')

        # If there is an error when creating data files
    except Exception as e:
        print('We ran into a problem\nPlease report this issue ' + str(e) + '\nFiles couldn\'t be created properly')

    try:
        # install required libraries into marvin-env
        print('\nInstalling needed libraries\n')
        terminal('pip install -r requirements.txt -t ' + path.join('marvin-env','lib','site-packages') + ' --upgrade')

        # dependencies couldn't be installed
    except Exception as e:
        print('We ran into a problem\nPlease report this issue ' + str(e) + '\nFiles couldn\'t be installed properly')

        # make list full of uneeded folders created from pip installs
    uneeded_dirs = ['word2number-1.1.dist-info','beautifulsoup4-4.6.3.dist-info','bs4-0.0.1.dist-info',
                    'certifi-2018.10.15.dist-info','chardet-3.0.4.dist-info','Click-7.0.dist-info',
                    'Flask-1.0.2.dist-info','gTTS_token-1.1.2.dist-info','gTTS-2.0.1.dist-info',
                    'idna-2.7.dist-info','itsdangerous-1.1.0.dist-info','Jinja2-2.10.dist-info',
                    'MarkupSafe-1.0.dist-info','playsound-1.2.2.dist-info','PyAudio-0.2.11.dist-info',
                    'requests-2.20.0.dist-info','six-1.11.0.dist-info','SpeechRecognition-3.8.1.dist-info',
                    'urllib3-1.24.1.dist-info','Werkzeug-0.14.1.dist-info']
    try:
        # for all uneeded folders delete them
        print('\nDeleting uneeded folders\n')
        for dirs in uneeded_dirs:

            # create path to folder to delete
            folder = path.join('marvin-env','lib','site-packages',dirs)

            # remove all files in the directory
            for files in listdir(folder):

                # file path inside folder
                file_path = path.join(folder, files)

                # if file exists delete it
                if path.isfile(file_path):
                    remove(file_path)

                # if dir exists delete it
                elif path.isdir(file_path):
                    rmtree(file_path)

            # finally delete folder
            rmtree(folder)
            print('deleted ' + folder + ' folder')

        # files and folders couln't be deleted
    except Exception as e:
        print('This error occured when trying to remove uneeded folders to save space' + str(e) + '. If this a problem please report the error to the github repository')

    source = path.join('marvin-env','lib','site-packages','bin')
    new_bin_folder = path.join('marvin-env','bin')

    try:
        files = listdir(source)

        for f in files:
            not_wanted_bin = path.join('marvin-env','lib','site-packages','bin',f)
            move(not_wanted_bin, new_bin_folder)

        rmtree(source)
        print('deleted ' + source + ' folder')

    except Exception as e:
        print('This error occured when trying to remove uneeded folders to save space' + str(e) + '. If this a problem please report the error to the github repository')

    # file ran from outside marvin folder which causes path problems for file creation
else:
    print('Make sure to run this script in the Marvin-v3-client folder/directory')
