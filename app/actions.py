from config import get_env
import requests
from bs4 import BeautifulSoup
import urllib.request

class Actions:
    def __init__(self, slackhelper):
        self.slackhelper = slackhelper
    
    def find_image(self, website, tag, image_details):
        """
        Grabs the website content and parses it using beautifulsoup. Searches 
        through the soup using the passed in tag and image details. If the image
        is found it calls the slack post message API and returns a true json. Else,
        it returns a false json.
        """
        response = requests.get(website)
        soup = BeautifulSoup(response.text, "html.parser")

        image_details = image_details.split("=")

        if image_details[0] == "class":
            middle = "."
        elif image_details[0] == "id":
            middle = "#"

        selector = tag

        image_details[1] = image_details[1].split(" ")

        for single in image_details[1]: #if it has multiple classes
            selector += middle + single

        images = soup.select(selector)
        if len(images) > 0: #checks to make sure there is more than one image found
            image = soup.select(selector)[0]
            picture_url = image['src'] #extracts the src url
            self.slackhelper.post_image(picture_url) #calls the slack api

            return {"image_found": True}
        
        else:
            return {"image_found": False}