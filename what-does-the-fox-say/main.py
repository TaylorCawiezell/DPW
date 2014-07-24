
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
       
        
class Animal(object):
    def __init__(self):
        self._phylum = ''
        self._class = ''
        self._family = ''
        self._genus = ''
        self._url = ''
        self._lifespan = '' + ' years'
        self._habitat = ''
        self._geolocation = ''
    
    def sound(self):
        return self._class



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
