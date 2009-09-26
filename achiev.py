from reappy import *

def BeingHandler(x):
    print x.text

def NotHandler(x, name):
    print "%s is not %s" % (x.user.user_name, name)

app = Application("@yuvipanda",
                  [(r'.*being.*', BeingHandler),
                   (r'.*not (?P<name>\S+).*', NotHandler)])

app.loop()
    
