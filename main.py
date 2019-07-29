__name__ = "__main__"

from flask import render_template

import connexion

# create app instance
app = connexion.App(__name__, specification_dir='./')

# read the swagger.yml file to config endpoints
app.add_api('swagger.yml')
# this is a YAML or JSON file that configures i/o validation
# url endpoint definition, and Swagger UI

# create URL route in app for "/"
@app.route('/')
def home():
    """
    responds to URL localhost:5000/
    :return: rendered template 'home.html'
    """
    return render_template('home.html')

# if in standalone mode, run app
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)