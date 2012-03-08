from datetime import date
import requests
import logging
import time
import json
import re

import pprint

import config
from database import *

 
class PlayerScraper(object):
    sleep = 2
    base_url = 'http://worldoftanks.%s/community/accounts/%s/'
    
    def __init__(self, player, clan):
        self.id = player['account_id']
        self.name = player['name']
        self.joined = datetime.date.fromtimestamp(player['member_since'])
        self.clan = clan
        self.fetch_data()
        
    def fetch_data(self):
        url = self.base_url % ('com' if self.clan.region == 'us' else self.clan.region, str(self.id))
        response = requests.get(url)
        if response.status_code != 200:
            logging.info('PLAYER: Server responded with %d on resource %s' % (response.status_code, url))
            return #TODO
        self.parse_page(response.content)
        
    def parse_page(self, content):
        pass
        


class ClanScraper(object):
    sleep = 1.5
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'X-Requested-With': 'XMLHttpRequest'}
    members_url = '/members/?type=table'
    fetched = False
    
    def __init__(self, url):
        pattern = r'.+?worldoftanks\.([\w]+)/[a-z-/]+([\d]+)'
        m = re.search(pattern, url)
        if len(m.groups()) != 2:
            raise Exception('Couldn\'t parse url')
        self.region = 'us' if m.group(1) == 'com' else m.group(1)
        self.id = int(m.group(2))
        self.url = url
        self.name = url #TODO
        self.fetch_members()
        
    def fetch_members(self, retry=3):
        self.members = []
        for run in xrange(0,retry):
            response = requests.get(self.url+self.members_url, headers=self.headers)
            if response.status_code != 200:
                logging.info('CLAN: Server responded with %d on resource %s' % (response.status_code, url))
                time.sleep((run + 1) * self.sleep)
                continue
            try:
                table = json.loads(response.content)
            except ValueError:
                break
            
            for player in table['request_data']['items']:
                self.members.append(PlayerScraper(player, self))
                time.sleep(self.sleep)
            self.fetched = True
            break
        else:
            pass
        
        logging.info('Fetched %d members for clan %s' % (len(self.members), self.name))
        return self.members

    def db_repr(self):
        if not self.fetched:
            fetch_members()
            


def main():
    clans = []
    for clan_url in config.clans:
        clans.append(ClanScraper(clan_url))

    

if __name__ == '__main__':
    main()