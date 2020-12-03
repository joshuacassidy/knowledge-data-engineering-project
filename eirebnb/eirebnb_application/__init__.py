import os

from flask import Flask
from eirebnb_application import home
from eirebnb_application import room_type_activities
from eirebnb_application import property_type_activities
from eirebnb_application import accommodation_activities_beds
from eirebnb_application import activity_date_availability
from eirebnb_application import accommodation_amenities_activity
from eirebnb_application import activities_rating_communication
from eirebnb_application import activity_host
from eirebnb_application import activity_type_price
from eirebnb_application import activity_acceptance
from eirebnb_application import activity_days

def create_app(test_config=None):
    app = Flask(__name__)

    app.register_blueprint(home.bp)
    app.register_blueprint(room_type_activities.bp)
    app.register_blueprint(property_type_activities.bp)
    app.register_blueprint(accommodation_activities_beds.bp)
    app.register_blueprint(activity_date_availability.bp)
    app.register_blueprint(accommodation_amenities_activity.bp)
    app.register_blueprint(activities_rating_communication.bp)
    app.register_blueprint(activity_host.bp)
    app.register_blueprint(activity_type_price.bp)
    app.register_blueprint(activity_acceptance.bp)
    app.register_blueprint(activity_days.bp)

    app.add_url_rule("/", endpoint="index")

    return app

