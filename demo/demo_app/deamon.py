from reappy import Application
from models import Opinion

def RocksHandler(tweet):
    o = Opinion()
    o.text = tweet.text
    o.user_name = tweet.user.user_name
    o.opinion = 'R'
    o.save()

def SucksHandler(tweet):
    o = Opinion()
    o.text = tweet.text
    o.user_name = tweet.user.user_name
    o.opinion = 'S'
    o.save()

app = Application("#pyconindia",
                    [(r'.*sucks.*', SucksHandler),
                     (r'.*rocks.*', RocksHandler)])

def run():
    app.loop()
