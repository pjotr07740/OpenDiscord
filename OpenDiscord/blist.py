'''
This is the blist.xyz API Wrapper.

Example
.. highlight:: python
.. codeblock:: python
    from OpenDiscord import blist

    blist_api = blist.api(bot_id, token) # Token is optional unless you are doing POST request, if you still try it will trow a 400 status code and a missing key error.

    id = blist_api.get_id()
    name = blist_api.get_name()

    owners = blist_api.get_owners() # Will return a list of all the owner's ids
    for owner in owners:
        print(owner)

'''
import json
from datetime import datetime

import requests

class API:
    '''
    The actual API Wrapper class
    '''
    def __init__(self, bot_id, authorization=None):
        '''
        bot_id: The bot id this cannot be None.
        authorization: Authorization this can be None unless you are making POST requests then it will trow an error
        '''
        self.bot_id = bot_id
        self.authorization = authorization

        self.url = "https://blist.xyz/api"

    def get_id(self):
        '''
        The target bots ID
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return int(request['id'])

    def get_name(self):
        '''
        Name of the bot
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['name']

    def get_main_owner(self):
        '''
        ID of the bots main owner
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return int(request['main_owner'])

    def get_owners(self):
        '''
        The bots secondary owners
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        owners_string = request['owners'].split()
        owners_int = []
        for owner in owners_string:
            owners_int.append(int(owner))
        return owners_int

    def get_library(self):
        '''
        The library the bot is coded in
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['library']

    def get_website(self):
        '''
        The bots website
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['website']

    def get_github(self):
        '''
        The bots github repo
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['github']

    def get_short_description(self):
        '''
        The bots short description
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['short_description']

    def get_prefix(self):
        '''
        The bots prefix
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['prefix']

    def get_invite_url(self):
        '''
        The bots invite url
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['invite_url']

    def get_support_server(self):
        '''
        The invite code of the bots support server
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['support_server']

    def get_tags(self):
        '''
        List of bots categories its been tagged with
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['tags']

    def get_monthly_votes(self):
        '''
        Amount of times the bots been voted for during the current month
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['monthly_votes']

    def get_total_votes(self):
        '''
        Amount of times the bots been voted for
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['total_votes']

    def get_certified(self):
        '''
        Whether the bot is certified
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        if request['certified'] == 'false':
            return False
        else:
            return True

    def get_vanity_url(self):
        '''
        The bots vanity
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['vanity_url']

    def get_server_count(self):
        '''
        The bots server count
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['server_count']

    def get_shard_count(self):
        '''
        The bots shard count
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['shard_count']

    def get_add_date(self):
        '''
        Returns the add data and time in the following format: Y-M-D H:M:S
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        ts = request['add_date']
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    def get_invites(self):
        '''
        Amount of times the bot has been invited from the site
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['invites']

    def get_page_views(self):
        '''
        Amount of times the page has been viewed
        '''
        request = requests.get(self.url + f"/bot/{self.bot_id}/stats/").json()
        return request['page_views']
