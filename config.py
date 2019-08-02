import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# create connexion app
connex_app = connexion.App(__name__, specification_dir=basedir)

# get the underlying Flask app instance
app = connex_app.app

# config the SQAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True # sets it so SQL statements are echoed to console
# prob should disable this if you deploy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'people.db')
# sets up the DB
# use sqlite as the db, and store the db as people.db in the local directory
# different db tools will have different config options
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# turn off SQLAlchemy's event system
# the event system is great, but it just adds overhead if you don't need it

# create sqlalchemy db instance
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)