#!/usr/bin/python3

"""
Test and example driver for saxe blue-sky library.
Revised 11 February 2024

A test image (in the public domain) is here.
User will need to prepare a bsky.app account beforehand, and supply 
this program with the handle (@example.bsky.social)

"""


import requests
import json
from datetime import date, datetime, time, timezone, timedelta
from saxe_bluesky import bskyURLdict,BskyCredentials, credentials_dict
from saxe_bluesky import BskyFeed, BskyBlobs,  BskyPosts
from saxe_bluesky import OpenSession

from PIL import Image


# Need to supply the account handle and an app password (established
# ahead of time in the web interface for bsky.app)

# # Get my permanent id (DID) and hang on to it for this session

# Replace example.bsky.social below with your handle, within the ' '
# Don't use the trailing '@'


MyHandle = {'handle':'example.bsky.social'} 
Actor = MyHandle.get('handle')
# Provide a real app password here;
# See https://blueskyfeeds.com/en/faq-app-password as an example
APP_PASSWORD = "moo-moo-moo-moo" 

# Prompt interactively for handle and app password for testing

Actor = input("Please provide your bsky handle (username): \n ")
APP_PASSWORD = input("Please provide your application password: \n ")

MyHandle['handle'] = Actor

              

# Use this info to start populating the credentials dictionary

# bsky_creds = credentials_dict
#bsky_creds['handle'] = MyHandle.get('handle')
#bsky_creds['app_pwd'] = APP_PASSWORD

# Get the DID that goes with my handle
# print (MyHandle)

# bsky_creds= BskyCredentials.get_did (MyHandle)
bsky_creds= BskyCredentials()
bsky_creds.set_handle('atest')

bsky_creds.print()

exit()

bsky_creds['DID'] = nicedid

# Establish session, get API_Key (ephemeral)

tokens=OpenSession.open_session(bsky_creds)

bsky_creds['session_token'] = tokens['session_token']
bsky_creds['refresh_token'] = tokens['refresh_token']


print ("My blue sky credentials are: \n", bsky_creds)

# now_iso = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
now_iso = iso_time_now
now = datetime.now()

bsky_creds['session_token_create_time'] = now_iso
bsky_creds['refresh_token_create_time'] = now_iso

# Need to revisit this time delta and time formats
futuredate = datetime.now(timezone.utc) + timedelta(seconds=3)
futuredate_iso = futuredate.isoformat().replace("+00:00", "Z")

bsky_creds['session_token_expiration'] = futuredate_iso
bsky_creds['refresh_token_expiration'] = futuredate_iso

print ("My blue sky credentials now are: \n", bsky_creds)

# Get my (author) Feed
# Feed length can be from 1 to 100, inclusive
"""
feed_length = 25
# feed = json.loads (get_author_feed (bsky_creds, feed_length))
feed = json.loads (get_actor_feed (bsky_creds, feed_length))

with open ('./outputfeed.txt', 'w') as feedfile:
     print (json.dumps(feed), file=feedfile)
"""

"""
# Open and check a blob
IMAGE_PATH = "./testimage.webp"
image = Image.open(IMAGE_PATH)
blob_info = blob_prep(image)

# print (blob_info)
with open (IMAGE_PATH, "rb") as imagefile:
    blob_bytes = imagefile.read()

    # this size limit is specified in the app.bsky.embed.images lexicon
if len(blob_bytes) > 2000000:
    raise Exception (
        "image file size too large. 2MB maximum, got: {len(blob_bytes)}"
    )

# print (len(blob_bytes))

# Note: the library currently doesn't (11 Feb 2024) use the imnage dimensions.
# To be implemented later (an optional item right now in the bsky api)

this_blob = blob_basic_dict
this_blob['imageWidth'] = blob_info['img_width']
this_blob['imageHeight'] = blob_info['img_height']
this_blob['imageMimeType'] = blob_info['img_format']
this_blob['imagesizebytes'] = len(blob_bytes)
this_blob['imageFilePath'] = IMAGE_PATH
this_blob['imageAltText'] = 'Test Image'


# Upload a blob to bsky, to be embedded in a post in a later step
# Provide link to the file, the blob data dictionary, and the credentials dictionary
# returns value of the internal bsky link to the blob, needed in the embed step next

bsky_link = blob_upload(blob_bytes, this_blob, bsky_creds)
this_blob['blobLink'] = bsky_link
"""

# print (this_blob)

# Basic Post to my feed

# supply text to post and the bsky_credentials dictionary structure
simple_post_create ("Testing: And Now for more boring tests", bsky_creds)

exit ()


#images_post_create (text2post, credentials, blob_info_array, num_images)

blobs = [this_blob, this_blob]


images_post_create ("stuff", bsky_creds, blobs, 2)




