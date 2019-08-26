from config import get_env
import requests
from bs4 import BeautifulSoup
import urllib.request

class Actions:
    def __init__(self, slackhelper):
        self.slackhelper = slackhelper
    
    def find_image(self, website, tag, image_details):
        response = requests.get(url_input)
        soup = BeautifulSoup(response.text, "html.parser")

        class_input = class_input.split("=")

        if class_input[0] == "class":
            middle = "."
        elif class_input[0] == "id":
            middle = "#"

        selector = tag_input

        class_input[1] = class_input[1].split(" ")

        for single in class_input[1]:
            selector += middle + single

        image = soup.select(selector)[0]
        picture_url = image['src']
        self.slackhelper.post_image(picture_url)

        return None
        # f = open('image.jpg', 'wb')
        # f.write(requests.get(picture_url).content)
        # f.close()

        # return 'image.jpg'