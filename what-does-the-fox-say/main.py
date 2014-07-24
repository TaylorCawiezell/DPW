
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(Page().p()) #printing out HTML Page class
class Page(object):
    def __init__(self):
        #writing variables for shorthand in strings
        self.d = Dog()
        self.c = Cat()
        self.f = Fox()
        self.animals = [self.d.p(),self.c.p(),self.f.p()] #array to store animals
        self._header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>What does the Fox Say?</title>
    </head>
    <body>'''
        
        self._body = '''<h1> '''
        self._close = '''</h1>
    </body>
</html>'''
        
    def p(self):
        return self._header + self._body + self.animals[0] + self._close
 #Animal Class (base class for all animals)       
class Animal(object):
    def __init__(self):
        self._phylum = ''
        self._class = ''
        self._family = ''
        self._genus = ''
        self._url = ''
        self._lifespan = ''
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
       self._phylum = 'Phylum: Chordata <br>'
       self._class = 'Class: Mammalia <br>'
       self._order = 'Order: Carnivora <br>'
       self._family = 'Family: Canidae <br>'
       self._genus = 'Genus: Canis <br>'
       self._url = 'Picture: <a href= "http://1.bp.blogspot.com/-4O1cWMzu40c/Ub3NUu0jFOI/AAAAAAAABdk/l1oUkwFItvM/s1600/happy-samoyed-dog-wallpaper.jpg">Link to Picture</a> <br>'
       self._lifespan = 'Life Expectancy: 10-13 years <br>'
       self._habitat = 'Habitat: Wide Variety <br>'
       self._geolocation = 'Geolocation: Found All Over The World <br>'

    def sound(self): #polymorphed sound method
        self._sound = 'Sound: Bark'
        return self._sound
    
    def p(self): #returning strings inside the Dog class
        return self._phylum + self._class + self._order + self._family + self._genus + self._url + self._lifespan + self._habitat + self._geolocation + Dog().sound()
    
class Cat(Animal):
    def __init__(self):
       super(Animal, self).__init__()
       self._phylum = 'Phylum: Chordata <br>'
       self._class = 'Class: Mammalia <br>'
       self._order = 'Order: Carnivora <br>'
       self._family = 'Family: Felidea <br>'
       self._genus = 'Genus: Felis <br>'
       self._url = 'Picture: <a href= "http://petapixel.com/assets/uploads/2014/03/cat.jpg">Link to Picture</a> <br>'
       self._lifespan = 'Life Expectancy: 12-14 years <br>'
       self._habitat = 'Habitat: Wide Variety <br>'
       self._geolocation = 'Geolocation: Found All Over The World <br>'
       
    def sound(self):
        self._sound = 'Sound: Meow'
        return self._sound
    
    def p(self):
        return self._phylum + self._class + self._order + self._family + self._genus + self._url + self._lifespan + self._habitat + self._geolocation + Cat().sound()

class Fox(Animal):
    def __init__(self):
       super(Animal, self).__init__()
       self._phylum = 'Phylum: yo <br>'
       self._class = 'Class: animal <br>'
       self._order = 'Order: order <br>'
       self._family = 'Family: dog <br>'
       self._genus = 'Genus: hello <br>'
       self._url = 'Picture: <a href= "www.pic.com">Link to Picture</a> <br>'
       self._lifespan = 'Life Expectancy: 16 years <br>'
       self._habitat = 'Habitat: grass <br>'
       self._geolocation = 'Geolocation: everywhere <br>'
       
    def sound(self):
        self._sound = 'Sound: POW POW POW POW POW POW POW'
        return self._sound
    
    def p(self):
        return self._phylum + self._class + self._order + self._family + self._genus + self._url + self._lifespan + self._habitat + self._geolocation + Fox().sound()
    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
