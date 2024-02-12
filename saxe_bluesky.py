"""

This is the main module for the saxe-blue(sky) python little library
to post basic text and basic text with images (and alt image info) to bsky.app (aka BlueSky, bsky.social).

It uses BlueSky's atproto's XRPC API to make the posts.

This is a basic start of a python library to post to bsky.app.



"""
import requests
import json
from datetime import date, datetime, time, timezone, timedelta
from PIL import Image


bskyURLdict = {
    'Get_DID_from_Handle'  : 'https://bsky.social/xrpc/com.atproto.identity.resolveHandle',
    'Create_Session' : 'https://bsky.social/xrpc/com.atproto.server.createSession',
    'Refresh_Session': 'https://bsky.social/xrpc/com.atproto.server.refreshSession',
    'Blob_Up' : 'https://bsky.social/xrpc/com.atproto.repo.uploadBlob',
    'Create_Record' : 'https://bsky.social/xrpc/com.atproto.repo.createRecord',
    'Get_Author_Feed' : 'https://bsky.social/xrpc/app.bsky.feed.getAuthorFeed'
}

credentials_dict = {
    'handle': 'static_text',
    'DID': 'static_text',
    'app_pwd': 'semi-static_text',
    'session_token': 'ephemeral',
    'refresh_token': 'ephemeral',
    'API_create_time': 'reserved',
    'API_Expiration': 'reserved'
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

# API expires in 60 to 120 seconds. see https://atproto.com/specs/xrpc

def get_DID (handle):
    handle_header = {
        'Accept': 'application/json'
    }
    
    URL = bskyURLdict.get('Get_DID_from_Handle')
    payload = handle
    
    r = requests.get(URL, headers=handle_header, params=payload)
    
    if r.status_code != 200:
        print ("Status Code", r.status_code)
        print ("Message", r.text)
        raise Exception("Status code other than 200 indicates a problem")

    elif r.status_code == 200:
        roughdid = r.text
        jsondid = json.loads(roughdid)
        did = jsondid.get('did')

    return did

# Open a session, get the API Key


def open_session (credentials):  # credentials are handle, did, and app password, and ephemeral API token and more 
        
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
    return tokens

def get_author_feed (credentials, feed_length):
    URL = bskyURLdict.get('Get_Author_Feed')

    # check feed_length. Between 1 and 100
    if feed_length < 1 or feed_length > 100:
        print ("Feed length requested ", feed_length, "Is too long")
        print ("Must be between 1 and 100, inclusive")
        raise Exception ("Feed Length Requested too long")

    pass
    
    
    actor = credentials.get('handle')
    feed_payload = {
        'actor': actor,
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
        return (feed)

    
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
        "record": {
            "text" : text2post,
            "createdAt": now,
            "$type": 'app.bsky.feed.post'
        }
     
    }
    r = requests.post(URL,headers=post_headers, data=json.dumps(post_payload))
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
        # print ("\n blbs is: \n", blbs)
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
    
    
    
