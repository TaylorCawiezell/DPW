'''
Taylor
7/13/14
DPW
Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Welcome!</title>
    </head>
    <body>'''
        
        page_body = '''<form method='GET'>
            <label>Name:</label><input type='text' name='user'/>
            <label>Name:</label><input type='text' name='email' />
            <input type='submit' value='Submit' />'''
        
        page_close = '''
        </form>
    </body>
</html>'''
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' | ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #printing information
            

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
