from flask import Blueprint

home = Blueprint('404', __name__)

import app.home.views
