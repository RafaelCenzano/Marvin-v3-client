from flask import Flask, render_template, request, make_response, redirect

'''
Marvin UI created with flask
'''

app = Flask(__name__, template_folder='templates')# declare flask app and point to html files for ui

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/', methods=['GET']) # home route
def index():
    return redirect("/dashboard", code=302) # redirect to dashboard

@app.route('/dashboard', methods=['GET']) # dashboard route
def dashboard():
    return render_template('dashboard.html') # render dashboard.html for UI