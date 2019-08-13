from datetime import datetime
from config import db, ma
# import the database and marshmellow setup from config file

class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PersonSchema(ma.ModelSchema):
    class Meta:
        """
        A class that defines how the data is mapped
        """
        model = Person
        # tells what model to serialize to/from

        sqla_session = db.session
        # tells what database session to use