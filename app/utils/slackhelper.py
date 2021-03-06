from slack import WebClient
from config import get_env

class SlackHelper:

    def __init__(self): #grabs the envrionment variables and identifies the slack workspace we will use
        self.slack_token = get_env('SLACK_TOKEN') 
        self.slack_client = WebClient(self.slack_token) 
        self.slack_channel = get_env('SLACK_CHANNEL')

    def post_image(self, image_url): 
        """
        Uses the slack API to send a picture as a slack message by using the src url
        """
        return self.slack_client.chat_postMessage(
            channel = self.slack_channel,
            blocks = [
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Enjoy your photo!"
                    },
                    "block_id": "image4",
                    "image_url": image_url,
                    "alt_text": "Photo requested by the user."
                }
            ]
        )