import sys
from platform import system
if system() == 'Windows':
    sys.path.insert(0, 'marvin-env\\lib\\site-packages') # make env sitepackages folder in path for pip installed libraries
    sys.path.insert(0, 'marvin-env\\lib\\marvin-modules') # make env marvin-modules folder in path for pip installed libraries
else:
    sys.path.insert(0, 'marvin-env/lib/site-packages') # make env sitepackages folder in path for pip installed libraries
    sys.path.insert(0, 'marvin-modules') # make env marvin-modules folder in path for pip installed libraries

from flask import Flask, render_template, request, make_response, redirect, request
import json

# sMarvin UI created with flask

app = Flask(__name__, template_folder='templates', static_folder='static')# declare flask app and point to html files for ui

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return redirect("/404_not_found", code=302) # redirect to /404_not_found

# Redirects to main routes
@app.route('/', methods=['GET']) # dashboard route
@app.route('/home', methods=['GET']) # dashboard route
@app.route('/marvin', methods=['GET']) # dashboard route
@app.route('/dashboards', methods=['GET']) # dashboard route
def dashboardRedirect():
    return redirect("/dashboard", code=302) # redirect to /dashboard

@app.route('/email', methods=['GET']) # dashboard route
def emailRedirect():
    return redirect("/dashboard", code=302) # redirect to /dashboard

# Main Routes

@app.route('/dashboard', methods=['GET']) # dashboard route
def dashboard():
    return render_template('dashboard.html') # render dashboard.html for UI

@app.route('/sendemail', methods=['GET']) # dashboard route
def sendemail():
    return render_template('contacts.html', options=['item','hello']) # render contacts.html for UI

# Misc Routes

@app.route('/404_not_found', methods=['GET'])
def not_found():
    return render_template('not_found.html')

@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True)
