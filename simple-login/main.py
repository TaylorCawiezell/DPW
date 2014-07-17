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
        <link href='http://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css' />
        <link href='http://fonts.googleapis.com/css?family=Codystar' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body><form method='GET'>'''
        
        page_body = '''
            <h1>Blue Style</h1>
            <label>Name</label><input type='text' name='user'/><br>
            <label>Email</label><input type='email' name='email' /><br>
            <label class='check-label' for='mlist'>Email Me!</label><input type="checkbox" id='check' name="mlist" value="checkv"><br>
            <select>
                  <option value=""></option>
                  <option value=""></option>
                  <option value=""></option>
                  <option value=""></option>
            </select><br>
            <input class='button' type='submit' value='Submit' />'''
        
        page_close = '''
        </form>
    </body>
</html>'''
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' | ' + email + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #printing information
            

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
