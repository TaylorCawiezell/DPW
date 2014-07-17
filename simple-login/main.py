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
            <h1>Blue Stitch</h1>
            <label>Name</label><input type='text' name='user'/><br>
            <label>Address</label><input type='text' name='address'/><br>
            <label>Email</label><input type='email' name='email' /><br>
            <label class='check-label' for='mlist'>Subscribe</label><input type="checkbox" name="mlist" value="yes"><br>
            <label>I need... </label><select name='select'>
                  <option value="pants">Pants</option>
                  <option value="jacket">Jacket</option>
                  <option value="shirt">Shirt</option>
                  <option value="shoes">Shoes</option>
            </select><br>
            <input class='button' type='submit' value='Pre-Order' />'''
        
        page_close = '''
        </form>
    </body>
</html>'''
        
        page_com = '''
            <h1>Voila!</h1>
            <h2>We will email you when we have the goods!</h2>
            '''
        
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            address = self.request.GET['address']
            checkbox = bool(self.request.GET.get('mlist'))
            selected = bool(self.request.GET.get('select'))
            print(selected)
            print(checkbox)
            self.response.write(page_head + page_com + user + '<br>' + address + '<br>' + email + '<br>Email listing: ' + str(checkbox) + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #printing information

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
