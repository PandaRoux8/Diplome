from flask import Flask, request, render_template, abort

app = Flask("Rest API test")


@app.route("/")
def index():
    return "Index"

# by default a string is passed
# URL = http://127.0.0.1:5002/module/abc
@app.route("/module/<name>")
def modules(name):
    return "Modules : %s " % name

# int: for passing an int as parameter
# URL = http://127.0.0.1:5002/module/3
@app.route("/module/<int:id>")
def module_id(id):
    return "Id of the module %s " % id

# path: for a string that accepts '/'
# URL = http://127.0.0.1:5002/module/'/usr/bin/test'
@app.route("/module/<path:module_path>")
def module_path(module_path):
    return "Module path : %s " % module_path


@app.route("/auth", methods=['GET', 'POST'])
def auth():
    print(request, request.form)
    if request.method == 'POST':
        if request.form.get('test') == 'auth':
            return "Authenticated"
        else:
            # Logging
            app.logger.warning("Unauthenticated user try to use the app")
            # Return error message
            abort(401)
    else:
        # Logging
        app.logger.warning("An error occured")
        # Rendering a template, looks for a "templates" folder in the sys.path and select the one with the matching
        # name.
        return render_template('fail.html')


# Run the app
app.run(port="5002")
