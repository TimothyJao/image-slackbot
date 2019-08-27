# Image Slackbot

This image slackbot was created as a coding challenge for American Express.

## Introduction

This Slackbot was created as a headless browser by using slack and connecting it to the Slackbot API. I also utilized BeautifulSoup to help parse the data and find the image. 

Thank you to Abdulqahhar Aminujatto for his [article](https://medium.com/the-andela-way/how-to-build-a-task-notification-bot-for-slack-with-python-part-1-333cb50985f4) that taught me how to set up a slackbot with Flask.

## How to Use
To use this slackbot, go to the designated channel and type: /slackbot (url) (tag) (class=xxxxxx)/(id=xxxxxx)

## Tecnologies
* Flask
* Beautiful Soup
* Slack API

## Examples

Here we use the example given to us in the prompt to find the image using the slackbot
<br />
<br />
<img src="./assets/images/correct-image1.gif" align="center">
<br />
<br />

Another example of the slackbot correctly working to grab Abdulqahhar's image from his medium post
<br />
<br />
<img src="./assets/images/correct-image2.gif" align="center">
<br />
<br />

An example with an input where the img does not exist. Notice that the image-found is returned as *false* to notify the user that the image cannot be found.
<br />
<br />
<img src="./assets/images/incorrect-image.gif" align="center">
<br />
<br />

## Installation

To install this slackbot in your own slack channel, follow these instructions:

1. Go to [your apps](https://api.slack.com/apps) on Slack, create a new app and fill out the information.

2. Click on bot users and add a new bot users using whatever name and username you desire.

3. Go to Install App under settings and install the app under your slack workspace. Record the OAuth Access token and Bot User OAuth Access token.

4. Fork this repo to have your own clone of the code. Create a new git repository with ```git init```, add the new content with ```git add .``` and commit the changes with a message using ```git commit -m "(enter a message of your choice here)"```

5. Create a Heroku account if you don't have one already, install the Heroku Toolbelt CLI and use ```heroku login``` to login to the heroku CLI

6. Create a new heroku app by using ```heroku create [appname]```

7. Login to your heroku dashboard, select this project, and go to settings. Click on __Reveal Config Vars__ and add the following key-value pairs as shown below.

8. Push the code by runnin ```git push heroku master```

9. Go to the app's page and select *Slash Commands* under __Features__. Select *Create New Command* and fill out the information.\

The slackbot should now be running on your own workspace! Test it out and grab images from online!