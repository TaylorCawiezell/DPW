'''
Taylor Cawiezell

07/24/14

What Does The Fox Say?
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # if Statement to select wich print out happens based off url
        if self.request.url == 'http://localhost:17080/?dog=':
            self.response.write(Page().dp())
        elif self.request.url == 'http://localhost:17080/?cat=':
            self.response.write(Page().cp())
        elif self.request.url == 'http://localhost:17080/?fox=':
            self.response.write(Page().fp())
        else:
             self.response.write(Page().p())
            

class Page(object):
    def __init__(self):
        #writing variables for shorthand in strings
        self.d = Dog()
        self.c = Cat()
        self.f = Fox()
        self.animals = [self.d.p(),self.c.p(),self.f.p()] #array to store animals
        self.header_array = ['Select Your Animal <br>', 'The Dog <br>', 'The Cat <br>', 'The Fox <br>']
        
        #variables for HTML
        self._title = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>What does the Fox Say?</title>
        <link rel="stylesheet" type="text/css" href="css/main.css" />
        <link href='http://fonts.googleapis.com/css?family=Shadows+Into+Light|Raleway' rel='stylesheet' type='text/css' />
    </head>
    <body>'''
        
        self._header = '''<header>
        <h1 class='header'>Know Your Animals</h1>
        <h1 class='animal-head'> '''
        
        self._body = '''</h1>
        <h1>
        <form style="display: inline" method="get">
            <button name='dog'>Dog</button>
            <button name='cat'>Cat</button>
            <button name='fox'>Fox</button>
        </form><br>
        ''' 
        
        self._close = '''</h1>
        </header>
    </body>
</html>'''
    
    def dp(self): #method for writing out Dog HTML information
            return self._title + self._header + self.header_array[1] + self._body + self.animals[0] + self._close
    
    def cp(self): #method for writing Cat out HTML information
            return self._title + self._header + self.header_array[2] + self._body + self.animals[1] + self._close
    
    def fp(self): #method for writing Fox out HTML information
            return self._title + self._header + self.header_array[3] + self._body + self.animals[2] + self._close
    
    def p(self): #method for writing out HTML information if nothing is selected
            return self._title + self._header + self.header_array[0] + self._body + self._close
 
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
    
    def p(self): #method for returning variables in Dog class
        return self._phylum + self._class + self._order + self._family + self._genus + self._url + self._lifespan + self._habitat + self._geolocation + Dog().sound()
    
class Cat(Animal):
    def __init__(self):
       super(Animal, self).__init__() #animal is the super clas for Cat
       self._phylum = 'Phylum: Chordata <br>'
       self._class = 'Class: Mammalia <br>'
       self._order = 'Order: Carnivora <br>'
       self._family = 'Family: Felidea <br>'
       self._genus = 'Genus: Felis <br>'
       self._url = 'Picture: <a href= "http://petapixel.com/assets/uploads/2014/03/cat.jpg">Link to Picture</a> <br>'
       self._lifespan = 'Life Expectancy: 12-14 years <br>'
       self._habitat = 'Habitat: Wide Variety <br>'
       self._geolocation = 'Geolocation: Found All Over The World <br>'
       
    def sound(self): #Cat Sound Method
        self._sound = 'Sound: Meow'
        return self._sound
    
    def p(self): #method for returning variables in Cat class
        return self._phylum + self._class + self._order + self._family + self._genus + self._url + self._lifespan + self._habitat + self._geolocation + Cat().sound()

class Fox(Animal):
    def __init__(self):
       super(Animal, self).__init__()
       self._phylum = 'Phylum: Chordata <br>'
       self._class = 'Class: Mammalia <br>'
       self._order = 'Order: Carnivora <br>'
       self._family = 'Family: Canidae <br>'
       self._genus = 'Genus: Vulpes <br>'
       self._url = 'Picture: <a href= "http://pgcpsmess.files.wordpress.com/2014/04/red_fox.jpg">Link to Picture</a> <br>'
       self._lifespan = 'Life Expectancy: 5 years <br>'
       self._habitat = 'Habitat: Forest, Grasslands, Mountains, Deserts <br>'
       self._geolocation = 'Geolocation: Found All Over The World <br>'
       
    def sound(self): #Fox sound Method
        self._sound = 'Sound: POW POW POW POW POW POW POW'
        return self._sound
    
    def p(self): #method for returning variables in Fox class
        return self._phylum + self._class + self._order + self._family + self._genus + self._url + self._lifespan + self._habitat + self._geolocation + Fox().sound()
    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
