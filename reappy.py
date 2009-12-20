from urllib2 import urlopen, Request
from urllib import urlencode
from dateutil import parser
import os
import re
import cPickle
import time
try:
    import simplejson as json
except ImportError:
    import json

USER_AGENT = "reappy application/0.1"



class User:
    def __init__(self, data):
        self.profile_image_url = data['profile_image_url']
        self.user_name = data['from_user']

class Tweet:
    def __init__(self, data):
        self.user = User(data)
        self.text = data['text']
        self.id = data['id']
        self.source = data['source']
        self.language = data['iso_language_code']
        self.created = parser.parse(data['created_at'])

    
class Application():
    def __init__(self, handlers):
        self.handlers = [(re.compile(r[0], re.IGNORECASE), r[1]) for r in handlers]
        if os.path.exists('since_id.data'):
            since_id_file = file('since_id.data', 'r')
            self.since_id = cPickle.load(since_id_file)
        else:
            self.since_id = None

    def _persist_since_id(self):
        save_file = file('since_id.data', 'w')
        cPickle.dump(self.since_id, save_file)
        save_file.close()

    def get_tweets_since(self, since_id):
        pass
    
    def run(self):
        tweets = self.get_tweets_since()
        if tweets:
            self.since_id = tweets[0].id
            self._persist_since_id()
        for t in tweets:
            for r, h in self.handlers:
                match = r.match(t.text)
                if match:
                    kargs = match.groupdict()
                    h(t, **kargs)

    def loop(self, poll_frequency=5):
        while True:
            self.run()
            time.sleep(poll_frequency)

class SearchApplication(Application):
    def __init__(self, search_term, handlers):        
        Application.__init__(self, handlers)
        self.search_term = search_term
        
    def _persist_since_id(self):
        save_file = file('since_id.data', 'w')
        cPickle.dump(self.since_id, save_file)
        save_file.close()
        
    def _grab_results(self, search_url):
        req = Request(search_url, headers={'User-Agent': USER_AGENT})
        results = json.loads(urlopen(req).read())
        return results

    def _build_url(self, search_query, since_id=None):
        params = {'q':search_query, 'rpp':100}
        if since_id: params['since_id'] = since_id
        return "http://search.twitter.com/search.json?" + urlencode(params)

    def get_tweets_since(self):        
        url = self._build_url(self.search_term, since_id=self.since_id)
        return [Tweet(rd) for rd in self._grab_results(url)['results']]
