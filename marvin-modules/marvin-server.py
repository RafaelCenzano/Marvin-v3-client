import requests
import json

r = requests.post('heroku thing login', data=json.dumps({'email':'test@example.com', 'password':'test123'}), headers={'content-type': 'application/json'})
