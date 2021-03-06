import os
from random import randint

from flask import Flask
from dash import Dash

from __version__ import __version__
from utils import get_dash_args_from_flask_config


def create_flask(config_object):
    """Create the Flask instance for this application"""
    server = Flask(__name__)

    # load default settings
    server.config.from_object(config_object)

    server.config.from_envvar(
        "THUY_LANGUAGE_LEARN_SETTINGS", silent=True
    )

    server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))

    return server


def create_dash(server):
    """Create the Dash instance for this application"""
    app = Dash(
        name=__name__,
        server=server,
        suppress_callback_exceptions=True,
        **get_dash_args_from_flask_config(server.config),
    )

    # Update the Flask config a default "TITLE" and then with any new Dash
    # configuration parameters that might have been updated so that we can
    # access Dash config easily from anywhere in the project with Flask's
    # 'current_app'
    server.config.setdefault("TITLE", "Dash")
    server.config.update({key.upper(): val for key, val in app.config.items()})

    app.title = server.config["TITLE"]

    if "SERVE_LOCALLY" in server.config:
        app.scripts.config.serve_locally = server.config["SERVE_LOCALLY"]
        app.css.config.serve_locally = server.config["SERVE_LOCALLY"]

    return app
