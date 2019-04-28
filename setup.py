# Imports
from os import path, mkdir, listdir, remove, getcwd
from platform import system as platform
from os import system as terminal
from shutil import rmtree, move
import sys

try:
    confirm = input('\n\n\n\nConfirm that you want to run setup.py. y/n? ').lower()
except:
    print('\nNot python 3\n')
    sys.exit(0)
if confirm == 'y' or confirm == 'yes' or confirm == 'true':
    pass
else:
    print('\nsetup.py cancled by user\n')
    sys.exit(0)

tqdm_here = False

# Run code if file directly called and app.py, requirements.txt, and
# __init__.py in marvin-env exists to make many checks that setup.py
# called in right directory
if __name__ == '__main__' and path.isfile('marvin.py') and path.isfile(
        'requirements.txt') and path.isfile(path.join('marvinenv', 'lib', 'sitepackages', '__init__.py')):

    try:
        if platform() == 'Darwin' and path.isfile('/usr/local/Homebrew/bin/brew') == False:
            print('MAC os detected\nHomebrew not found\nMarvin virtual assistant needs homebrew to install portaudio\n')
            allow_brew_install = input('Allow the setup.py to install Homebrew using Ruby and cURL? y/n? ').lower()

            if allow_brew_install == 'y' or allow_brew_install == 'yes' or allow_brew_install == 'true':
                print('\n\nInstalling Homebrew from https://raw.githubusercontent.com/Homebrew/install/master/install\n\n')
                terminal('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

                allow_portaudio_install = input('Allow the setup.py to install portaudio using Homebrew? y/n? ').lower()
                if allow_portaudio_install == 'y' or allow_portaudio_install == 'yes' or allow_portaudio_install == 'true':
                    print('\n\nInstalling portaudio from Homebrew\n\n')
                    terminal('brew install portaudio')
            else:
                print('There will be an error later when installing pyaudio. Read more about port audio here: http://www.portaudio.com/')

        else:
            allow_portaudio_install = input('Allow the setup.py to install portaudio using Homebrew? y/n? ').lower()
            if allow_portaudio_install == 'y' or allow_portaudio_install == 'yes' or allow_portaudio_install == 'true':
                print('\n\nInstalling portaudio from Homebrew\n\n')
                terminal('brew install portaudio')
            else:
                print('There will be an error later when installing pyaudio. Read more about port audio here: http://www.portaudio.com/')

    except Exception as e:
        print(f'There was an error when working with Homebrew: {e}')

    try:
        # install required libraries into marvin-env
        print('\nInstalling needed libraries\n')
        marvin_env = path.join('marvinenv','lib','sitepackages')
        terminal(f'pip3 install  -r requirements.txt -t {marvin_env}')

        # dependencies couldn't be installed
    except Exception as e:
        print(f'We ran into a problem\nPlease report this issue: {e} \nFiles couldn\'t be installed properly')

        # make list full of uneeded folders created from pip installs

    uneeded_dirs = [
        'SpeechRecognition-3.8.1.dist-info',
        'word2number-1.1.dist-info',
        'beautifulsoup4-4.6.3.dist-info',
        'chardet-3.0.4.dist-info',
        'certifi-2018.10.15.dist-info',
        'idna-2.7.dist-info',
        'gTTS_token-1.1.2.dist-info',
        'Click-7.0.dist-info',
        'playsound-1.2.2.dist-info',
        'gTTS-2.0.1.dist-info',
        'requests-2.20.0.dist-info',
        'six-1.11.0.dist-info',
        'PyAudio-0.2.11.dist-info',
        'bs4-0.0.1.dist-info']

    try:
        # for all uneeded folders delete them
        print('\nDeleting uneeded folders\n')
        for dirs in uneeded_dirs:

            # create path to folder to delete
            folder = path.join('marvinenv', 'lib', 'sitepackages', dirs)

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
        print(f'This error occured when trying to remove uneeded folders to save space: {e}. If this a problem please report the error to the github repository')
    '''
    source = path.join('marvinenv', 'lib', 'sitepackages')
    new_bin_folder = path.join('marvinenv', 'bin')

    try:
        files = listdir(source)

        for f in files:
            not_wanted_bin = path.join('marvinenv', 'bin', f)
            move(not_wanted_bin, new_bin_folder)

        rmtree(source)
        print('deleted ' + source + ' folder')

    except Exception as e:
        print(f'This error occured when trying to remove uneeded folders to save space: {e}. If this a problem please report the error to the github repository')
    '''
    try:
        absolute_path = getcwd()
        path_file = open(path.join('marvinenv','path.py'), 'w+')
        path_file.write(f'marvin_path = \'{absolute_path}\'')
        path_file.close()
    except Exception as e:
        print(f'This error occured when trying to save data: {e}. If this a problem please report the error to the github repository')

    # file ran from outside marvin folder which causes path problems for file
    # creation
else:
    print('Make sure to run this script in the Marvin-v3-client folder/directory')
