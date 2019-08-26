from flask_api import FlaskAPI
from config.env import app_env
from app.utils.slackhelper import SlackHelper
from flask import request, jsonify
from app.actions import Actions
from re import match

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config = False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')

    @app.route("/image-bot", methods=["POST"])
    def imagebot():
        command_text = request.data.get('text')
        command_text = command_text.split(' ')
        slackhelper = SlackHelper()
        actions = Actions(slackhelper)

        website = command_text[0]
        tag = command_text[1]
        image_details = command_text[2]

        response_body = actions.find_image(website, tag, image_details)
    return app