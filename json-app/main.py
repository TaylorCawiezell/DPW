# Yahoo XML file link
#http://xml.weather.yahoo.com/forecastrss?p=

import webapp2
import urllib2 #python classes and code needed to open url information (request, recieve, open).
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
       p = FormPage();
       p.inputs = [ ['city','text','City'],['country','text','Country'],['Go!','submit'] ]
       self.response.write(p.print_out())
       
       if self.request.GET:
           #get info from api
           city = self.request.GET['city']
           country = self.request.GET['country']
           url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country
           #assemble request
           request = urllib2.Request(url)
           #use the urllib2 to create an object to get the url
           opener = urllib2.build_opener()
           # use the url to get a result - request info from the API
           result = opener.open(request)
           
           #parsing JSON
           jsondoc = json.load(result)
           
           name = jsondoc['name']
           weather = jsondoc['weather'][0]['description']
           temp = jsondoc['main']['temp']
           
           self.response.write("City Chosen: " + name + '<br>The Weather at your location : '+weather + '<br>' + str(temp))
           
           
           
           
           
           '''#parse the XML with Etree
           xmldoc = ET.parse(result)
           root = xmldoc.getroot()
           
           namespace = "http://xml.weather.yahoo.com/ns/rss/1.0" 
           
           self.content = '<br>'
           self.content = root[0][12][7].attrib['day'] + "<br>"
           for i in root.iter("{" + namespace + "}forecast"):
               content += i.attrib['day'] + "---HIGH" + i.attrib['high']
               
            self.responce.write(content)'''
        
class Page(object): #borrowing from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>''''
        
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
            '''
            #if third item add it in
            if len(item) > 2:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            else:
                self._form_inputs += '" />'
            '''
    
        print self._form_inputs
    
    #polymorphism METHOD OVERRIDING!
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close
        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
