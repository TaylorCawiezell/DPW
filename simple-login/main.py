'''
Taylor
7/13/14
DPW
Simple Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Welcome!</title>
    </head>
    <body>
        <form method='GET'>
            <label>Name:</label><input type='text' name='user'/>
            <label>Name:</label><input type='text' name='email' />
            <input type='submit' value='Submit' />
        </form>
    </body>
</html>'''
        self.response.write(page) #printing information

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
