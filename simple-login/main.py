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
        <h1>Simple Form</h1>
    </body>
</html>'''
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
