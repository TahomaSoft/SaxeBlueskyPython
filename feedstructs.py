'''
Feed info data structures
Data structure for main configuration elements
'''


simple_bsky_info = {
    'Username': 'A user Name',
    'App_passwd': 'a app password',
    'Nickname': 'account nickname',
    'DefaultSensitive': bool(False)
}

main_config_genInfo = {
    'Title': 'Overall Config Name',
    'Statefile': 'name of the file to write state info',
    'TZ_abbr': 'UTC',
    'NumFeeds': 1
}

main_config_feedInfo = {
    'Name': 'Arbitrary Feed name for reference',
    'Number': 0,
    'URL': 'URL of the feed',
    'Type': 'rss',
    'TimeJitter': 0
}

state_config_genInfo = {
    'Title': 'a title'
}


feed_metadata = {
    'Name': 'Nick name for feed',
    'Number': 'item number',
    'URL':'feed url string',
    'feed_last_read_iso': 'iso time',
    'feed_last_read_unix': 'unixtime',
    'feed_previous_last_read_iso': 'iso time',
    'feed_previous_last_read_unix': 'unixtime',
    'newest_feed_item_unix':'unixtime',
    'newest_feed_item_iso':'iso time',
    'oldest_feed_item_iso': 'iso time',
    'oldest_feed_item_unix': 'unixtime',
}

bsky_post_metadata = {
    'previous_last_posted_unix':'unixtime',
    'previous_last_posted_iso': 'iso time',
    'last_posted_unix': 'unixtime',
    'last_posted_iso': 'iso time',
}

'''
    Main data structure from fediverse posts
    Content warning is currently unused;
'''

post_constructor = {
    'ELEMENTsequence':'integer in sequence 0',
    'original_url': 'long url from mastodon',
    'media_rating': 'nonadult, adult,...',
    'rating': 'reserved',
    'html_text':'Original string from _summary_ ',
    'html_text_sdetail':  'original string from _summary_detail_',
    'basic_text': 'string',
    'basic_text_rev': 'revised version of basic text, after cw filtering',
    'raw_text2post' : 'string',
    'orig_post_time': 'convert to unixtime',
    'number_of_media': 'integer, 0-4 (hopefully)',
    'lang_of_post': 'string',
    'alt_lang_post': 'language string in a different part of the post',
    'base_post_mime_t': 'string',
    'media_array': 'to be constructed from post_media_detail',
    'altTextSet': 'to be constructed from _content_ if present',
    'published_parsed': 'published parsed python',
    'tags': 'list of tags',
    'fixed_tags': 'cleaned list of tags',
    'base_url': 'base location of feed',
    'content_warn': 'content_warning if any',
    'content_rating':'adult, not adult, etc',
    'sensitive_post': 'boolean, true or false',
    'post_privacy': 'reserved',
    'contentWarn': 'reserved',
    'textReady2Post': 'cleaned up text'
}


post_altText_plus = {
    'altText': '',
     # alt text string for media
    'lang':'',
    #'post of language nested in _content_ ',
    'base':'',
    # 'base link to poster in _content_ ',
    'value':''
    # 'the alt text for an image',
}

post_media_item = {
    'media_url': 'string',
    'media_type': 'mime-type-string',
    'media_size_stated': 'fsize in bytes from fediverse rss post',
    'media_size_calculated': 'use system to find size',
    'medium_type': 'image,video,etc',
    'localFilePath': 'file path and file name on local system',
    'alt Text': 'alt text string'

}

# media_array = [post_media_item]

'''
post_content_warn = {
    'content_warn': 'content_warning if any',
    'content_rating':'adult, not adult, etc',
    'media_rating':'adult, not adult, etc',
    'sensitive_media': 'boolean, true or false',
}
'''
