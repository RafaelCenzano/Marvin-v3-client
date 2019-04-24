import urllib2

def internet_on():
    try:
        urllib2.urlopen('http://192.30.253.113', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False