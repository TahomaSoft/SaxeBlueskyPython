# -*- mode: python; python-indent-offset: 4 -*-

"""

This is the main module for the saxe-blue(sky) python little library
to post basic text and basic text with images
(and alt image info) to bsky.app (aka BlueSky, bsky.social).

It uses BlueSky's atproto's XRPC API to make the posts.

This is a basic start of a python library to post to bsky.app.



"""
import syslog
import requests
import json
from datetime import date, datetime, time, timezone, timedelta
from PIL import Image
# From feedstructs import post_media_item

credentials_dict = {
    'handle': 'static_text',
    'DID': 'static_text',
    'app_pwd': 'semi-static_text',
    'session_token': 'ephemeral',
    'refresh_token': 'ephemeral',
    'session_token_create_time': 'reserved',
    'refresh_token_create_time': 'reserved',
    'session_token_expiration': 'reserved',
    'refresh_token_expiration': 'reserved',

}

blob_basic_dict = {
    'imageMimeType': 'MimeImageTypeString_like_image/jpg',
    'imageFilePath': '/dev/null/foo.jpg',
    'imagesizebytes' : 0,
    'blobLink': 'TBD',
    'imageHeight': 0,
    'imageWidth':0,
    'imageAltText': 'TBD'
}

basic_post_dict = {
    'fediPostItems': {
        'fixed_tags': 'cleaned list of tags',
        'base_url': 'base location of feed',
        'content_rating':'adult, not adult, etc',
        'textReady2Post': 'cleaned up text',
        'number_of_media': 'integer, 0-4 (hopefully)',
        'sensitive_post':'sensitive_post boolean',
        'contentWarn': 'content Warning',
        'media_detail': 'post_media_item',
    },
    
    'repo': 'credentials_DID',
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

bskyURLdict = {
    'Get_DID_from_Handle'  : 'https://bsky.social/xrpc/com.atproto.identity.resolveHandle',
    'Create_Session' : 'https://bsky.social/xrpc/com.atproto.server.createSession',
    'Refresh_Session': 'https://bsky.social/xrpc/com.atproto.server.refreshSession',
    'Blob_Up' : 'https://bsky.social/xrpc/com.atproto.repo.uploadBlob',
    'Create_Record' : 'https://bsky.social/xrpc/com.atproto.repo.createRecord',
    'Get_Author_Feed' : 'https://bsky.social/xrpc/app.bsky.feed.getAuthorFeed',
    'Get_Actor_Feed': 'https://bsky.social/xrpc/app.bsky.feed.getActorFeeds',
    'Get_Home_Timeline':'https://bsky.social/xrpc/app.bsky.feed.getTimeline'
}

class BskyStruct:
    def __init__(self):
        self.bpost_dict = basic_post_dict
        
    def INIT (self):
        return self.bpost_dict

    
class BskyCredentials:
    def __init__(self):
        self.cred = credentials_dict
                                
    def printCred(self):
        print (self.cred)

    def _getHandle(self):
        return self.cred['handle']
    
    def set_handle(self, handle):
        self.cred['handle'] = handle

    def set_appPW(self,appPW):
        self.cred['app_pwd'] = appPW

    def echo(self):
        return self.cred
    
    def json (self):
        print (json.dumps(self.cred))
    
      
    def get_did(self):
      
        handle_header = {
            'Accept': 'application/json'
        }
        URLset = bskyURLdict
        URL = URLset.get('Get_DID_from_Handle')
        handle = self._getHandle()
        
        payload =  {'handle': handle}
        
        r = requests.get(URL, headers=handle_header, params=payload)
        
        if r.status_code != 200:
            print ("Status Code", r.status_code)
            print ("Message", r.text)
            raise Exception("Status code other than 200 indicates a problem")
        
        elif r.status_code == 200:
            roughdid = r.text
            jsondid = json.loads(roughdid)
            did = jsondid.get('did')
            self.cred['DID'] = did
        else:
            print ("we are lost")
            
        return self.cred['DID']

    def myDID (self):
        return self.cred['DID']
        
    def start_session(self):
        
        URL = bskyURLdict.get('Create_Session')

        content_info_header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        prepayload = {
            'identifier':self.cred['DID'],
            'password': self.cred['app_pwd']
        }

        payload = json.dumps(prepayload)

        r = requests.post(URL, headers=content_info_header, data=payload)

        if r.status_code != 200:
            print ("Status Code", r.status_code)
            print ("Message", r.text)
            raise Exception("Status code other than 200 indicates a problem")
        
        elif r.status_code == 200:
            temp_i = json.loads (r.text)
            session_token = temp_i.get('accessJwt')
            refresh_token = temp_i.get('refreshJwt')
            tokens = {
                'session_token': session_token,
                'refresh_token': refresh_token
            }

        self.cred['session_token'] = tokens['session_token']
        self.cred['refresh_token'] = tokens['refresh_token']
        
        return self.cred
    
    def show_creds(self):
        return self.cred

    def get_sessT(self):
        return self.cred['session_token']

    def session_refresh(self):
        #stuff
        return 


class BasicPost:
    def __init__(self):

        self.post_payload = {
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
        
    def display (self):
        print (json.dumps(self.post_payload))
            
    def add_text (self, text2use):
        self.post_payload['record']['text'] = text2use
                
    def post_data (self):
        return self.post_payload
                
    def make_post (self):
        print ("hllo")


class ImagePost (BasicPost):

    BasicPost.image_info = {
        '$type': 'app.bsky.embed.images',
        'alt': 'imageAltText',
        'image': {
            '$type': 'blob',
            'ref': {
                '$link': 'blobLink'
            },
            'mimeType': 'imageMimeType',
            'size': 'imagesizebytes',
        }
    }

    BasicPost.image_dim = {
        'img_width': 'img.width',
        'img_height': 'img.height',
        'img_format': 'image_format'
    }

    BasicPost.Images = [BasicPost.image_info]

    BasicPost.Embed =  {
        "embed": {
            "$type": "app.bsky.embed.images",
            "images": BasicPost.Images
        }
    }
    def add_images(BasicPost,num_images):
        BasicPost.post_payload['record'].update(BasicPost.Embed)








# image_post_dict =  #child class




# For later
# content_rating_dict = {}

# API expires in 60 to 120 seconds. see https://atproto.com/specs/xrpc



# Open a session, get the API Key
class OpenSession:
    def set_post_content_warnings():
        return


    def open_session (credentials):
        '''
        credentials are handle, did, and app password,
        and ephemeral API token and more
        '''
        
        URL = bskyURLdict.get('Create_Session')

        content_info_header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        prepayload = {
            'identifier': credentials.get('DID'),
            'password': credentials.get('app_pwd')
        }

        payload = json.dumps(prepayload)

        r = requests.post(URL, headers=content_info_header, data=payload)

        if r.status_code != 200:
            print ("Status Code", r.status_code)
            print ("Message", r.text)
            raise Exception("Status code other than 200 indicates a problem")

        elif r.status_code == 200:
            temp_i = json.loads (r.text)
            session_token = temp_i.get('accessJwt')
            refresh_token = temp_i.get('refreshJwt')
            tokens = {
                'session_token': session_token,
                'refresh_token': refresh_token
            }
            # assign tokens
        else:
            print ('We are lost')
            
        return credentials


class BskyFeed:
    def get_author_feed (credentials, feed_length):
        # Get actor's 'author feed'; posts and reposts by the author
        URL = bskyURLdict.get('Get_Author_Feed')

        # check feed_length. Between 1 and 100
        if feed_length < 1 or feed_length > 100:
            print ("Feed length requested ", feed_length, "Is too long")
            print ("Must be between 1 and 100, inclusive")
            raise Exception ("Feed Length Requested too long")

        author = credentials.get('handle')
        feed_payload = {
            'actor': author,
            'limit': feed_length
        }

        Session_Token = credentials.get('session_token')

        feed_header = {
            'Authorization': 'Bearer' + ' ' + Session_Token
        }

        r = requests.get(URL, headers=feed_header, params=feed_payload)

        if r.status_code != 200:
            print ("Status Code", r.status_code)
            print ("Message", r.text)
            raise Exception("Status code other than 200 indicates a problem")
        elif r.status_code == 200:
            feed = r.text
            return feed

    def get_actor_feed (credentials, feed_length):
        # Get actor's feed generator feeds/records

        URL = bskyURLdict.get('Get_Actor_Feed')
        # check feed_length. Between 1 and 100
        if feed_length < 1 or feed_length > 100:
            print ("Feed length requested ", feed_length, "Is too long")
            print ("Must be between 1 and 100, inclusive")
            raise Exception ("Feed Length Requested too long")

        else:

            actor = credentials.get('handle')
            Session_Token = credentials.get('session_token')

            actor_header = {
                'Accept': 'application/json',
                'Authorization': 'Bearer' + ' ' + Session_Token
            }

            actor_payload = {
                'actor': actor,
                'limit': feed_length
            }

            r = requests.get(URL, headers=actor_header, params=actor_payload)


            if r.status_code != 200:
                print ("Status Code", r.status_code)
                print ("Message", r.text)
                raise Exception("Status code other than 200 indicates a problem")

            elif r.status_code == 200:
                feed = r.text
        return feed

class BskyBlobs:

    def blob_prep (image_filehandle):

        img = image_filehandle
        # print('width: ', img.width)
        # print('height:', img.height)
        i = img.format
        image_format = 'image/' + i.lower()
        # print (image_format)

        i_dict = {
            'img_width': img.width,
            'img_height': img.height,
            'img_format': image_format
        }
        return (i_dict)




    def blob_upload (image_filehandle, blob_info, credentials):
        # blob_info is blob_basic_dict
        # Credentials are credentials_dict
        img = image_filehandle

        URL = bskyURLdict.get ('Blob_Up')

        blob_payload = img
        blob_headers = {
            'Content-Type': blob_info['imageMimeType'],
            'Accept': 'application/json',
            'Authorization': 'Bearer' + ' ' + credentials['session_token']
        }

        r = requests.post(URL, headers=blob_headers, data=blob_payload)
        if r.status_code != 200:
            print ("Status Code", r.status_code)
            print ("Message", r.text)
            raise Exception("Status code other than 200 indicates a problem")

        elif r.status_code == 200:
            j = json.loads(r.text)
            b = j.get('blob')
            ref = b.get('ref')
            bsky_link = ref.get('$link')

        return bsky_link

class BskyPosts:

    def post_simple_ready (BluePost,session_token):
        URL = bskyURLdict.get ('Create_Record')
        post_headers  = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer' + ' ' + session_token
        }
        post_payload = BluePost
        # print(post_payload)
    
        r = requests.post(URL,headers=post_headers,
            data=json.dumps(post_payload))
        if r.status_code != 200:
            print ("Status Code", r.status_code)
            print ("Message", r.text)
            raise Exception("Status code other than 200 indicates a problem")
        
        elif r.status_code == 200:
            return r.status_code    
        else:
            print ("we are lost")
                
                
        
                    
    def simple_post_create (text2post,credentials):
        URL = bskyURLdict.get ('Create_Record')
        now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        post_headers  = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer' + ' ' + credentials['session_token']
        }

        post_payload = {
            "repo": credentials['DID'],
            "collection": "app.bsky.feed.post",
            # "rkey": "string",
            "validate": True,
            "labels": [],
            "record": {
                "text" : text2post,
                "createdAt": now,
                "$type": 'app.bsky.feed.post',
                'langs': ['en'],
            }

        }

        r = requests.post(URL,headers=post_headers,
            data=json.dumps(post_payload))
        if r.status_code != 200:
            print ("Status Code", r.status_code)
            print ("Message", r.text)
            raise Exception("Status code other than 200 indicates a problem")

        elif r.status_code == 200:
            return r.status_code


    def images_post_create (text2post,credentials,blob_info_array, num_images):
        URL = bskyURLdict.get ('Create_Record')
        if num_images < 1 or num_images > 4:
            print ("Number of images isn't right; must be an integer between 1 and 4, inclusive")
            raise Exception("Wrong number of images")

        if isinstance(blob_info_array,list) == False:
            computedblobs = 1
        elif isinstance(blob_info_array,list) == True:
            computedblobs = len(blob_info_array)

            # check num_images with what is in the blob_info_array
            # compare length of blob_basic_dict with size of blob_info_array
            # If only one image, isinstance(blob_info_array, list) is false
            # If multiple images isinstance(blob_info_arrray, list) is true, and use len(blob_info_array)

            # Add aspect Ratio later

            if num_images == computedblobs:
                pass

            elif num_images != computedblobs:
                print ("Number of images listed doesn't match number of images in blob array")
                raise Exception("Image count mismatch")


            I_post_headers  = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Bearer' + ' ' +  credentials['session_token']
            }


            if computedblobs == 1:
                blb = blob_info_array

                hImage = {
                    '$type': 'app.bsky.embed.images',
                    'alt': blb.get('imageAltText'),
                    'image': {
                        '$type': 'blob',
                        'ref': {
                            '$link': blb.get('blobLink')
                        },
                        'mimeType': blb.get('imageMimeType'),
                        'size': blb.get('imagesizebytes')
                    }
                }
                hImages = [hImage]


            elif computedblobs > 1:
                blbs = blob_info_array
                hImage = {
                    '$type': 'app.bsky.embed.images',
                    'alt': 'Brief Alt Text Descripton',
                    'image': {
                        '$type': 'blob',
                        'ref': {
                            '$link': '_LinkVariable'
                        },
                        'mimeType': '_MimeTypeVariable',
                        'size': '_SizeOfBlobVariable'
                    }
                }

            hImages = [hImage]


            for x in range (1, computedblobs):
                hImages.append(hImage)

                for k in range (0, computedblobs):

                    hImages[k]['alt'] = blbs[k].get('imageAltText')
                    hImages[k]['image']['ref']['$link'] = blbs[k].get('blobLink')
                    hImages[k]['image']['mimeType'] = blbs[k].get('imageMimeType')
                    hImages[k]['image']['size'] = blbs[k].get('imagesizebytes')

                    # print("K is: \t hImages[k] is: \n", k, hImages[k])


                else:
                    raise Exception("Should not ever reach here")

                hEmbed =  {
                    "embed": {
                        "$type": "app.bsky.embed.images",
                        "images": hImages
                    }
                }

                now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
                I_post_payload = {
                    "repo": credentials['DID'],
                    "collection": "app.bsky.feed.post",
                    # "rkey": "string",
                    "validate": True,
                    "record": {
                        "text" : text2post,
                        "createdAt": now,
                        "$type": 'app.bsky.feed.post',
                        "embed": 'PlaceHolder'
                    }
                }

                I_post_payload['record'] |= hEmbed

                r = requests.post(URL,headers=I_post_headers, data=json.dumps(I_post_payload))

                if r.status_code != 200:
                    print ("Status Code", r.status_code)
                    print ("Message", r.text)
                    raise Exception("Status code other than 200 indicates a problem")

                elif r.status_code == 200:
                    return r.status_code
