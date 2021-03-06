# Yahoo XML file link
#http://xml.weather.yahoo.com/forecastrss?p=

import webapp2
import urllib2 #python classes and code needed to open url information (request, recieve, open).
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
       p = FormPage()
       p.inputs = [ ['zip','text','Zip Code'],['Go!','submit'] ]
       
       if self.request.GET:
           #get info from api
           wm = WeatherModel()# creates model
           wm.zip = self.request.GET['zip']
           wm.callApi()#tells it to connect to api
           wv = WeatherView()#creates view
           wv.wdos = wm.dos #takes data objects from MOdel and gives view
           p._body = wm.dos
       
       self.response.write(p.print_out())
            
class WeatherView(object):
    '''This class handle how the weather is shown'''
    def __init__(self):
        self.__wdos = []
        self.__content = '<br>'
    
    def update(self):
        for do in self.__wdos:
            self.__content += do.day + ' High: ' + do.high + ' Low: ' + do.low + ' Cnodish' + do.condition
            
        
    @property
    def content(self):
        return self.__content
         
    @property
    def wdos(self):
        pass
    
    @wdos.setter
    def wdos(self, arr):
        self.__wdos = arr
        self.update()
        
class WeatherModel(object):
    '''This model handles fetching parsing and sorting data
    '''
    def __init__(self):
        self.__url = 'http://xml.weather.yahoo.com/forecastrss?p='
        self.__zip = ''
        self.__xmldoc = ''
        #contact API
        #open the URL
        #parse
    
    #requests and loads information from api
    def callApi(self):
        #assemble request
        request = urllib2.Request(self.__url+self.__zip)
        #use the urllib2 to create an object to get the url
        opener = urllib2.build_opener()
        # use the url to get a result - request info from the API
        result = opener.open(request)
        #parse the XML
        self.__xmldoc = minidom.parse(result)
        #self.content = '<br>'
        
        #sorting Data
        list = self.__xmldoc.getElementsByTagName("yweather:forecast")
        self._dos = []
        for tag in list:
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high = tag.attributes['high'].value
            do.low = tag.attributes['low'].value
            do.date = tag.attributes['date'].value
            do.condition = tag.attributes['code'].value
            self._dos.append(do)
   
    @property
    def dos(self):
        return self._dos     
        
    
    @property
    def zip(self):
        pass
    
    @zip.setter
    def zip(self, z):
        self.__zip = z

class WeatherData(object):
    def __init__(self):
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''
        self.date = ''
        
class Page(object): #borrowing from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''
        
        self._body = 'Filler'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
       super(FormPage, self).__init__() #custructor fuction for the super class
       self._form_open = '<form method="GET">'
       self._form_close = '</form>'
       self.__inputs = []
       self._form_inputs = ''
       
       #<input type='text' value='' name='first' placeholder='First Name' />
       #<input type='text' value='' name='last' placeholder='Last Name' />
       #<input type='submit' value='Submit' />
       
    @property
    def inputs(self):
        pass
    
    @inputs.setter
    def inputs(self, arr):
        #change my private variable 
        self.__inputs = arr
        #sort though the mega array and create html inputs based on the info there
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            except:
                self._form_inputs += '" />'
    
    #polymorphism METHOD OVERRIDING!
    def print_out(self):
        return self._head + self._form_open + self._form_inputs + self._form_close + self._body + self._close
        

        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
