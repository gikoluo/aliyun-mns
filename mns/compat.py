
try:
    from httplib import HTTPConnection, BadStatusLine, HTTPSConnection
    import ConfigParser
except:
    from http.client import HTTPConnection, BadStatusLine, HTTPSConnection
    import configparser as ConfigParser

