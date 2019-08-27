from config import get_env
import requests
from bs4 import BeautifulSoup
import urllib.request

class Actions:
    def __init__(self, slackhelper):
        self.slackhelper = slackhelper
    
    def find_image(self, website, tag, image_details):
        response = requests.get(website)
        soup = BeautifulSoup(response.text, "html.parser")

        image_details = image_details.split("=")

        if image_details[0] == "class":
            middle = "."
        elif image_details[0] == "id":
            middle = "#"

        selector = tag

        image_details[1] = image_details[1].split(" ")

        for single in image_details[1]:
            selector += middle + single

        images = soup.select(selector)
        if len(images) > 0:
            image = soup.select(selector)[0]
            picture_url = image['src']
            self.slackhelper.post_image(picture_url)

            return {"image_found": True}
        
        else:
            return {"image_found": False}