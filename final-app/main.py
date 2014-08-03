
import webapp2
import urllib2 #python classes and code needed to open url information
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #variable for test page
        page = Page()
        #if statement for requesting information
        if self.request.GET:
            #get info from api
            mm = MovieModel()# creates model
            mm.search = self.request.GET['search']#gets search input for users quiery
            mm.search = self.request.GET['search'].replace(" ","+")#replaces spaces with plus to make searches work 
            mm.callApi()#tells it to connect to api
            mv = MovieView()#creates view
            
            #takes data objects from Model and gives view
            #page._body = mv.movie # not working coming up as none type
            page._body = mm.callApi()
         #printing html information   
        self.response.write(page.print_out())

class MovieView(object):
    '''This class handle how the movie object should be shown however its not working
       No matter what I put as the update method I'm getting the same results'''
    def __init__(self):
        self.__movie = '<br>'
    #suppose to update the movie variable
    def update(self):
        self.__movie += mi.title + '<br>' + '<img src="' + mi.poster+'" />' + '<br> release year: ' + str(mi.year) + '<br> critic rating ' +  str(mi.rating) + '<br> length ' + str(mi.runtime)  + ' minutes '  + '<br>' + mi.synopsis
    #propperty for movie variable      
    @property
    def movie(self):
        return self.__movie
    #passing on getter    
    @property
    def movieup(self):
        pass
    #setter for movie tried multipe ways of changing with no result 
    @movie.setter
    def movieup(self):
        self.update()
        
class MovieModel(object):
    ''' this is the model for the movie wich gets data from json and puts it into variables'''
    def __init__(self):
        #url variables with API key
        self.__url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=amgmm7669zxyxdf64mkk6pj2&q='
        #search variable for eventual user input
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
        #variables for json information
        mi = MovieInformation()
        mi.poster = jsondoc['movies'][0]['posters']['thumbnail']
        mi.year = jsondoc['movies'][0]['year']
        mi.title = jsondoc['movies'][0]['title']
        mi.rating = jsondoc['movies'][0]['ratings']['critics_score']
        mi.synopsis = jsondoc['movies'][0]['synopsis']
        mi.runtime = jsondoc['movies'][0]['runtime']
        print mi.poster
        # displaying the json information correctly
        return  mi.title + '<br>' + '<img src="' +mi.poster+'" />' + '<br> Release Year: ' + str(mi.year) + '<br> Critic Rating: ' +  str(mi.rating) + '<br> Length: ' + str(mi.runtime)  + ' minutes '  + '<br><br>' + mi.synopsis
            
        
    
    @property
    def search(self):
        pass
    #to sett search variable to polymorph
    @search.setter
    def search(self, s):
        self.__search = s
        
class Page():
    #class for creating web page layout
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
        <div class='content'>
        <header>
            <h1 class='title'>Film Found!</h1><img src='css/icon.png' />
            <h1>Just type a Movie into the Search bar!<h1 class='movie'>
        </header>'''
        self._search = '<form method=GET><input type="text" name="search" spellcheck="true" required /><input type="submit" value="go" /></form><h1>'
        self._body = ''
        self._close = '''
        </h1>
        </div>
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
