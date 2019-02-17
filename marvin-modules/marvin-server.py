# env imports
import sys
from os import path
sys.path.insert(0, path.join('marvin-env','lib','site-packages')) # make env sitepackages folder in path for pip installed libraries

# marvin imports
import requests
import json

r = requests.post('heroku thing login', data=json.dumps({'email':'test@example.com', 'password':'test123'}), headers={'content-type': 'application/json'})
