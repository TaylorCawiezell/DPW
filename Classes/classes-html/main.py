import webapp2
from pages import Page #from ofile import class

class MainHandler(webapp2.RequestHandler):
    def get(self):
       p = Page()
       p.body = "Miss Piggy is aweful!"
       self.response.write(p.print_out())
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
