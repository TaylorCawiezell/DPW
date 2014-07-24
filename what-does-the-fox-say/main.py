
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
       
 #Animal Class (base class for all animals)       
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
    #sound method, will be polymorphed
    def sound(self):
        self._sound = ''
        return self._class
# Dog class inherited from animal class
class Dog(Animal):
    def __init__(self):
       super(Animal, self).__init__() #Making animal the Super class of Dog
       self._phylum = 'yo'
       self._class = 'animal'
       self._family = 'dog'
       self._genus = 'hello'
       self._url = 'www.pic.com'
       self._lifespan = '16' + ' years'
       self._habitat = 'grass'
       self._geolocation = 'everywhere'

    def sound(self): #polymorphed sound method
        self._sound = 'Bark'
        return self._sound
    
    def p(self): #returning strings inside the Dog class
        return self._phylum + self._class + self._family + self._genus + self._url + self._lifespan + self._habitat + self._geolocation
    


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
