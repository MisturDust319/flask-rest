"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# import flask code
from flask import (
    make_response,
    abort,
)

# import app config code
from config import db
from models import (
    Person,
    PersonSchema,
)

def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    people = Person.query \
        .order_by(Person.lname) \
        .all()

    # Serialize the data for the response
    person_schema = PersonSchema(many=True)
    # creates an iterable compatible schema for the data
    # many sets whether it's for iterables
    return person_schema.dump(people).data
    # use the schema object to dump people into a list
    # connexion can automatically convert this list to JSON

def read_one(person_id):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people

    :param person_id:   ID of person to find
    :return:            person matching ID
    """
    # Get the person requested
    person = Person.query \
        .filter(Person.person_id == person_id) \
        .one_or_none()

    # Did we find a person?
    if person is not None:

        # Serialize the data for the response
        person_schema = PersonSchema()
        return person_schema.dump(person).data

    # Otherwise, nope, didn't find that person
    else:
        abort(404, 'Person not found for Id: {person_id}'.format(person_id=person_id))
