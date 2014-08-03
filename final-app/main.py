
import webapp2
import urllib2 #python classes and code needed to open url information
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        
            
        self.response.write(page.print_out())


class MovieModel(object):
    def __init__(self):
        self.__url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=amgmm7669zxyxdf64mkk6pj2&q='
        self.__search = ''
        self.json = ''
        #contact API
        #open the URL
        #parse
    
    #requests and loads information from api
    def callApi(self):
        #assemble request
        request = urllib2.Request(self.__url+self.__search+'&page_limit=5')
        #use the urllib2 to create an object to get the url
        opener = urllib2.build_opener()
        # use the url to get a result - request info from the API
        result = opener.open(request)
           
    
        
        
    
    @property
    def search(self):
        pass
    
    @search.setter
    def search(self, s):
        self.__search = s
        
class Page():
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Film Found</title>
        <meta charset="utf-8" />
        <link href='http://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body>
        <header>
            <h1>Just type a Movie into the Search bar!</h1>
        </header>'''
        self._search = '<form method=GET><input type="text" name="search" spellcheck="true" required /><input type="submit" value="go" /></form>'
        self._body = MovieInformation().rating
        self._close = '''
    </body>
</html>'''
    
        print self._body
    
    def print_out(self):
        return self._head + self._search + self._body + self._close
    
class MovieInformation(object):
    def __init__(self):
        self.title = ''
        self.runtime = ''
        self.rating = ''
        self.review = ''
        self.year = ''
        self.synopsis = ''
        self.poster = ''
        
    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
