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
from saxe_bluesky import bskyURLdict, fetch_DID, credentials_dict, open_session 
from saxe_bluesky import get_author_feed, blob_basic_dict, blob_prep
from saxe_bluesky import blob_upload, simple_post_create, images_post_create
from saxe_bluesky import get_actor_feed, BskyCredentials, BasicPost, ImagePost


from PIL import Image


x = BskyCredentials()
y = BasicPost()
q = ImagePost()


x = BskyCredentials.init_cred(x)
handle = 'slutguy.com'
apppwd = 'Venomous^Exclude^Kimono8'

x = BskyCredentials.get_did(x, handle)
# print (x.cred)

x = BskyCredentials.start_session(x,apppwd)
# t = x.get_cred('')
print (x)
