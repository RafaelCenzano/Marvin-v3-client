from flask import Flask, render_template, request, make_response, redirect

'''
Marvin UI created with flask
'''

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
        return render_template('dashboard.html') # render dashboard.html for UI

# Misc Routes

@app.route('/404_not_found', methods=['GET'])
def not_found():
    return render_template('not_found.html')

if __name__ == '__main__':
    app.run(debug=True)
