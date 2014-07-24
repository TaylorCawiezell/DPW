import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
       p = FormPage();
       p.inputs = [['first','text','First Name'],['last','text','Last Name'],['Submit','submit'] ]
       self.response.write(p.print_out_form())
        
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
            '''
            #if third item add it in
            if len(item) > 2:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            else:
                self._form_inputs += '" />'
            '''
    
        print self._form_inputs
    
    def print_out_form(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close
        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
