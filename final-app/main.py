
import webapp2
import urllib2 #python classes and code needed to open url information
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        if self.request.GET:
            #get info from api
            mm = MovieModel()# creates model
            mm.search = self.request.GET['search']
            mm.search = self.request.GET['search'].replace(" ","+")
            #searchcode = search
            mm.callApi()#tells it to connect to api
            mv = MovieView()#creates view
            #takes data objects from MOdel and gives view
            #page._body = mv.movie
            page._body = mm.callApi()
            
        self.response.write(page.print_out())

class MovieView(object):
    '''This class handle how the weather is shown'''
    def __init__(self):
        self.__movie = '<br>'
    
    def update(self):
        self.__movie += mi.title + '<br>' + '<img src="' +mi.poster+'" />' + '<br> release year: ' + str(mi.year) + '<br> critic rating ' +  str(mi.rating) + '<br> length ' + str(mi.runtime)  + ' minutes '  + '<br>' + mi.synopsis
            
    @property
    def movie(self):
        return self.__movie
         
    @property
    def movie(self):
        pass
    
    @movie.setter
    def movie(self):
        self.update()
        
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
           
    
        #parsing JSON
        jsondoc = json.load(result)
        
        mi = MovieInformation()
        mi.poster = jsondoc['movies'][0]['posters']['thumbnail']
        mi.year = jsondoc['movies'][0]['year']
        mi.title = jsondoc['movies'][0]['title']
        mi.rating = jsondoc['movies'][0]['ratings']['critics_score']
        mi.synopsis = jsondoc['movies'][0]['synopsis']
        mi.runtime = jsondoc['movies'][0]['runtime']
        print mi.poster
        
        return  mi.title + '<br>' + '<img src="' +mi.poster+'" />' + '<br> release year: ' + str(mi.year) + '<br> critic rating ' +  str(mi.rating) + '<br> length ' + str(mi.runtime)  + ' minutes '  + '<br>' + mi.synopsis
            
        
    
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
