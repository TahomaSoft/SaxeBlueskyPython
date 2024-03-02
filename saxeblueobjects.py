''' docstring '''
# -*- mode: python; python-indent-offset: 4 -*-
import requests
import json
# import ticktocktime
from ticktocktime import unix_time_now, bsky_time_now
from saxe_bluesky import BskyCredentials, BasicPost


class BskyPostPuck(BskyCredentials,PostXwalk,BasicPost):
    ''' bsky post entry class
    individual post/entry
    Might be deprecated
    '''

    def __init__(self):
        super().__init__()
        self.basicPost = {}

        self.delxPost = {}
        self.blobsum = {}
        self.blobinfo = []


    def print(self):
        for i in self.basicPost:
            print (self.basicPost)

        for j in self.delxPost:
            print (self.delxPost)

        return

    def bEcho(self):
        return self.basicPost

    def dEcho(self):
        return self.delxPost


    def bDataIngest(self,FBxo,bsky_creds):
        DID = bsky_creds['DID']
        text2post = FBxo['textReady2Post']
        nowtime = bsky_time_now()
        payloadPrep = {
            'repo': DID,
            'collection': 'app.bsky.feed.post',
            # 'rkey': 'string',
            'validate': True,
            'labels': [],
            'record': {
                'text' : text2post,
                'createdAt': nowtime,
                '$type': 'app.bsky.feed.post',
                'langs': ['en'],
            }
        }
        self.basicPost = payloadPrep
        self.creds = bsky_creds
        return

    def bCredIngest(self,bsky_creds):
        self.creds = bsky_creds
        return


    def dlxDataIngest(self,FBxo,bsky_creds):
        DID = bsky_creds['DID']
        text2post = FBxo['textReady2Post']
        nowtime = bsky_time_now()
        payloadPrep = {
            'repo': DID,
            'collection': 'app.bsky.feed.post',
            # 'rkey': 'string',
            'validate': True,
            'labels': [],
            'record': {
                'text' : text2post,
                'createdAt': nowtime,
                '$type': 'app.bsky.feed.post',
                'langs': ['en'],
            }
        }
        self.delxPost = payloadPrep
        return

    def bUpDataIngest (self,FBxo,bsky_creds):
        return

    def bBlobLinks (self, bloblinks):
        return


    def simple_post (self):
        return

class SimplePostQueue:
    ''' queue for simple bsky post '''
    def __init__(self,bsky_crd):
        self.s_p_queue = []
        self.rcode_list = []
        self.bsky_cred = bsky_crd
        self.API_URL = \
            'https://bsky.social/xrpc/com.atproto.repo.createRecord'
        self.p_template = {
            'repo': 'DID_credentials',
            'collection': 'app.bsky.feed.post',
            # 'rkey': 'string',
            'validate': True,
            'labels': [],
            'record': {
                'text' : 'text2post',
                'createdAt': 'now-time',
                '$type': 'app.bsky.feed.post',
                'langs': ['en'],
            }
        }
        self.h_template = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer <TOKEN>',
        }

    def item_add (self, rawentry):
        ''' compose a simple bsky post '''
        URL = self.API_URL
        DID = self.bsky_cred['DID']
        ses_tok = self.bsky_cred['session_token']

        text2post = rawentry['fix']
        create_time = bsky_time_now()

        header_entry = self.h_template
        header_entry['Authorization'] = 'Bearer' + ' ' + ses_tok

        payload_entry = self.p_template
        payload_entry['repo'] = DID
        payload_entry['record']['text'] = rawentry['basic_text_rev']
        payload_entry['record']['createdAt'] = create_time



        entry = (URL,header_entry,payload_entry)


        self.s_p_queue.append (entry)
        return entry

    def json_queue (self):
        print (json.dumps(self.s_p_queue))
        return

    def post_all_in_queue(self):
        for i in self.s_p_queue:
            rcode = post_the_post(i(0),i(1),i(2)) # URL, Header, Payload
            self.rcode_list.append(rcode)

            return self.rcode_list


# End Class


# Start Functions

def post_the_post(URL,headers,payload):
    r = requests.post(URL,headers,
                      json.dumps(payload))

    if r.status_code != 200:
        print ("Status Code", r.status_code)
        print ("Message", r.text)
        raise Exception("Status code other than 200 indicates a problem")

    elif r.status_code == 200:
        return r.status_code

def PostXwalk():
    ''' dummy '''
    return
