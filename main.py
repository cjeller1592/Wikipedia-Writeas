import requests
import json

import wikipedia
import writeas

from settings import token

c = writeas.NewClient()
c.setToken(token)

# Now we use the Wikipedia API to grab a summary of a selected topic
topic = raw_input("Put in a topic here: ")
search = wikipedia.summary(topic, sentences=5)


# This is the post that will be published on Write.as (make as a post.json file later?)
title = topic
body = '>' + search + '\n\n -- from Wikipedia'

# The request goes out to create the post
p = c.createPost(body, title)
# Grab the post so that you can go to it from the command line
url = "https://write.as/" + p['id'] + '.md'

print "Check the post here: " + url
