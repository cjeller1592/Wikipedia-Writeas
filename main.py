import requests
import json
import wikipedia

# Authenticate via Write.as through this request
data = {"alias": "blah", "pass": "blahblahblah" }

r = requests.post("https://write.as/api/auth/login",
                    data=json.dumps(data),
                    headers= {"Content-Type":"application/json"})

# A temporary way to check for exceptions, be it connection errors or client snafus(incorrect password or request)
# Will find a better way to raise exceptions - perhaps as Try/Except blocks?
r.raise_for_status()

# Once the request is successfully sent, we will grab the access token for the request
access_token = r.json()['data']['access_token']

# Now we use the Wikipedia API to grab a summary of a selected topic
topic = raw_input("Put in a topic here: ")
search = wikipedia.summary(topic, sentences=5)

# Now we construct our request...
headers = {'Authorization': "Token %s" % access_token,
            'Content-Type': 'application/json'}

# This is the post that will be published on Write.as (make as a post.json file later?)
post = {'title': topic,
        'body': search + '\n - from Wikipedia'}

# The request goes out to create the post
w = requests.post('https://write.as/api/posts', headers=headers, data=json.dumps(post))

# Grab the post so that you can go to it from the command line
url = "https://write.as/" + w.json()['data']['id']

print "Check the post here: " + url
