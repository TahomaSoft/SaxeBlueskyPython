# -*- mode: python; python-indent-offset: 4 -*-
from SaxeBlueskyPython.ticktocktime import unix_time_now, bsky_time_now
from SaxeBlueskyPython.saxe_bluesky import BskyCredentials, BasicPost
from FediBskyXwalk import PostXwalk
class BskyPostPuck(BskyCredentials,PostXwalk,BasicPost):
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
        
